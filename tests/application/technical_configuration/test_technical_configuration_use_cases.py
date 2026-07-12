from __future__ import annotations

from copy import deepcopy
from dataclasses import FrozenInstanceError
from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.application.technical_configuration.add_technical_component import (
    AddTechnicalComponentRequest,
)
from mfm.application.technical_configuration.add_technical_component import (
    AddTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    BusinessRuleViolation,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    CreateTechnicalConfigurationRequest,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    CreateTechnicalConfigurationResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    CreateTechnicalConfigurationUseCase,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    RepositoryException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    SpecificationEntryInput,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    ValidationException,
)
from mfm.application.technical_configuration.get_technical_configuration import (
    GetTechnicalConfigurationRequest,
)
from mfm.application.technical_configuration.get_technical_configuration import (
    GetTechnicalConfigurationUseCase,
)
from mfm.application.technical_configuration.install_technical_component import (
    InstallTechnicalComponentRequest,
)
from mfm.application.technical_configuration.install_technical_component import (
    InstallTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.remove_technical_component import (
    RemoveTechnicalComponentRequest,
)
from mfm.application.technical_configuration.remove_technical_component import (
    RemoveTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.replace_technical_component import (
    ReplaceTechnicalComponentRequest,
)
from mfm.application.technical_configuration.replace_technical_component import (
    ReplaceTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.update_technical_component_details import (
    UpdateTechnicalComponentDetailsRequest,
)
from mfm.application.technical_configuration.update_technical_component_details import (
    UpdateTechnicalComponentDetailsUseCase,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.domain.technical_configuration.technical_component import TechnicalComponent
from mfm.domain.technical_configuration.technical_component_status import (
    TechnicalComponentStatus,
)
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)
from mfm.domain.technical_configuration.technical_configuration import (
    TechnicalConfiguration,
)
from mfm.infrastructure.persistence.sqlite.sqlite_technical_configuration_repository import (
    SQLiteTechnicalConfigurationRepository,
)
from mfm.repositories.technical_configuration_repository import (
    TechnicalConfigurationRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class InMemoryTechnicalConfigurationRepository(TechnicalConfigurationRepository):
    def __init__(
        self,
        store: dict[UUID, TechnicalConfiguration],
        *,
        fail_on_add: bool = False,
        fail_on_update: bool = False,
    ) -> None:
        self._store = store
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

        self.add_calls = 0
        self.update_calls = 0
        self.get_by_id_calls = 0
        self.get_by_vessel_id_calls = 0

    def add(self, configuration: TechnicalConfiguration) -> None:
        self.add_calls += 1
        if self._fail_on_add:
            raise RuntimeError("add failed")
        self._store[configuration.id.value] = configuration

    def get_by_id(self, configuration_id: UUID) -> TechnicalConfiguration | None:
        self.get_by_id_calls += 1
        return self._store.get(configuration_id)

    def get_by_vessel_id(self, vessel_id: UUID) -> TechnicalConfiguration | None:
        self.get_by_vessel_id_calls += 1
        return next(
            (
                configuration
                for configuration in self._store.values()
                if configuration.vessel_id == vessel_id
            ),
            None,
        )

    def update(self, configuration: TechnicalConfiguration) -> None:
        self.update_calls += 1
        if self._fail_on_update:
            raise RuntimeError("update failed")
        self._store[configuration.id.value] = configuration

    def delete(self, configuration_id: UUID) -> None:
        self._store.pop(configuration_id, None)

    def exists(self, configuration_id: UUID) -> bool:
        return configuration_id in self._store

    def list(self) -> list[TechnicalConfiguration]:
        return list(self._store.values())

    def search(self, text: str) -> list[TechnicalConfiguration]:
        lowered = text.casefold()
        return [
            configuration
            for configuration in self._store.values()
            if lowered in str(configuration.vessel_id).casefold()
            or any(
                lowered in component.name.casefold()
                for component in configuration.list_components()
            )
        ]


class FakeTechnicalConfigurationUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        fail_add: bool = False,
        fail_update: bool = False,
    ) -> None:
        super().__init__()
        self.fail_add = fail_add
        self.fail_update = fail_update

        self.configurations: dict[UUID, TechnicalConfiguration] = {}

        self.commits = 0
        self.rollbacks = 0
        self.last_repository: InMemoryTechnicalConfigurationRepository | None = None

    def _start_scope(self) -> None:
        self._snapshot = deepcopy(self.configurations)
        self.technical_configuration_repository = InMemoryTechnicalConfigurationRepository(
            self.configurations,
            fail_on_add=self.fail_add,
            fail_on_update=self.fail_update,
        )
        self.last_repository = self.technical_configuration_repository

    def _commit_impl(self) -> None:
        self.commits += 1

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self.configurations = self._snapshot

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


def _create_sqlite_session() -> tuple[object, Session]:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


class SQLiteTechnicalConfigurationApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session

    def _start_scope(self) -> None:
        self.technical_configuration_repository = SQLiteTechnicalConfigurationRepository(
            UnitOfWork(self._session)
        )

    def _commit_impl(self) -> None:
        self._session.commit()

    def _rollback_impl(self) -> None:
        self._session.rollback()

    def _flush_impl(self) -> None:
        self._session.flush()

    def _close_impl(self) -> None:
        self._session.close()


def _create_configuration(uow: FakeTechnicalConfigurationUnitOfWork) -> UUID:
    create_use_case = CreateTechnicalConfigurationUseCase(unit_of_work=uow)
    response = create_use_case.execute(CreateTechnicalConfigurationRequest(vessel_id=uuid4()))
    return response.configuration.id


def _add_planned_component(
    uow: FakeTechnicalConfigurationUnitOfWork,
    configuration_id: UUID,
    *,
    name: str,
    component_type: TechnicalComponentType,
    component_id: UUID | None = None,
) -> UUID:
    add_use_case = AddTechnicalComponentUseCase(unit_of_work=uow)
    response = add_use_case.execute(
        AddTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            component_type=component_type,
            name=name,
            status=TechnicalComponentStatus.PLANNED,
            specification_schema_key="GENERIC_V1",
            specification_entries=(
                SpecificationEntryInput(key="k", value=1),
            ),
        )
    )

    added = next(component for component in response.configuration.components if component.name == name)
    return added.id


def test_create_technical_configuration() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    use_case = CreateTechnicalConfigurationUseCase(unit_of_work=uow)
    vessel_id = uuid4()

    response = use_case.execute(CreateTechnicalConfigurationRequest(vessel_id=vessel_id))

    assert response.configuration.vessel_id == vessel_id
    assert uow.commits == 1
    assert response.configuration.id in uow.configurations


def test_invalid_vessel_id() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    use_case = CreateTechnicalConfigurationUseCase(unit_of_work=uow)

    with pytest.raises(ValidationException):
        use_case.execute(CreateTechnicalConfigurationRequest(vessel_id="x"))  # type: ignore[arg-type]


def test_duplicate_vessel_configuration() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    use_case = CreateTechnicalConfigurationUseCase(unit_of_work=uow)
    vessel_id = uuid4()

    use_case.execute(CreateTechnicalConfigurationRequest(vessel_id=vessel_id))

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(CreateTechnicalConfigurationRequest(vessel_id=vessel_id))


def test_add_component() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)

    add_use_case = AddTechnicalComponentUseCase(unit_of_work=uow)
    response = add_use_case.execute(
        AddTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_type=TechnicalComponentType.PROPULSION_ENGINE,
            name="Engine",
            manufacturer="Maker",
            model="X1",
            serial_number="ENG-1",
            status=TechnicalComponentStatus.PLANNED,
            specification_schema_key="ENGINE_V1",
            specification_entries=(
                SpecificationEntryInput(key="power_kw", value=2400, unit="kW"),
            ),
        )
    )

    assert any(component.name == "Engine" for component in response.configuration.components)


def test_duplicate_component() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)
    duplicate_id = uuid4()

    _ = _add_planned_component(
        uow,
        configuration_id,
        name="Component A",
        component_type=TechnicalComponentType.OTHER,
        component_id=duplicate_id,
    )

    add_use_case = AddTechnicalComponentUseCase(unit_of_work=uow)
    with pytest.raises(BusinessRuleViolation):
        add_use_case.execute(
            AddTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=duplicate_id,
                component_type=TechnicalComponentType.OTHER,
                name="Component B",
            )
        )


def test_install_component() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)
    component_id = _add_planned_component(
        uow,
        configuration_id,
        name="Installable",
        component_type=TechnicalComponentType.PUMP,
    )

    install_use_case = InstallTechnicalComponentUseCase(unit_of_work=uow)
    response = install_use_case.execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 1, 1),
        )
    )

    installed = next(component for component in response.configuration.components if component.id == component_id)
    assert installed.status == "INSTALLED"
    assert installed.installed_date == date(2025, 1, 1)


def test_remove_component() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)
    component_id = _add_planned_component(
        uow,
        configuration_id,
        name="Removable",
        component_type=TechnicalComponentType.PUMP,
    )

    InstallTechnicalComponentUseCase(unit_of_work=uow).execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 1, 1),
        )
    )

    remove_use_case = RemoveTechnicalComponentUseCase(unit_of_work=uow)
    response = remove_use_case.execute(
        RemoveTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            removed_on=date(2025, 3, 1),
        )
    )

    removed = next(component for component in response.configuration.components if component.id == component_id)
    assert removed.status == "REMOVED"
    assert removed.removed_date == date(2025, 3, 1)


def test_replace_component() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)
    component_a_id = _add_planned_component(
        uow,
        configuration_id,
        name="Component A",
        component_type=TechnicalComponentType.GEARBOX,
    )
    InstallTechnicalComponentUseCase(unit_of_work=uow).execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_a_id,
            installed_on=date(2024, 1, 1),
        )
    )

    replace_use_case = ReplaceTechnicalComponentUseCase(unit_of_work=uow)
    response = replace_use_case.execute(
        ReplaceTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_a_id,
            replaced_on=date(2025, 1, 1),
            reason="Wear",
            replacement_component_type=TechnicalComponentType.GEARBOX,
            replacement_name="Component B",
            replacement_serial_number="GB-2",
        )
    )

    names = [component.name for component in response.configuration.components]
    assert "Component A" in names
    assert "Component B" in names

    a = next(component for component in response.configuration.components if component.name == "Component A")
    b = next(component for component in response.configuration.components if component.name == "Component B")
    assert a.status == "REMOVED"
    assert b.status == "INSTALLED"
    assert len(response.configuration.replacement_history) == 1


def test_update_component_details() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)
    component_id = _add_planned_component(
        uow,
        configuration_id,
        name="Updatable",
        component_type=TechnicalComponentType.GENERATOR,
    )

    update_use_case = UpdateTechnicalComponentDetailsUseCase(unit_of_work=uow)
    response = update_use_case.execute(
        UpdateTechnicalComponentDetailsRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            manufacturer="Updated Maker",
            model="Z-9",
            specification_schema_key="GENERATOR_V1",
            specification_entries=(
                SpecificationEntryInput(key="rating_kw", value=450, unit="kW"),
            ),
        )
    )

    component = next(
        candidate
        for candidate in response.configuration.components
        if candidate.id == component_id
    )
    assert component.manufacturer == "Updated Maker"
    assert component.model == "Z-9"
    assert component.specification_schema_key == "GENERATOR_V1"


def test_configuration_not_found() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    use_case = AddTechnicalComponentUseCase(unit_of_work=uow)

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            AddTechnicalComponentRequest(
                configuration_id=uuid4(),
                component_type=TechnicalComponentType.OTHER,
                name="Missing",
            )
        )


def test_component_not_found() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)

    use_case = InstallTechnicalComponentUseCase(unit_of_work=uow)
    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            InstallTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=uuid4(),
                installed_on=date(2025, 1, 1),
            )
        )


def test_invalid_lifecycle_transition() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)
    component_id = _add_planned_component(
        uow,
        configuration_id,
        name="Already installed",
        component_type=TechnicalComponentType.OTHER,
    )

    install_use_case = InstallTechnicalComponentUseCase(unit_of_work=uow)
    install_use_case.execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 1, 1),
        )
    )

    with pytest.raises(BusinessRuleViolation):
        install_use_case.execute(
            InstallTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=component_id,
                installed_on=date(2025, 1, 2),
            )
        )


def test_invalid_chronology() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)
    component_id = _add_planned_component(
        uow,
        configuration_id,
        name="Chronology",
        component_type=TechnicalComponentType.OTHER,
    )

    InstallTechnicalComponentUseCase(unit_of_work=uow).execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 2, 1),
        )
    )

    remove_use_case = RemoveTechnicalComponentUseCase(unit_of_work=uow)
    with pytest.raises(BusinessRuleViolation):
        remove_use_case.execute(
            RemoveTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=component_id,
                removed_on=date(2025, 1, 1),
            )
        )


def test_invalid_replacement() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)
    component_id = _add_planned_component(
        uow,
        configuration_id,
        name="Replaceable",
        component_type=TechnicalComponentType.GEARBOX,
    )

    InstallTechnicalComponentUseCase(unit_of_work=uow).execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 1, 1),
        )
    )

    replace_use_case = ReplaceTechnicalComponentUseCase(unit_of_work=uow)
    replace_use_case.execute(
        ReplaceTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            replaced_on=date(2025, 2, 1),
            reason="Wear",
            replacement_component_type=TechnicalComponentType.GEARBOX,
            replacement_name="Replacement 1",
        )
    )

    with pytest.raises(BusinessRuleViolation):
        replace_use_case.execute(
            ReplaceTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=component_id,
                replaced_on=date(2025, 3, 1),
                reason="Invalid second replace",
                replacement_component_type=TechnicalComponentType.GEARBOX,
                replacement_name="Replacement 2",
            )
        )


def test_repository_add_update_interaction() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)

    _ = _add_planned_component(
        uow,
        configuration_id,
        name="Interaction",
        component_type=TechnicalComponentType.OTHER,
    )

    assert uow.last_repository is not None
    assert uow.last_repository.get_by_id_calls >= 1
    assert uow.last_repository.update_calls >= 1


def test_unit_of_work_commit() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    use_case = CreateTechnicalConfigurationUseCase(unit_of_work=uow)

    use_case.execute(CreateTechnicalConfigurationRequest(vessel_id=uuid4()))

    assert uow.commits == 1


def test_unit_of_work_rollback() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork(fail_add=True)
    use_case = CreateTechnicalConfigurationUseCase(unit_of_work=uow)

    with pytest.raises(RepositoryException):
        use_case.execute(CreateTechnicalConfigurationRequest(vessel_id=uuid4()))

    assert uow.commits == 0
    assert uow.rollbacks == 1


def test_immutable_request_and_response_dto() -> None:
    request = CreateTechnicalConfigurationRequest(vessel_id=uuid4())
    response = CreateTechnicalConfigurationResponse(
        configuration=CreateTechnicalConfigurationUseCase(
            unit_of_work=FakeTechnicalConfigurationUnitOfWork()
        ).execute(CreateTechnicalConfigurationRequest(vessel_id=uuid4())).configuration
    )

    with pytest.raises(FrozenInstanceError):
        request.vessel_id = uuid4()  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        response.configuration = response.configuration  # type: ignore[misc]


def test_response_mapping_no_domain_object_leakage() -> None:
    uow = FakeTechnicalConfigurationUnitOfWork()
    configuration_id = _create_configuration(uow)
    component_id = _add_planned_component(
        uow,
        configuration_id,
        name="Mapped",
        component_type=TechnicalComponentType.PUMP,
    )

    response = InstallTechnicalComponentUseCase(unit_of_work=uow).execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 1, 1),
        )
    )

    assert not isinstance(response.configuration, TechnicalConfiguration)
    for component in response.configuration.components:
        assert not isinstance(component, TechnicalComponent)
        assert isinstance(component.component_type, str)
        assert isinstance(component.status, str)


def test_historical_configuration_application_scenario_reload() -> None:
    engine, write_session = _create_sqlite_session()
    read_session: Session | None = None
    try:
        write_uow = SQLiteTechnicalConfigurationApplicationUnitOfWork(write_session)

        create_response = CreateTechnicalConfigurationUseCase(unit_of_work=write_uow).execute(
            CreateTechnicalConfigurationRequest(vessel_id=uuid4())
        )
        configuration_id = create_response.configuration.id

        add_use_case = AddTechnicalComponentUseCase(unit_of_work=write_uow)
        add_a = add_use_case.execute(
            AddTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_type=TechnicalComponentType.GEARBOX,
                name="Component A",
            )
        )
        component_a_id = next(
            component.id for component in add_a.configuration.components if component.name == "Component A"
        )

        InstallTechnicalComponentUseCase(unit_of_work=write_uow).execute(
            InstallTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=component_a_id,
                installed_on=date(2025, 1, 1),
            )
        )

        ReplaceTechnicalComponentUseCase(unit_of_work=write_uow).execute(
            ReplaceTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=component_a_id,
                replaced_on=date(2025, 4, 1),
                reason="Wear",
                replacement_component_type=TechnicalComponentType.GEARBOX,
                replacement_name="Component B",
            )
        )
        write_session.close()

        read_session = Session(engine)
        read_uow = SQLiteTechnicalConfigurationApplicationUnitOfWork(read_session)

        loaded = GetTechnicalConfigurationUseCase(unit_of_work=read_uow).execute(
            GetTechnicalConfigurationRequest(configuration_id=configuration_id)
        )

        assert any(component.name == "Component A" for component in loaded.configuration.components)
        assert any(component.name == "Component B" for component in loaded.configuration.components)

        component_a = next(
            component
            for component in loaded.configuration.components
            if component.name == "Component A"
        )
        component_b = next(
            component
            for component in loaded.configuration.components
            if component.name == "Component B"
        )

        assert component_a.status == "REMOVED"
        assert component_a.removed_date == date(2025, 4, 1)
        assert component_b.status == "INSTALLED"
        assert len(loaded.configuration.replacement_history) == 1
    finally:
        write_session.close()
        if read_session is not None:
            read_session.close()
        engine.dispose()


def test_propulsion_chain_application_scenario_reload() -> None:
    engine, write_session = _create_sqlite_session()
    read_session: Session | None = None
    try:
        write_uow = SQLiteTechnicalConfigurationApplicationUnitOfWork(write_session)

        create_response = CreateTechnicalConfigurationUseCase(unit_of_work=write_uow).execute(
            CreateTechnicalConfigurationRequest(vessel_id=uuid4())
        )
        configuration_id = create_response.configuration.id

        add_use_case = AddTechnicalComponentUseCase(unit_of_work=write_uow)
        install_use_case = InstallTechnicalComponentUseCase(unit_of_work=write_uow)

        components = [
            ("Propulsion Engine", TechnicalComponentType.PROPULSION_ENGINE),
            ("Gear Arrangement", TechnicalComponentType.GEARBOX),
            ("Shaft", TechnicalComponentType.SHAFT),
            ("Controllable Pitch Propeller", TechnicalComponentType.PROPELLER),
        ]

        for name, component_type in components:
            add_response = add_use_case.execute(
                AddTechnicalComponentRequest(
                    configuration_id=configuration_id,
                    component_type=component_type,
                    name=name,
                )
            )
            component_id = next(
                component.id
                for component in add_response.configuration.components
                if component.name == name
            )

            install_use_case.execute(
                InstallTechnicalComponentRequest(
                    configuration_id=configuration_id,
                    component_id=component_id,
                    installed_on=date(2025, 1, 1),
                )
            )

        write_session.close()

        read_session = Session(engine)
        read_uow = SQLiteTechnicalConfigurationApplicationUnitOfWork(read_session)

        loaded = GetTechnicalConfigurationUseCase(unit_of_work=read_uow).execute(
            GetTechnicalConfigurationRequest(configuration_id=configuration_id)
        )

        names = [component.name for component in loaded.configuration.components]
        statuses = {component.name: component.status for component in loaded.configuration.components}

        assert "Propulsion Engine" in names
        assert "Gear Arrangement" in names
        assert "Shaft" in names
        assert "Controllable Pitch Propeller" in names
        assert statuses["Propulsion Engine"] == "INSTALLED"
        assert statuses["Gear Arrangement"] == "INSTALLED"
        assert statuses["Shaft"] == "INSTALLED"
        assert statuses["Controllable Pitch Propeller"] == "INSTALLED"
    finally:
        write_session.close()
        if read_session is not None:
            read_session.close()
        engine.dispose()

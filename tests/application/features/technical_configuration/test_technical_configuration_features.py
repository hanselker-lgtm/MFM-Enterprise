from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.application.features.technical_configuration.add_technical_component_feature import (
    AddTechnicalComponentFeature,
)
from mfm.application.features.technical_configuration.add_technical_component_feature import (
    AddTechnicalComponentRequest,
)
from mfm.application.features.technical_configuration.add_technical_component_feature import (
    AddTechnicalComponentResponse,
)
from mfm.application.features.technical_configuration.add_technical_component_feature import (
    ValidationException as AddValidationException,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    BusinessRuleViolation as FeatureBusinessRuleViolation,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    ComponentReplacementRecordResponse,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    CreateTechnicalConfigurationFeature,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    CreateTechnicalConfigurationRequest,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    CreateTechnicalConfigurationResponse,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    RepositoryException as FeatureRepositoryException,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    TechnicalComponentResponse,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    TechnicalConfigurationResponse,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    TechnicalSpecificationEntryResponse,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    ValidationException as FeatureValidationException,
)
from mfm.application.features.technical_configuration.install_technical_component_feature import (
    InstallTechnicalComponentFeature,
)
from mfm.application.features.technical_configuration.install_technical_component_feature import (
    InstallTechnicalComponentRequest,
)
from mfm.application.features.technical_configuration.remove_technical_component_feature import (
    RemoveTechnicalComponentFeature,
)
from mfm.application.features.technical_configuration.remove_technical_component_feature import (
    RemoveTechnicalComponentRequest,
)
from mfm.application.features.technical_configuration.replace_technical_component_feature import (
    ReplaceTechnicalComponentFeature,
)
from mfm.application.features.technical_configuration.replace_technical_component_feature import (
    ReplaceTechnicalComponentRequest,
)
from mfm.application.features.technical_configuration.update_technical_component_details_feature import (
    UpdateTechnicalComponentDetailsFeature,
)
from mfm.application.features.technical_configuration.update_technical_component_details_feature import (
    UpdateTechnicalComponentDetailsRequest,
)
from mfm.application.technical_configuration.add_technical_component import (
    AddTechnicalComponentResponse as ServiceAddResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    CreateTechnicalConfigurationResponse as ServiceCreateResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    ValidationException as ServiceValidationException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    CreateTechnicalConfigurationUseCase,
)
from mfm.application.technical_configuration.add_technical_component import (
    AddTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.install_technical_component import (
    InstallTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.remove_technical_component import (
    RemoveTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.replace_technical_component import (
    ReplaceTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.update_technical_component_details import (
    UpdateTechnicalComponentDetailsUseCase,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.domain.technical_configuration.technical_component import TechnicalComponent
from mfm.domain.technical_configuration.technical_configuration import TechnicalConfiguration
from mfm.infrastructure.persistence.sqlite.sqlite_technical_configuration_repository import (
    SQLiteTechnicalConfigurationRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error
        self.last_request = None

    def execute(self, request):
        self.last_request = request
        if self._error is not None:
            raise self._error
        return self._response


def _sample_configuration_response(
    *,
    configuration_id: UUID | None = None,
    vessel_id: UUID | None = None,
) -> TechnicalConfigurationResponse:
    comp_a_id = uuid4()
    comp_b_id = uuid4()
    replaced_on = date(2025, 5, 1)

    return TechnicalConfigurationResponse(
        id=configuration_id or uuid4(),
        vessel_id=vessel_id or uuid4(),
        status="ACTIVE",
        components=(
            TechnicalComponentResponse(
                id=comp_a_id,
                component_type="GEARBOX",
                name="Component A",
                manufacturer=None,
                model=None,
                serial_number="GB-001",
                build_year=2020,
                status="REMOVED",
                installed_date=date(2024, 1, 1),
                removed_date=replaced_on,
                notes=None,
                specification_schema_key="GEARBOX_V1",
                specification_entries=(
                    TechnicalSpecificationEntryResponse(key="ratio", value=4.0, unit=None),
                ),
                replacement_successor_id=comp_b_id,
            ),
            TechnicalComponentResponse(
                id=comp_b_id,
                component_type="GEARBOX",
                name="Component B",
                manufacturer=None,
                model=None,
                serial_number="GB-002",
                build_year=2024,
                status="INSTALLED",
                installed_date=replaced_on,
                removed_date=None,
                notes=None,
                specification_schema_key="GEARBOX_V1",
                specification_entries=(
                    TechnicalSpecificationEntryResponse(key="ratio", value=4.2, unit=None),
                ),
                replacement_successor_id=None,
            ),
        ),
        replacement_history=(
            ComponentReplacementRecordResponse(
                id=uuid4(),
                replaced_component_id=comp_a_id,
                replacement_component_id=comp_b_id,
                replaced_on=replaced_on,
                reason="Wear",
                notes=None,
            ),
        ),
    )


def test_create_configuration_feature_happy_path() -> None:
    sample = _sample_configuration_response()
    feature = CreateTechnicalConfigurationFeature(
        service=StubService(response=ServiceCreateResponse(configuration=sample))
    )

    response = feature.execute(CreateTechnicalConfigurationRequest(vessel_id=sample.vessel_id))

    assert isinstance(response, CreateTechnicalConfigurationResponse)
    assert response.configuration.id == sample.id
    assert response.configuration.vessel_id == sample.vessel_id


def test_add_component_feature_happy_path_and_component_type_mapping() -> None:
    sample = _sample_configuration_response()
    service = StubService(response=ServiceAddResponse(configuration=sample))
    feature = AddTechnicalComponentFeature(service=service)

    response = feature.execute(
        AddTechnicalComponentRequest(
            configuration_id=sample.id,
            component_type="propulsion_engine",
            name="Engine",
            status="planned",
        )
    )

    assert isinstance(response, AddTechnicalComponentResponse)
    assert service.last_request.component_type.value == "PROPULSION_ENGINE"
    assert service.last_request.status.value == "PLANNED"


def test_install_component_feature_happy_path() -> None:
    sample = _sample_configuration_response()
    feature = InstallTechnicalComponentFeature(
        service=StubService(
            response=type("R", (), {"configuration": sample})()
        )
    )

    response = feature.execute(
        InstallTechnicalComponentRequest(
            configuration_id=sample.id,
            component_id=sample.components[1].id,
            installed_on=date(2025, 1, 1),
        )
    )

    assert response.configuration.id == sample.id


def test_remove_component_feature_happy_path() -> None:
    sample = _sample_configuration_response()
    feature = RemoveTechnicalComponentFeature(
        service=StubService(
            response=type("R", (), {"configuration": sample})()
        )
    )

    response = feature.execute(
        RemoveTechnicalComponentRequest(
            configuration_id=sample.id,
            component_id=sample.components[0].id,
            removed_on=date(2025, 1, 1),
        )
    )

    assert any(component.status == "REMOVED" for component in response.configuration.components)


def test_replace_component_feature_happy_path() -> None:
    sample = _sample_configuration_response()
    feature = ReplaceTechnicalComponentFeature(
        service=StubService(
            response=type("R", (), {"configuration": sample})()
        )
    )

    response = feature.execute(
        ReplaceTechnicalComponentRequest(
            configuration_id=sample.id,
            component_id=sample.components[0].id,
            replaced_on=date(2025, 5, 1),
            reason="Wear",
            replacement_component_type="GEARBOX",
            replacement_name="Component B",
        )
    )

    assert any(component.name == "Component A" for component in response.configuration.components)
    assert any(component.name == "Component B" for component in response.configuration.components)


def test_update_component_details_feature_happy_path() -> None:
    sample = _sample_configuration_response()
    feature = UpdateTechnicalComponentDetailsFeature(
        service=StubService(
            response=type("R", (), {"configuration": sample})()
        )
    )

    response = feature.execute(
        UpdateTechnicalComponentDetailsRequest(
            configuration_id=sample.id,
            component_id=sample.components[1].id,
            manufacturer="Updated Maker",
        )
    )

    assert response.configuration.id == sample.id


def test_request_validation_mapping() -> None:
    feature = CreateTechnicalConfigurationFeature(service=StubService(response=None))

    with pytest.raises(FeatureValidationException):
        feature.execute(CreateTechnicalConfigurationRequest(vessel_id="x"))  # type: ignore[arg-type]


def test_duplicate_configuration_mapping() -> None:
    feature = CreateTechnicalConfigurationFeature(
        service=StubService(error=ServiceBusinessRuleViolation("already exists"))
    )

    with pytest.raises(FeatureBusinessRuleViolation):
        feature.execute(CreateTechnicalConfigurationRequest(vessel_id=uuid4()))


def test_duplicate_component_mapping() -> None:
    feature = AddTechnicalComponentFeature(
        service=StubService(error=ServiceBusinessRuleViolation("component already exists"))
    )

    with pytest.raises(FeatureBusinessRuleViolation):
        feature.execute(
            AddTechnicalComponentRequest(
                configuration_id=uuid4(),
                component_type="OTHER",
                name="X",
            )
        )


def test_component_not_found_mapping() -> None:
    feature = InstallTechnicalComponentFeature(
        service=StubService(error=ServiceBusinessRuleViolation("component not found"))
    )

    with pytest.raises(FeatureBusinessRuleViolation):
        feature.execute(
            InstallTechnicalComponentRequest(
                configuration_id=uuid4(),
                component_id=uuid4(),
                installed_on=date(2025, 1, 1),
            )
        )


def test_invalid_lifecycle_mapping() -> None:
    feature = RemoveTechnicalComponentFeature(
        service=StubService(error=ServiceBusinessRuleViolation("invalid lifecycle"))
    )

    with pytest.raises(FeatureBusinessRuleViolation):
        feature.execute(
            RemoveTechnicalComponentRequest(
                configuration_id=uuid4(),
                component_id=uuid4(),
                removed_on=date(2025, 1, 1),
            )
        )


def test_invalid_chronology_mapping() -> None:
    feature = RemoveTechnicalComponentFeature(
        service=StubService(error=ServiceBusinessRuleViolation("invalid chronology"))
    )

    with pytest.raises(FeatureBusinessRuleViolation):
        feature.execute(
            RemoveTechnicalComponentRequest(
                configuration_id=uuid4(),
                component_id=uuid4(),
                removed_on=date(2024, 1, 1),
            )
        )


def test_invalid_replacement_mapping() -> None:
    feature = ReplaceTechnicalComponentFeature(
        service=StubService(error=ServiceBusinessRuleViolation("invalid replacement"))
    )

    with pytest.raises(FeatureBusinessRuleViolation):
        feature.execute(
            ReplaceTechnicalComponentRequest(
                configuration_id=uuid4(),
                component_id=uuid4(),
                replaced_on=date(2025, 1, 1),
                reason="X",
                replacement_component_type="GEARBOX",
                replacement_name="Y",
            )
        )


def test_invalid_component_type_mapping() -> None:
    feature = AddTechnicalComponentFeature(service=StubService(response=None))

    with pytest.raises(AddValidationException):
        feature.execute(
            AddTechnicalComponentRequest(
                configuration_id=uuid4(),
                component_type="NOT_A_TYPE",
                name="X",
            )
        )


def test_application_service_exception_mapping() -> None:
    sample = _sample_configuration_response()

    validation_feature = CreateTechnicalConfigurationFeature(
        service=StubService(error=ServiceValidationException("bad request"))
    )
    with pytest.raises(FeatureValidationException):
        validation_feature.execute(CreateTechnicalConfigurationRequest(vessel_id=uuid4()))

    repository_feature = CreateTechnicalConfigurationFeature(
        service=StubService(error=ServiceRepositoryException("db issue"))
    )
    with pytest.raises(FeatureRepositoryException):
        repository_feature.execute(CreateTechnicalConfigurationRequest(vessel_id=uuid4()))

    unknown_feature = AddTechnicalComponentFeature(service=StubService(error=RuntimeError("boom")))
    with pytest.raises(FeatureRepositoryException):
        unknown_feature.execute(
            AddTechnicalComponentRequest(
                configuration_id=sample.id,
                component_type="OTHER",
                name="X",
            )
        )


def test_response_mapping_and_public_primitives() -> None:
    sample = _sample_configuration_response()
    feature = CreateTechnicalConfigurationFeature(
        service=StubService(response=ServiceCreateResponse(configuration=sample))
    )

    response = feature.execute(CreateTechnicalConfigurationRequest(vessel_id=sample.vessel_id))

    assert isinstance(response.configuration.id, UUID)
    assert isinstance(response.configuration.vessel_id, UUID)
    for component in response.configuration.components:
        assert isinstance(component.component_type, str)
        assert isinstance(component.status, str)


def test_immutable_public_dto_behavior() -> None:
    sample = _sample_configuration_response()
    response = CreateTechnicalConfigurationResponse(configuration=sample)

    with pytest.raises(FrozenInstanceError):
        response.configuration = sample  # type: ignore[misc]


def test_no_domain_object_leakage() -> None:
    sample = _sample_configuration_response()
    feature = CreateTechnicalConfigurationFeature(
        service=StubService(response=ServiceCreateResponse(configuration=sample))
    )

    response = feature.execute(CreateTechnicalConfigurationRequest(vessel_id=sample.vessel_id))

    assert not isinstance(response.configuration, TechnicalConfiguration)
    for component in response.configuration.components:
        assert not isinstance(component, TechnicalComponent)


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


def test_historical_replacement_feature_scenario() -> None:
    engine, write_session = _create_sqlite_session()
    uow = SQLiteTechnicalConfigurationApplicationUnitOfWork(write_session)

    create_feature = CreateTechnicalConfigurationFeature(
        service=CreateTechnicalConfigurationUseCase(unit_of_work=uow)
    )
    add_feature = AddTechnicalComponentFeature(service=AddTechnicalComponentUseCase(unit_of_work=uow))
    install_feature = InstallTechnicalComponentFeature(
        service=InstallTechnicalComponentUseCase(unit_of_work=uow)
    )
    replace_feature = ReplaceTechnicalComponentFeature(
        service=ReplaceTechnicalComponentUseCase(unit_of_work=uow)
    )

    created = create_feature.execute(CreateTechnicalConfigurationRequest(vessel_id=uuid4()))
    configuration_id = created.configuration.id

    add_a = add_feature.execute(
        AddTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_type="GEARBOX",
            name="Component A",
        )
    )

    component_a_id = next(
        component.id
        for component in add_a.configuration.components
        if component.name == "Component A"
    )

    install_feature.execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_a_id,
            installed_on=date(2025, 1, 1),
        )
    )

    replaced = replace_feature.execute(
        ReplaceTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_a_id,
            replaced_on=date(2025, 4, 1),
            reason="Wear",
            replacement_component_type="GEARBOX",
            replacement_name="Component B",
        )
    )

    assert any(component.name == "Component A" for component in replaced.configuration.components)
    assert any(component.name == "Component B" for component in replaced.configuration.components)

    component_a = next(
        component
        for component in replaced.configuration.components
        if component.name == "Component A"
    )
    component_b = next(
        component
        for component in replaced.configuration.components
        if component.name == "Component B"
    )

    assert component_a.status == "REMOVED"
    assert component_b.status == "INSTALLED"
    assert len(replaced.configuration.replacement_history) == 1

    write_session.close()


def test_propulsion_chain_feature_scenario() -> None:
    engine, write_session = _create_sqlite_session()
    uow = SQLiteTechnicalConfigurationApplicationUnitOfWork(write_session)

    create_feature = CreateTechnicalConfigurationFeature(
        service=CreateTechnicalConfigurationUseCase(unit_of_work=uow)
    )
    add_feature = AddTechnicalComponentFeature(service=AddTechnicalComponentUseCase(unit_of_work=uow))
    install_feature = InstallTechnicalComponentFeature(
        service=InstallTechnicalComponentUseCase(unit_of_work=uow)
    )

    created = create_feature.execute(CreateTechnicalConfigurationRequest(vessel_id=uuid4()))
    configuration_id = created.configuration.id

    flow = [
        ("Propulsion Engine", "PROPULSION_ENGINE"),
        ("Gear Arrangement", "GEARBOX"),
        ("Shaft", "SHAFT"),
        ("Controllable Pitch Propeller", "PROPELLER"),
    ]

    for name, component_type in flow:
        add_response = add_feature.execute(
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

        install_response = install_feature.execute(
            InstallTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=component_id,
                installed_on=date(2025, 1, 1),
            )
        )

    names = [component.name for component in install_response.configuration.components]
    statuses = {component.name: component.status for component in install_response.configuration.components}

    assert "Propulsion Engine" in names
    assert "Gear Arrangement" in names
    assert "Shaft" in names
    assert "Controllable Pitch Propeller" in names
    assert statuses["Propulsion Engine"] == "INSTALLED"
    assert statuses["Gear Arrangement"] == "INSTALLED"
    assert statuses["Shaft"] == "INSTALLED"
    assert statuses["Controllable Pitch Propeller"] == "INSTALLED"

    write_session.close()

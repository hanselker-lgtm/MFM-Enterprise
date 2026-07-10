from __future__ import annotations

from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.organization.assign_role_feature import AssignRoleFeature
from mfm.application.features.organization.assign_role_feature import AssignRoleRequest
from mfm.application.features.organization.assign_role_feature import AssignRoleResponse
from mfm.application.features.organization.assign_role_feature import BusinessRuleViolation as AssignRoleBusinessRuleViolation
from mfm.application.features.organization.assign_role_feature import RepositoryException as AssignRoleRepositoryException
from mfm.application.features.organization.assign_role_feature import ValidationException as AssignRoleValidationException
from mfm.application.features.organization.create_board_feature import BoardMemberInput
from mfm.application.features.organization.create_board_feature import CreateBoardFeature
from mfm.application.features.organization.create_board_feature import CreateBoardRequest
from mfm.application.features.organization.create_board_feature import CreateBoardResponse
from mfm.application.features.organization.create_board_feature import BusinessRuleViolation as CreateBoardBusinessRuleViolation
from mfm.application.features.organization.create_board_feature import RepositoryException as CreateBoardRepositoryException
from mfm.application.features.organization.create_board_feature import ValidationException as CreateBoardValidationException
from mfm.application.features.organization.create_committee_feature import CommitteeMemberInput
from mfm.application.features.organization.create_committee_feature import CreateCommitteeFeature
from mfm.application.features.organization.create_committee_feature import CreateCommitteeRequest
from mfm.application.features.organization.create_committee_feature import CreateCommitteeResponse
from mfm.application.features.organization.create_committee_feature import BusinessRuleViolation as CreateCommitteeBusinessRuleViolation
from mfm.application.features.organization.create_committee_feature import RepositoryException as CreateCommitteeRepositoryException
from mfm.application.features.organization.create_committee_feature import ValidationException as CreateCommitteeValidationException
from mfm.application.features.organization.create_organization_feature import CreateOrganizationFeature
from mfm.application.features.organization.create_organization_feature import CreateOrganizationRequest
from mfm.application.features.organization.create_organization_feature import CreateOrganizationResponse
from mfm.application.features.organization.create_organization_feature import BusinessRuleViolation as CreateOrganizationBusinessRuleViolation
from mfm.application.features.organization.create_organization_feature import RepositoryException as CreateOrganizationRepositoryException
from mfm.application.features.organization.create_organization_feature import ValidationException as CreateOrganizationValidationException
from mfm.application.features.organization.register_volunteer_feature import RegisterVolunteerFeature
from mfm.application.features.organization.register_volunteer_feature import RegisterVolunteerRequest
from mfm.application.features.organization.register_volunteer_feature import RegisterVolunteerResponse
from mfm.application.features.organization.register_volunteer_feature import VolunteerCertificateInput
from mfm.application.features.organization.register_volunteer_feature import BusinessRuleViolation as RegisterVolunteerBusinessRuleViolation
from mfm.application.features.organization.register_volunteer_feature import RepositoryException as RegisterVolunteerRepositoryException
from mfm.application.features.organization.register_volunteer_feature import ValidationException as RegisterVolunteerValidationException
from mfm.application.features.organization.update_organization_feature import UpdateOrganizationFeature
from mfm.application.features.organization.update_organization_feature import UpdateOrganizationRequest
from mfm.application.features.organization.update_organization_feature import UpdateOrganizationResponse
from mfm.application.features.organization.update_organization_feature import BusinessRuleViolation as UpdateOrganizationBusinessRuleViolation
from mfm.application.features.organization.update_organization_feature import RepositoryException as UpdateOrganizationRepositoryException
from mfm.application.features.organization.update_organization_feature import ValidationException as UpdateOrganizationValidationException
from mfm.application.organization.assign_role import AssignRoleResponse as ServiceAssignRoleResponse
from mfm.application.organization.create_board import CreateBoardResponse as ServiceCreateBoardResponse
from mfm.application.organization.create_committee import CreateCommitteeResponse as ServiceCreateCommitteeResponse
from mfm.application.organization.create_organization import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.organization.create_organization import CreateOrganizationResponse as ServiceCreateOrganizationResponse
from mfm.application.organization.create_organization import RepositoryException as ServiceRepositoryException
from mfm.application.organization.create_organization import ValidationException as ServiceValidationException
from mfm.application.organization.register_volunteer import RegisterVolunteerResponse as ServiceRegisterVolunteerResponse
from mfm.application.organization.update_organization import UpdateOrganizationResponse as ServiceUpdateOrganizationResponse
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType


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


def test_create_organization_feature_happy_path_and_response_mapping() -> None:
    organization_id = uuid4()
    service = StubService(
        response=ServiceCreateOrganizationResponse(
            organization_id=organization_id,
            organization_number="ORG-FEAT-001",
            name="Feature Org",
        )
    )
    feature = CreateOrganizationFeature(service=service)

    response = feature.execute(
        CreateOrganizationRequest(
            organization_number="ORG-FEAT-001",
            name="Feature Org",
            organization_type=OrganizationType.ASSOCIATION,
        )
    )

    assert isinstance(response, CreateOrganizationResponse)
    assert isinstance(response.organization_id, UUID)
    assert response.organization_number == "ORG-FEAT-001"
    assert response.name == "Feature Org"
    assert service.last_request.organization_type is OrganizationType.ASSOCIATION


def test_create_organization_feature_validation_duplicate_rollback_exception_mapping() -> None:
    feature = CreateOrganizationFeature(service=StubService(response=None))

    with pytest.raises(CreateOrganizationValidationException):
        feature.execute(
            CreateOrganizationRequest(
                organization_number="",
                name="X",
                organization_type=OrganizationType.ASSOCIATION,
            )
        )

    duplicate_feature = CreateOrganizationFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate"))
    )
    with pytest.raises(CreateOrganizationBusinessRuleViolation):
        duplicate_feature.execute(
            CreateOrganizationRequest(
                organization_number="ORG-FEAT-002",
                name="X",
                organization_type=OrganizationType.ASSOCIATION,
            )
        )

    rollback_feature = CreateOrganizationFeature(
        service=StubService(error=ServiceRepositoryException("rollback"))
    )
    with pytest.raises(CreateOrganizationRepositoryException):
        rollback_feature.execute(
            CreateOrganizationRequest(
                organization_number="ORG-FEAT-003",
                name="X",
                organization_type=OrganizationType.ASSOCIATION,
            )
        )

    unknown_feature = CreateOrganizationFeature(service=StubService(error=RuntimeError("boom")))
    with pytest.raises(CreateOrganizationRepositoryException):
        unknown_feature.execute(
            CreateOrganizationRequest(
                organization_number="ORG-FEAT-004",
                name="X",
                organization_type=OrganizationType.ASSOCIATION,
            )
        )


def test_update_organization_feature_happy_path_and_response_mapping() -> None:
    organization_id = uuid4()
    service = StubService(
        response=ServiceUpdateOrganizationResponse(
            organization_id=organization_id,
            organization_number="ORG-FEAT-010",
            name="Updated Org",
            status=OrganizationStatus.INACTIVE,
        )
    )
    feature = UpdateOrganizationFeature(service=service)

    response = feature.execute(
        UpdateOrganizationRequest(
            organization_id=organization_id,
            name="Updated Org",
            status=OrganizationStatus.INACTIVE,
        )
    )

    assert isinstance(response, UpdateOrganizationResponse)
    assert response.organization_id == organization_id
    assert response.status == "INACTIVE"


def test_update_organization_feature_validation_duplicate_rollback_exception_mapping() -> None:
    feature = UpdateOrganizationFeature(service=StubService(response=None))

    with pytest.raises(UpdateOrganizationValidationException):
        feature.execute(UpdateOrganizationRequest(organization_id=uuid4(), name="   "))

    duplicate_feature = UpdateOrganizationFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate"))
    )
    with pytest.raises(UpdateOrganizationBusinessRuleViolation):
        duplicate_feature.execute(UpdateOrganizationRequest(organization_id=uuid4(), name="X"))

    rollback_feature = UpdateOrganizationFeature(
        service=StubService(error=ServiceRepositoryException("rollback"))
    )
    with pytest.raises(UpdateOrganizationRepositoryException):
        rollback_feature.execute(UpdateOrganizationRequest(organization_id=uuid4(), name="X"))


def test_create_board_feature_happy_path_and_response_mapping() -> None:
    board_id = uuid4()
    organization_id = uuid4()
    service = StubService(
        response=ServiceCreateBoardResponse(
            board_id=board_id,
            organization_id=organization_id,
            name="National Board",
        )
    )
    feature = CreateBoardFeature(service=service)

    response = feature.execute(
        CreateBoardRequest(
            organization_id=organization_id,
            name="National Board",
            term_start=date(2026, 1, 1),
            term_end=date(2026, 12, 31),
            members=(
                BoardMemberInput(
                    member_id=uuid4(),
                    role="CHAIR",
                    appointed_on=date(2026, 1, 1),
                    is_chair=True,
                ),
            ),
        )
    )

    assert isinstance(response, CreateBoardResponse)
    assert response.board_id == board_id


def test_create_board_feature_validation_duplicate_rollback_exception_mapping() -> None:
    feature = CreateBoardFeature(service=StubService(response=None))

    with pytest.raises(CreateBoardValidationException):
        feature.execute(
            CreateBoardRequest(
                organization_id=uuid4(),
                name="Board",
                term_start=date(2026, 1, 1),
                term_end=date(2026, 12, 31),
                members=(),
            )
        )

    duplicate_feature = CreateBoardFeature(service=StubService(error=ServiceBusinessRuleViolation("duplicate")))
    with pytest.raises(CreateBoardBusinessRuleViolation):
        duplicate_feature.execute(
            CreateBoardRequest(
                organization_id=uuid4(),
                name="Board",
                term_start=date(2026, 1, 1),
                term_end=date(2026, 12, 31),
                members=(
                    BoardMemberInput(
                        member_id=uuid4(),
                        role="CHAIR",
                        appointed_on=date(2026, 1, 1),
                        is_chair=True,
                    ),
                ),
            )
        )

    rollback_feature = CreateBoardFeature(service=StubService(error=ServiceRepositoryException("rollback")))
    with pytest.raises(CreateBoardRepositoryException):
        rollback_feature.execute(
            CreateBoardRequest(
                organization_id=uuid4(),
                name="Board",
                term_start=date(2026, 1, 1),
                term_end=date(2026, 12, 31),
                members=(
                    BoardMemberInput(
                        member_id=uuid4(),
                        role="CHAIR",
                        appointed_on=date(2026, 1, 1),
                        is_chair=True,
                    ),
                ),
            )
        )


def test_create_committee_feature_happy_path_and_response_mapping() -> None:
    committee_id = uuid4()
    organization_id = uuid4()
    service = StubService(
        response=ServiceCreateCommitteeResponse(
            committee_id=committee_id,
            organization_id=organization_id,
            name="Safety Committee",
        )
    )
    feature = CreateCommitteeFeature(service=service)

    response = feature.execute(
        CreateCommitteeRequest(
            organization_id=organization_id,
            name="Safety Committee",
            purpose="Safety",
            members=(
                CommitteeMemberInput(
                    reference_id=uuid4(),
                    function_title="Lead",
                    joined_at=date(2026, 1, 1),
                ),
            ),
        )
    )

    assert isinstance(response, CreateCommitteeResponse)
    assert response.committee_id == committee_id


def test_create_committee_feature_validation_duplicate_rollback_exception_mapping() -> None:
    feature = CreateCommitteeFeature(service=StubService(response=None))

    with pytest.raises(CreateCommitteeValidationException):
        feature.execute(
            CreateCommitteeRequest(
                organization_id=uuid4(),
                name="",
                purpose="Safety",
            )
        )

    duplicate_feature = CreateCommitteeFeature(service=StubService(error=ServiceBusinessRuleViolation("duplicate")))
    with pytest.raises(CreateCommitteeBusinessRuleViolation):
        duplicate_feature.execute(
            CreateCommitteeRequest(
                organization_id=uuid4(),
                name="Safety",
                purpose="Safety",
            )
        )

    rollback_feature = CreateCommitteeFeature(service=StubService(error=ServiceRepositoryException("rollback")))
    with pytest.raises(CreateCommitteeRepositoryException):
        rollback_feature.execute(
            CreateCommitteeRequest(
                organization_id=uuid4(),
                name="Safety",
                purpose="Safety",
            )
        )


def test_register_volunteer_feature_happy_path_and_response_mapping() -> None:
    volunteer_id = uuid4()
    contact_id = uuid4()
    service = StubService(
        response=ServiceRegisterVolunteerResponse(
            volunteer_id=volunteer_id,
            contact_id=contact_id,
        )
    )
    feature = RegisterVolunteerFeature(service=service)

    response = feature.execute(
        RegisterVolunteerRequest(
            contact_id=contact_id,
            member_id=uuid4(),
            is_available=True,
            max_hours_per_week=8,
            preferred_days=("MONDAY",),
            skills=("FIRST AID",),
            certificates=(VolunteerCertificateInput(name="CPR", expires_at=date(2027, 1, 1)),),
            joined_at=date(2026, 1, 1),
        )
    )

    assert isinstance(response, RegisterVolunteerResponse)
    assert response.volunteer_id == volunteer_id


def test_register_volunteer_feature_validation_duplicate_rollback_exception_mapping() -> None:
    feature = RegisterVolunteerFeature(service=StubService(response=None))

    with pytest.raises(RegisterVolunteerValidationException):
        feature.execute(
            RegisterVolunteerRequest(
                contact_id=uuid4(),
                member_id=None,
                is_available=True,
                max_hours_per_week=-1,
                preferred_days=(),
                skills=(),
                certificates=(),
                joined_at=date(2026, 1, 1),
            )
        )

    duplicate_feature = RegisterVolunteerFeature(service=StubService(error=ServiceBusinessRuleViolation("duplicate")))
    with pytest.raises(RegisterVolunteerBusinessRuleViolation):
        duplicate_feature.execute(
            RegisterVolunteerRequest(
                contact_id=uuid4(),
                member_id=None,
                is_available=True,
                max_hours_per_week=1,
                preferred_days=(),
                skills=("FIRST AID",),
                certificates=(),
                joined_at=date(2026, 1, 1),
            )
        )

    rollback_feature = RegisterVolunteerFeature(service=StubService(error=ServiceRepositoryException("rollback")))
    with pytest.raises(RegisterVolunteerRepositoryException):
        rollback_feature.execute(
            RegisterVolunteerRequest(
                contact_id=uuid4(),
                member_id=None,
                is_available=True,
                max_hours_per_week=1,
                preferred_days=(),
                skills=("FIRST AID",),
                certificates=(),
                joined_at=date(2026, 1, 1),
            )
        )


def test_assign_role_feature_happy_path_and_response_mapping() -> None:
    role_id = uuid4()
    assignee_id = uuid4()
    organization_id = uuid4()
    service = StubService(
        response=ServiceAssignRoleResponse(
            role_id=role_id,
            assignee_id=assignee_id,
            organization_id=organization_id,
        )
    )
    feature = AssignRoleFeature(service=service)

    response = feature.execute(
        AssignRoleRequest(
            role_id=role_id,
            assignee_id=assignee_id,
            organization_id=organization_id,
            valid_from=date(2026, 1, 1),
        )
    )

    assert isinstance(response, AssignRoleResponse)
    assert response.role_id == role_id
    assert response.assignee_id == assignee_id


def test_assign_role_feature_validation_duplicate_rollback_exception_mapping() -> None:
    feature = AssignRoleFeature(service=StubService(response=None))

    with pytest.raises(AssignRoleValidationException):
        feature.execute(
            AssignRoleRequest(
                role_id=uuid4(),
                assignee_id=uuid4(),
                organization_id=uuid4(),
                valid_from=date(2026, 2, 1),
                valid_to=date(2026, 1, 1),
            )
        )

    duplicate_feature = AssignRoleFeature(service=StubService(error=ServiceBusinessRuleViolation("duplicate")))
    with pytest.raises(AssignRoleBusinessRuleViolation):
        duplicate_feature.execute(
            AssignRoleRequest(
                role_id=uuid4(),
                assignee_id=uuid4(),
                organization_id=uuid4(),
                valid_from=date(2026, 1, 1),
            )
        )

    rollback_feature = AssignRoleFeature(service=StubService(error=ServiceRepositoryException("rollback")))
    with pytest.raises(AssignRoleRepositoryException):
        rollback_feature.execute(
            AssignRoleRequest(
                role_id=uuid4(),
                assignee_id=uuid4(),
                organization_id=uuid4(),
                valid_from=date(2026, 1, 1),
            )
        )

    unknown_feature = AssignRoleFeature(service=StubService(error=RuntimeError("boom")))
    with pytest.raises(AssignRoleRepositoryException):
        unknown_feature.execute(
            AssignRoleRequest(
                role_id=uuid4(),
                assignee_id=uuid4(),
                organization_id=uuid4(),
                valid_from=date(2026, 1, 1),
            )
        )

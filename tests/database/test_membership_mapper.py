from datetime import date
from uuid import uuid4

from mfm.database.mappers.membership_mapper import MembershipMapper
from mfm.database.models.membership_type_model import MembershipTypeModel
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_category import MembershipCategory
from mfm.domain.membership.membership_status import MembershipStatus
from mfm.domain.membership.membership_type import MembershipType


def test_membership_mapper_domain_to_orm_and_back():
    membership_type = MembershipType(
        code="STANDARD",
        name="Standard",
        category=MembershipCategory.GENERAL,
    )
    membership = Membership(
        member_id=uuid4(),
        membership_type=membership_type,
        status=MembershipStatus.ACTIVE,
        start_date=date(2026, 1, 1),
    )

    orm = MembershipMapper.to_orm(membership)
    orm.membership_type = MembershipTypeModel(
        id=membership_type.id,
        code=membership_type.code,
        name=membership_type.name,
        category=membership_type.category,
        description=membership_type.description,
        is_active=membership_type.is_active,
    )

    round_tripped = MembershipMapper.to_domain(orm)

    assert round_tripped.id == membership.id
    assert round_tripped.member_id == membership.member_id
    assert round_tripped.membership_type.id == membership_type.id
    assert round_tripped.membership_type.code == "STANDARD"
    assert round_tripped.membership_type.category is MembershipCategory.GENERAL
    assert round_tripped.status is MembershipStatus.ACTIVE

from mfm.database.mappers.membership_type_mapper import MembershipTypeMapper
from mfm.database.models.membership_type_model import MembershipTypeModel
from mfm.domain.membership.membership_category import MembershipCategory
from mfm.domain.membership.membership_type import MembershipType


def test_membership_type_mapper_domain_to_orm_and_back():
    membership_type = MembershipType(
        code="STANDARD",
        name="Standard",
        category=MembershipCategory.GENERAL,
        description="Default membership",
        is_active=True,
    )

    orm = MembershipTypeMapper.to_orm(membership_type)

    assert isinstance(orm, MembershipTypeModel)
    assert orm.id == membership_type.id
    assert orm.code == "STANDARD"
    assert orm.name == "Standard"
    assert orm.category is MembershipCategory.GENERAL
    assert orm.description == "Default membership"
    assert orm.is_active is True

    round_tripped = MembershipTypeMapper.to_domain(orm)

    assert round_tripped.id == membership_type.id
    assert round_tripped.code == "STANDARD"
    assert round_tripped.name == "Standard"
    assert round_tripped.category is MembershipCategory.GENERAL
    assert round_tripped.description == "Default membership"
    assert round_tripped.is_active is True

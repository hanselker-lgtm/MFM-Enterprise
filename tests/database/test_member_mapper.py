from datetime import date
from uuid import uuid4

from mfm.database.mappers.member_mapper import MemberMapper
from mfm.database.models.member_model import MemberModel
from mfm.domain.member.member import Member
from mfm.domain.member.member_status import MemberStatus


def test_member_mapper_domain_to_orm_and_back():
    member = Member(
        contact_id=uuid4(),
        member_number="M-100001",
        status=MemberStatus.ACTIVE,
        join_date=date(2026, 1, 1),
        leave_date=None,
    )

    orm = MemberMapper.to_orm(member)

    assert isinstance(orm, MemberModel)
    assert orm.id == member.id
    assert orm.contact_id == member.contact_id
    assert orm.member_number == member.member_number
    assert orm.status == MemberStatus.ACTIVE

    round_tripped = MemberMapper.to_domain(orm)

    assert round_tripped.id == member.id
    assert round_tripped.contact_id == member.contact_id
    assert round_tripped.member_number == "M-100001"
    assert round_tripped.status == MemberStatus.ACTIVE
    assert round_tripped.join_date == date(2026, 1, 1)

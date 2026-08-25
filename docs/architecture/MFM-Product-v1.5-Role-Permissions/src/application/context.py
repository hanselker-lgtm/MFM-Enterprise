from src.repositories.project_repository import ProjectRepository
from src.repositories.task_repository import TaskRepository
from src.repositories.risk_repository import RiskRepository
from src.repositories.decision_repository import DecisionRepository
from src.services.project_service import ProjectService
from src.services.task_service import TaskService
from src.services.risk_service import RiskService
from src.services.decision_service import DecisionService
from src.repositories.accounting_repository import AccountingRepository
from src.services.accounting_service import AccountingService
from src.repositories.member_repository import MemberRepository
from src.services.member_service import MemberService
from src.repositories.bank_repository import BankRepository
from src.services.bank_service import BankService
from src.services.management_service import ManagementService
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from src.services.system_service import SystemService
from src.repositories.permission_repository import PermissionRepository
from src.services.permission_service import PermissionService
from src.services.search_service import SearchService
from src.services.export_service import ExportService
from src.services.organization_service import OrganizationService

class ApplicationContext:
    def __init__(self, db):
        self.db = db
        self.projects = ProjectService(ProjectRepository(db))
        self.tasks = TaskService(TaskRepository(db))
        self.risks = RiskService(RiskRepository(db))
        self.decisions = DecisionService(DecisionRepository(db))
        self.accounting = AccountingService(AccountingRepository(db))
        self.accounting.seed_standard_accounts()
        self.members = MemberService(MemberRepository(db), self.accounting)
        self.bank = BankService(BankRepository(db))
        self.management = ManagementService(self)
        self.users = UserService(UserRepository(db))
        self.users.ensure_defaults()
        self.system = SystemService(db)
        self.permissions = PermissionService(PermissionRepository(db), self.users.repo)
        self.permissions.ensure_defaults()
        self.search = SearchService(db)
        self.export = ExportService(self)
        self.organization = OrganizationService(db)

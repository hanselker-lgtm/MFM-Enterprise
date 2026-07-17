# RC-001B Public API Stability Review

Date: 2026-07-17
Scope: Review of all Feature APIs under src/mfm/application/features without behavior changes.

## Executive Summary

- Total Feature APIs reviewed: 117
- Classification counts: Stable=110, Internal=7, Experimental=0, Deprecated=0
- Command/query split: Commands=92, Queries=25
- Leakage checks (imports): domain=14, persistence=0, gui=0, repositories=0
- DTO contract verification: architecture tests enforce immutable Request/Response DTOs and response-level no-domain exposure for Feature APIs.
- Exception strategy: broad consistency found; most features map service-layer Validation/BusinessRule/Repository exceptions to feature-local exceptions.

## Verification Results

### Leakage Verification

- No persistence leakage imports found in Feature packages: 0
- No GUI leakage imports found in Feature packages: 0
- No repository exposure imports found in Feature packages: 0
- Domain imports present in 14 Feature modules (primarily enums/value types in request mapping):
  - AnnualContingentGenerationFeature (mfm.application.features.annual_contingent_generation)
  - CreateAnnualContingentFeature (mfm.application.features.annual_contingent_generation)
  - ListGeneralLedgerFeature (mfm.application.features.general_ledger_service)
  - CreateMemberFeature (mfm.application.features.member_enrollment)
  - MemberEnrollmentFeature (mfm.application.features.member_enrollment)
  - CreateAssetFeature (mfm.application.features.asset.create_asset_feature)
  - ChangeVesselStatusFeature (mfm.application.features.fleet.change_vessel_status_feature)
  - CreateVesselFeature (mfm.application.features.fleet.create_vessel_feature)
  - UpdateVesselFeature (mfm.application.features.fleet.update_vessel_feature)
  - CompleteOrganizationOnboardingFeature (mfm.application.features.onboarding.complete_organization_onboarding_feature)
  - CreateOrganizationFeature (mfm.application.features.organization.create_organization_feature)
  - UpdateOrganizationFeature (mfm.application.features.organization.update_organization_feature)
  - AddTechnicalComponentFeature (mfm.application.features.technical_configuration.add_technical_component_feature)
  - ReplaceTechnicalComponentFeature (mfm.application.features.technical_configuration.replace_technical_component_feature)

### DTO Contract Verification

- Existing architecture test suite covers:
  - execute(request) signature and documentation requirements
  - immutable Request DTO requirement
  - immutable Response DTO requirement
  - response fields must not expose domain types

### Command/Query Separation

- Query features (module names get/list/search/find/read): 25
- Command features: 92
- Separation is mostly consistent by naming; no mixed command+query public methods found inside Feature classes (single execute entry point pattern).

### Naming Consistency

- Class naming: all reviewed public API classes use *Feature suffix.
- Module naming: mostly *_feature.py per capability package, with a few non-suffixed internal modules that still host Feature classes (annual_contingent_generation, general_ledger_service, member_enrollment).

### Exception Strategy

- Features with explicit validation/business/repository exception mapping signals: 115
- Common mapping pattern: ServiceValidationException -> ValidationException, ServiceBusinessRuleViolation -> BusinessRuleViolation, ServiceRepositoryException/Exception -> RepositoryException.
- Risk: broad except Exception clauses can mask root causes if overused.

## Stable APIs

- mfm.application.features.accounting
  - CloseFiscalYearFeature (mfm.application.features.accounting.close_fiscal_year_feature)
  - CreateFiscalYearFeature (mfm.application.features.accounting.create_fiscal_year_feature)
  - CreateJournalFeature (mfm.application.features.accounting.create_journal_feature)
  - CreateLedgerAccountFeature (mfm.application.features.accounting.create_ledger_account_feature)
  - GetFiscalYearFeature (mfm.application.features.accounting.get_fiscal_year_feature)
  - GetJournalFeature (mfm.application.features.accounting.get_journal_feature)
  - GetLedgerAccountFeature (mfm.application.features.accounting.get_ledger_account_feature)
  - ListFiscalYearsFeature (mfm.application.features.accounting.list_fiscal_years_feature)
  - ListJournalsFeature (mfm.application.features.accounting.list_journals_feature)
  - ListLedgerAccountsFeature (mfm.application.features.accounting.list_ledger_accounts_feature)
  - OpenFiscalYearFeature (mfm.application.features.accounting.open_fiscal_year_feature)
  - PostJournalFeature (mfm.application.features.accounting.post_journal_feature)
  - ReverseJournalFeature (mfm.application.features.accounting.reverse_journal_feature)
  - SearchJournalsFeature (mfm.application.features.accounting.search_journals_feature)
  - UpdateLedgerAccountFeature (mfm.application.features.accounting.update_ledger_account_feature)
- mfm.application.features.asset
  - CreateAssetFeature (mfm.application.features.asset.create_asset_feature)
  - DisposeAssetFeature (mfm.application.features.asset.dispose_asset_feature)
  - RelocateAssetFeature (mfm.application.features.asset.relocate_asset_feature)
  - RetireAssetFeature (mfm.application.features.asset.retire_asset_feature)
  - TransferOwnershipFeature (mfm.application.features.asset.transfer_ownership_feature)
  - UpdateAssetFeature (mfm.application.features.asset.update_asset_feature)
- mfm.application.features.certificates
  - ActivateCertificateFeature (mfm.application.features.certificates.activate_certificate_feature)
  - CreateCertificateFeature (mfm.application.features.certificates.create_certificate_feature)
  - EvaluateCertificateStatusFeature (mfm.application.features.certificates.evaluate_certificate_status_feature)
  - GetCertificateHistoryFeature (mfm.application.features.certificates.get_certificate_history_feature)
  - GetExpiringCertificatesFeature (mfm.application.features.certificates.get_expiring_certificates_feature)
  - RenewCertificateFeature (mfm.application.features.certificates.renew_certificate_feature)
  - RevokeCertificateFeature (mfm.application.features.certificates.revoke_certificate_feature)
  - SuspendCertificateFeature (mfm.application.features.certificates.suspend_certificate_feature)
- mfm.application.features.documents
  - ArchiveDocumentFeature (mfm.application.features.documents.archive_document_feature)
  - AttachReferenceFeature (mfm.application.features.documents.attach_reference_feature)
  - CreateDocumentFeature (mfm.application.features.documents.create_document_feature)
  - DeleteDocumentFeature (mfm.application.features.documents.delete_document_feature)
  - GetDocumentFeature (mfm.application.features.documents.get_document_feature)
  - ListDocumentsFeature (mfm.application.features.documents.list_documents_feature)
  - RegisterDocumentVersionFeature (mfm.application.features.documents.register_document_version_feature)
  - RemoveReferenceFeature (mfm.application.features.documents.remove_reference_feature)
  - SearchDocumentsFeature (mfm.application.features.documents.search_documents_feature)
  - UpdateDocumentMetadataFeature (mfm.application.features.documents.update_document_metadata_feature)
- mfm.application.features.fleet
  - ChangeVesselRegistrationFeature (mfm.application.features.fleet.change_vessel_registration_feature)
  - ChangeVesselStatusFeature (mfm.application.features.fleet.change_vessel_status_feature)
  - CreateVesselFeature (mfm.application.features.fleet.create_vessel_feature)
  - RenameVesselFeature (mfm.application.features.fleet.rename_vessel_feature)
  - UpdateVesselDimensionsFeature (mfm.application.features.fleet.update_vessel_dimensions_feature)
  - UpdateVesselFeature (mfm.application.features.fleet.update_vessel_feature)
- mfm.application.features.inventory
  - AdjustStockFeature (mfm.application.features.inventory.adjust_stock_feature)
  - CreateInventoryItemFeature (mfm.application.features.inventory.create_inventory_item_feature)
  - DeactivateInventoryItemFeature (mfm.application.features.inventory.deactivate_inventory_item_feature)
  - GetInventoryItemFeature (mfm.application.features.inventory.get_inventory_item_feature)
  - IssueStockFeature (mfm.application.features.inventory.issue_stock_feature)
  - ListInventoryItemsFeature (mfm.application.features.inventory.list_inventory_items_feature)
  - ListLowStockItemsFeature (mfm.application.features.inventory.list_low_stock_items_feature)
  - ReactivateInventoryItemFeature (mfm.application.features.inventory.reactivate_inventory_item_feature)
  - ReceiveStockFeature (mfm.application.features.inventory.receive_stock_feature)
- mfm.application.features.maintenance
  - AddMaintenanceRequirementFeature (mfm.application.features.maintenance.add_maintenance_requirement_feature)
  - CalculateDueMaintenanceFeature (mfm.application.features.maintenance.calculate_due_maintenance_feature)
  - CancelWorkOrderFeature (mfm.application.features.maintenance.cancel_work_order_feature)
  - CompleteWorkOrderFeature (mfm.application.features.maintenance.complete_work_order_feature)
  - CreateMaintenancePlanFeature (mfm.application.features.maintenance.create_maintenance_plan_feature)
  - CreateWorkOrderFeature (mfm.application.features.maintenance.create_work_order_feature)
  - GetMaintenanceHistoryFeature (mfm.application.features.maintenance.get_maintenance_history_feature)
  - OpenWorkOrderFeature (mfm.application.features.maintenance.open_work_order_feature)
  - StartWorkOrderFeature (mfm.application.features.maintenance.start_work_order_feature)
  - UpdateMaintenanceRequirementFeature (mfm.application.features.maintenance.update_maintenance_requirement_feature)
- mfm.application.features.onboarding
  - CompleteOrganizationOnboardingFeature (mfm.application.features.onboarding.complete_organization_onboarding_feature)
  - ProjectAccountingFeature (mfm.application.features.onboarding.project_accounting_feature)
  - ProjectBudgetInitializationFeature (mfm.application.features.onboarding.project_budget_initialization_feature)
  - ProjectClosureArchiveFeature (mfm.application.features.onboarding.project_closure_archive_feature)
  - ProjectDocumentRegistrationFeature (mfm.application.features.onboarding.project_document_registration_feature)
- mfm.application.features.organization
  - AssignRoleFeature (mfm.application.features.organization.assign_role_feature)
  - CreateBoardFeature (mfm.application.features.organization.create_board_feature)
  - CreateCommitteeFeature (mfm.application.features.organization.create_committee_feature)
  - CreateOrganizationFeature (mfm.application.features.organization.create_organization_feature)
  - RegisterVolunteerFeature (mfm.application.features.organization.register_volunteer_feature)
  - UpdateOrganizationFeature (mfm.application.features.organization.update_organization_feature)
- mfm.application.features.procurement
  - AmendDraftPurchaseOrderFeature (mfm.application.features.procurement.amend_draft_purchase_order_feature)
  - ApprovePurchaseOrderFeature (mfm.application.features.procurement.approve_purchase_order_feature)
  - CancelPurchaseOrderFeature (mfm.application.features.procurement.cancel_purchase_order_feature)
  - CreatePurchaseOrderFeature (mfm.application.features.procurement.create_purchase_order_feature)
  - GetPurchaseOrderFeature (mfm.application.features.procurement.get_purchase_order_feature)
  - ListPurchaseOrdersByStateFeature (mfm.application.features.procurement.list_purchase_orders_by_state_feature)
  - ListPurchaseOrdersBySupplierFeature (mfm.application.features.procurement.list_purchase_orders_by_supplier_feature)
  - ListPurchaseOrdersFeature (mfm.application.features.procurement.list_purchase_orders_feature)
  - PlacePurchaseOrderFeature (mfm.application.features.procurement.place_purchase_order_feature)
  - RecordPurchaseReceiptFeature (mfm.application.features.procurement.record_purchase_receipt_feature)
  - SubmitPurchaseOrderFeature (mfm.application.features.procurement.submit_purchase_order_feature)
- mfm.application.features.projects
  - ArchiveProjectFeature (mfm.application.features.projects.archive_project_feature)
  - CompleteProjectFeature (mfm.application.features.projects.complete_project_feature)
  - CreateProjectFeature (mfm.application.features.projects.create_project_feature)
  - DeleteProjectFeature (mfm.application.features.projects.delete_project_feature)
  - GetProjectFeature (mfm.application.features.projects.get_project_feature)
  - ListProjectsFeature (mfm.application.features.projects.list_projects_feature)
  - SearchProjectsFeature (mfm.application.features.projects.search_projects_feature)
  - UpdateProjectFeature (mfm.application.features.projects.update_project_feature)
- mfm.application.features.reporting
  - BudgetVsActualFeature (mfm.application.features.reporting.budget_vs_actual_feature)
  - OrganizationDashboardFeature (mfm.application.features.reporting.organization_dashboard_feature)
  - ProjectStatusFeature (mfm.application.features.reporting.project_status_feature)
- mfm.application.features.technical_configuration
  - AddTechnicalComponentFeature (mfm.application.features.technical_configuration.add_technical_component_feature)
  - CreateTechnicalConfigurationFeature (mfm.application.features.technical_configuration.create_technical_configuration_feature)
  - InstallTechnicalComponentFeature (mfm.application.features.technical_configuration.install_technical_component_feature)
  - RemoveTechnicalComponentFeature (mfm.application.features.technical_configuration.remove_technical_component_feature)
  - ReplaceTechnicalComponentFeature (mfm.application.features.technical_configuration.replace_technical_component_feature)
  - UpdateTechnicalComponentDetailsFeature (mfm.application.features.technical_configuration.update_technical_component_details_feature)
- mfm.application.features.voyages
  - ArriveVoyageFeature (mfm.application.features.voyages.arrive_voyage_feature)
  - CancelVoyageFeature (mfm.application.features.voyages.cancel_voyage_feature)
  - CreateVoyageFeature (mfm.application.features.voyages.create_voyage_feature)
  - DepartVoyageFeature (mfm.application.features.voyages.depart_voyage_feature)
  - GetVoyageFeature (mfm.application.features.voyages.get_voyage_feature)
  - ListVesselVoyagesFeature (mfm.application.features.voyages.list_vessel_voyages_feature)
  - PlanVoyageFeature (mfm.application.features.voyages.plan_voyage_feature)

## Internal APIs

- mfm.application.features
  - AnnualContingentGenerationFeature (mfm.application.features.annual_contingent_generation)
  - CreateAnnualContingentFeature (mfm.application.features.annual_contingent_generation)
  - CreateMemberFeature (mfm.application.features.member_enrollment)
  - ListGeneralLedgerFeature (mfm.application.features.general_ledger_service)
  - MemberEnrollmentFeature (mfm.application.features.member_enrollment)
- mfm.application.features.onboarding
  - CompleteProjectCreationFeature (mfm.application.features.onboarding.complete_project_creation_feature)
- mfm.application.features.reporting
  - ActiveProjectsFeature (mfm.application.features.reporting.active_projects_feature)

## Experimental APIs

- None

## Deprecated APIs

- None

## Recommended API Changes

1. Reduce domain-type coupling in request contracts for public Stable APIs by replacing domain enums/value objects with API-local enums/value DTOs where feasible.
2. Promote explicit public-surface governance: require __all__ in every features subpackage __init__.py and treat export list as the authoritative stable surface.
3. Standardize module naming for Feature hosts to *_feature.py to improve discoverability and public API clarity.
4. Tighten exception handling by minimizing generic Exception catches and preserving root-cause chaining/telemetry context consistently.

## Backlog Items

1. Add architecture test asserting no domain imports in Stable Feature modules unless explicitly allowlisted (with rationale).
2. Add architecture test asserting every public Feature is exported from its package __init__.py.
3. Add API review gate in CI that diff-checks stable export surfaces and flags unreviewed public-surface changes.
4. Convert internal features to explicit internal namespace or promote them to stable with documentation and contract tests.
5. Add linter rule/check for consistent *_feature.py module naming for classes ending with Feature.


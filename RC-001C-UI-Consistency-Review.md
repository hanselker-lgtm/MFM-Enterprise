# RC-001C UI Consistency Review

Date: 2026-07-17
Scope: Complete Presentation Layer consistency review in src/mfm/presentation.
Constraint: No new functionality, no architectural changes, only objective usability/consistency improvements.

## Executive Summary

This review covered navigation consistency, toolbars, window titles, icons, keyboard shortcuts, status messages, dialogs, success notifications, selection behavior, naming consistency, spacing, common dialog behavior, loading, empty-state behavior, and refresh behavior.

Objective consistency improvements were applied without changing architecture or domain behavior:
- Navigation tree now supports single-click route activation in addition to activated events.
- Main window title now reflects current route label for contextual consistency.
- Status bar messages now use a transient display window.
- Search/refresh behavior is aligned across toolbars (Enter to search, F5 for refresh).
- Toolbar spacing/margins are aligned across Projects, Documents, and Accounting workspaces.
- List selection mode is aligned to single-row selection in all three list views.
- Success notifications were added for document version registration, document archive, and journal posting to match existing create-action feedback patterns.

## Findings

### Critical

- None.

### High

1. Inconsistent navigation activation behavior across UI interactions
- Evidence: Left navigation used activated event only, making route changes less predictable between keyboard/mouse interactions.
- Improvement applied: Connected itemClicked in addition to itemActivated.

2. Inconsistent operation feedback for non-create actions
- Evidence: Some actions (create) showed success dialogs, while archive/post/register actions did not.
- Improvement applied: Added success notifications for archive document, register version, and post journal.

### Medium

1. Toolbar interaction and shortcut inconsistency
- Evidence: Search relied only on button click in toolbars; refresh had no consistent shortcut.
- Improvement applied: Enter triggers search, F5 triggers refresh in all operational toolbars.

2. Window context signaling inconsistency
- Evidence: Shell title was static regardless of current route.
- Improvement applied: Window title now includes selected route label.

3. Selection behavior inconsistency risk
- Evidence: List views selected rows, but single-selection policy was not explicitly enforced.
- Improvement applied: Enabled single-selection mode across list views.

### Low

1. Icons are still not consistently applied across navigation and toolbar actions
- Current state: Functional, but visual icon language remains sparse.
- Recommendation: Introduce a shared icon policy using Qt standard icons or resource icons.

2. Loading/empty-state messaging remains minimal in list/detail panes
- Current state: Functional tables with pagination; no dedicated loading indicator or explicit empty-state callout label.
- Recommendation: Add non-invasive empty-state labels and lightweight busy indicators in a future incremental pass.

3. Dialog copy style can be further normalized
- Current state: Titles/messages are clear; wording style is mostly consistent but not centrally standardized.
- Recommendation: Introduce shared dialog message helpers/constants for uniform tone.

## Recommended Improvements

1. Define a shared UI interaction guideline for route activation, keyboard shortcuts, and status feedback.
2. Add a small shared helper for success/error dialog phrasing to keep notification wording consistent.
3. Introduce consistent icon usage policy for primary actions and navigation categories.
4. Add explicit empty-state placeholders for list views when item count is zero.
5. Add lightweight loading feedback for refresh/search actions that may take longer.
6. Add additional presentation tests for shortcut-triggered actions and success-notification consistency.

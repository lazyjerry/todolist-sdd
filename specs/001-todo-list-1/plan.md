# Implementation Plan: TODO List Backend API

**Branch**: `001-todo-list-1` | **Date**: 2025 年 9 月 9 日 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-list-1/spec.md`

## Execution Flow (/plan command scope)

```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
4. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
5. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, or `GEMINI.md` for Gemini CLI).
6. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
7. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
8. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:

- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary

TODO List 後端 API 提供基本的 CRUD 操作功能，使用 Laravel 12 框架實現，包含 Laravel Sail 開發環境配置 (MariaDB)，所有程式碼需要中文註解。主要功能包括新增、查看、更新和刪除任務，任務實體包含 title 和 description 欄位。

## Technical Context

**Language/Version**: PHP 8.3, Laravel 12  
**Primary Dependencies**: Laravel 12, Laravel Sail, MariaDB, PHPUnit  
**Storage**: MariaDB 資料庫  
**Testing**: PHPUnit, Laravel Feature Tests, Database Testing  
**Target Platform**: Docker 容器環境 (Laravel Sail)
**Project Type**: web (單體後端 API)  
**Performance Goals**: 標準 REST API 回應時間 <200ms  
**Constraints**: 需要中文註解和流程說明，使用 Laravel 標準實作模式  
**Scale/Scope**: 基本 TODO 應用，支援基本 CRUD 操作，單一使用者情境

User Arguments: 請建立一個 laravel-todo-example 資料夾作為專案資料夾。使用 Laravel 12 實現，包含 sail 的開發環境（使用 mariadb），添加的程式碼，包含測試的程式碼與設定檔，其中函式和變數需要有中文註解與中文流程說明。

## Constitution Check

_GATE: Must pass before Phase 0 research. Re-check after Phase 1 design._

**Simplicity**:

- Projects: 1 (Laravel 專案 laravel-todo-example)
- Using framework directly? Yes (直接使用 Laravel 標準模式)
- Single data model? Yes (Todo 模型)
- Avoiding patterns? Yes (使用 Laravel 標準的 Model-Controller 模式，不額外抽象)

**Architecture**:

- EVERY feature as library? 否 (Laravel 專案不需要庫結構，使用標準 MVC)
- Libraries listed: N/A (標準 Laravel 結構)
- CLI per library: 否 (使用 Laravel Artisan 命令)
- Library docs: N/A (使用 Laravel 文件標準)

**Testing (NON-NEGOTIABLE)**:

- RED-GREEN-Refactor cycle enforced? Yes (先寫測試後實作)
- Git commits show tests before implementation? Yes
- Order: Contract→Integration→E2E→Unit strictly followed? Yes (Feature Tests → Unit Tests)
- Real dependencies used? Yes (真實 MariaDB 資料庫)
- Integration tests for: API endpoints, database operations
- FORBIDDEN: Implementation before test, skipping RED phase

**Observability**:

- Structured logging included? Yes (Laravel Log)
- Frontend logs → backend? N/A (後端 API only)
- Error context sufficient? Yes (Laravel 錯誤處理)

**Versioning**:

- Version number assigned? 1.0.0
- BUILD increments on every change? Yes
- Breaking changes handled? Yes (migration scripts)

## Project Structure

### Documentation (this feature)

```
specs/[###-feature]/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)

```
### Source Code (repository root)
```

# Laravel 專案結構 (laravel-todo-example)

laravel-todo-example/
├── app/
│ ├── Models/ # Todo 模型
│ ├── Http/
│ │ ├── Controllers/ # TodoController
│ │ └── Requests/ # 驗證請求
│ └── Services/ # 業務邏輯 (如需要)
├── database/
│ ├── migrations/ # 資料庫遷移
│ └── seeders/ # 測試資料
├── tests/
│ ├── Feature/ # API 功能測試
│ └── Unit/ # 單元測試
├── routes/
│ └── api.php # API 路由
├── docker-compose.yml # Sail 配置
└── README.md # 中文說明文件

```

**Structure Decision**: Laravel 標準結構 (Option 1 修改版)

## Phase 0: Outline & Research
1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:
```

For each unknown in Technical Context:
Task: "Research {unknown} for {feature context}"
For each technology choice:
Task: "Find best practices for {tech} in {domain}"

```

3. **Consolidate findings** in `research.md` using format:
- Decision: [what was chosen]
- Rationale: [why chosen]
- Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`:
- Entity name, fields, relationships
- Validation rules from requirements
- State transitions if applicable

2. **Generate API contracts** from functional requirements:
- For each user action → endpoint
- Use standard REST/GraphQL patterns
- Output OpenAPI/GraphQL schema to `/contracts/`

3. **Generate contract tests** from contracts:
- One test file per endpoint
- Assert request/response schemas
- Tests must fail (no implementation yet)

4. **Extract test scenarios** from user stories:
- Each story → integration test scenario
- Quickstart test = story validation steps

5. **Update agent file incrementally** (O(1) operation):
- Run `/scripts/update-agent-context.sh [claude|gemini|copilot]` for your AI assistant
- If exists: Add only NEW tech from current plan
- Preserve manual additions between markers
- Update recent changes (keep last 3)
- Keep under 150 lines for token efficiency
- Output to repository root

**Output**: data-model.md, /contracts/*, failing tests, quickstart.md, agent-specific file

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `/templates/tasks-template.md` as base
- Generate tasks from Phase 1 design docs (contracts, data model, quickstart)
- Each contract → contract test task [P]
- Each entity → model creation task [P]
- Each user story → integration test task
- Implementation tasks to make tests pass

**Ordering Strategy**:
- TDD order: Tests before implementation
- Dependency order: Models before services before UI
- Mark [P] for parallel execution (independent files)

**Estimated Output**: 25-30 numbered, ordered tasks in tasks.md

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)
**Phase 4**: Implementation (execute tasks.md following constitutional principles)
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking
*No violations identified - using standard Laravel patterns*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |

## Phase 2: Task Planning Approach
*這個階段描述 /tasks 命令將會執行的內容 - 不在 /plan 期間執行*

**任務生成策略**:
- 載入 `/templates/tasks-template.md` 作為基礎
- 從 Phase 1 設計文件生成任務 (合約、數據模型、快速開始)
- 每個 API 端點 → 合約測試任務 [P]
- 每個實體 → 模型建立任務 [P]
- 每個使用者故事 → 整合測試任務
- 實作任務讓測試通過

**排序策略**:
- TDD 順序：測試先於實作
- 依賴順序：模型 → 服務 → 控制器 → API
- 標記 [P] 表示可平行執行 (獨立檔案)

**預估輸出**: 在 tasks.md 中包含 15-20 個有序任務

**重要提醒**: 此階段由 /tasks 命令執行，不是由 /plan 執行

## Progress Tracking
*This checklist is updated during execution flow*

**Phase Status**:
- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [x] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [x] Complexity deviations documented (none)

---
*Based on Constitution v2.1.1 - See `/memory/constitution.md`*
```

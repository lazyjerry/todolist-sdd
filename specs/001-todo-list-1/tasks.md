# Tasks: TODO List Backend API

**Input**: Design documents from `/specs/001-todo-list-1/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow (main)

```
1. Load plan.md from feature directory
   → Tech stack: Laravel 12, Sail, MariaDB, PHPUnit
   → Structure: Laravel 標準 MVC 架構
2. Load design documents:
   → data-model.md: Todo 實體 → model tasks
   → contracts/api-spec.yaml: 5 個端點 → contract test tasks
   → research.md: Laravel + Sail 決策 → setup tasks
3. Generated tasks by category:
   → Setup: Laravel 專案建立、Sail 環境、依賴安裝
   → Tests: API 合約測試、功能測試
   → Core: Todo 模型、控制器、驗證請求
   → Integration: 資料庫遷移、路由配置
   → Polish: 單元測試、文件、清理
4. Task rules applied:
   → 不同檔案 = 標記 [P] 平行執行
   → 相同檔案 = 順序執行
   → 測試優先於實作 (TDD)
5. 任務編號: T001-T020
6. 依賴關係已建立
7. 平行執行範例已提供
8. 任務完整性驗證: ✓
```

## Format: `[ID] [P?] Description`

- **[P]**: 可平行執行 (不同檔案，無依賴關係)
- 包含確切的檔案路徑

## Path Conventions

Laravel 專案結構 (laravel-todo-example/):

- **Models**: `app/Models/`
- **Controllers**: `app/Http/Controllers/`
- **Requests**: `app/Http/Requests/`
- **Migrations**: `database/migrations/`
- **Tests**: `tests/Feature/`, `tests/Unit/`
- **Routes**: `routes/api.php`

## Phase 3.1: Setup

- [ ] T001 建立 laravel-todo-example 專案目錄並設置 Laravel 12 + Sail 環境
- [ ] T002 配置 .env 檔案、生成 APP_KEY 並確保 MariaDB 連線正常
- [ ] T003 [P] 安裝並配置開發工具 (Telescope, Debugbar)

## Phase 3.2: Tests First (TDD) ⚠️ 必須在 3.3 之前完成

**重要: 這些測試必須先寫並且必須失敗，才能進行任何實作**

- [ ] T004 [P] API 合約測試 GET /api/todos 在 tests/Feature/TodoApiGetAllTest.php
- [ ] T005 [P] API 合約測試 POST /api/todos 在 tests/Feature/TodoApiCreateTest.php
- [ ] T006 [P] API 合約測試 GET /api/todos/{id} 在 tests/Feature/TodoApiGetSingleTest.php
- [ ] T007 [P] API 合約測試 PUT /api/todos/{id} 在 tests/Feature/TodoApiUpdateTest.php
- [ ] T008 [P] API 合約測試 PATCH /api/todos/{id} 在 tests/Feature/TodoApiPatchTest.php
- [ ] T009 [P] API 合約測試 DELETE /api/todos/{id} 在 tests/Feature/TodoApiDeleteTest.php
- [ ] T010 [P] 整合測試 Todo CRUD 完整流程在 tests/Feature/TodoCrudIntegrationTest.php

## Phase 3.3: Core Implementation (僅在測試失敗後執行)

- [ ] T011 [P] 建立 todos 資料表遷移檔案 database/migrations/xxxx_create_todos_table.php
- [ ] T012 [P] 建立 Todo 模型 app/Models/Todo.php (包含中文註解)
- [ ] T013 [P] 建立 StoreTodoRequest 驗證請求 app/Http/Requests/StoreTodoRequest.php
- [ ] T014 [P] 建立 UpdateTodoRequest 驗證請求 app/Http/Requests/UpdateTodoRequest.php
- [ ] T015 建立 TodoController API 控制器 app/Http/Controllers/TodoController.php (包含所有 CRUD 方法和中文註解)
- [ ] T016 配置 API 路由 routes/api.php

## Phase 3.4: Integration

- [ ] T017 執行資料庫遷移並驗證資料表結構
- [ ] T018 建立 TodoSeeder 測試資料產生器 database/seeders/TodoSeeder.php
- [ ] T019 配置 API 錯誤處理和回應格式

## Phase 3.5: Polish

- [ ] T020 [P] 建立 Todo 模型單元測試 tests/Unit/TodoModelTest.php
- [ ] T021 [P] 建立驗證規則單元測試 tests/Unit/TodoValidationTest.php
- [ ] T022 [P] 更新 README.md 專案說明文件 (中文)
- [ ] T023 執行完整測試套件並確保所有測試通過
- [ ] T024 效能測試和最佳化 (API 回應時間 <200ms)

## Dependencies

**測試階段 (T004-T010) 必須在實作階段 (T011-T016) 之前完成**

- T011 (遷移) 阻塞 T017 (執行遷移)
- T012 (模型) 阻塞 T015 (控制器), T020 (單元測試)
- T013, T014 (驗證請求) 阻塞 T015 (控制器)
- T015 (控制器) 阻塞 T016 (路由)
- T016 (路由) 阻塞 T019 (錯誤處理)
- 所有實作完成後才能進行 Polish (T020-T024)

## Parallel Example

```bash
# 同時啟動 T004-T010 合約和整合測試:
Task: "API 合約測試 GET /api/todos 在 tests/Feature/TodoApiGetAllTest.php"
Task: "API 合約測試 POST /api/todos 在 tests/Feature/TodoApiCreateTest.php"
Task: "API 合約測試 GET /api/todos/{id} 在 tests/Feature/TodoApiGetSingleTest.php"
Task: "API 合約測試 PUT /api/todos/{id} 在 tests/Feature/TodoApiUpdateTest.php"
Task: "API 合約測試 PATCH /api/todos/{id} 在 tests/Feature/TodoApiPatchTest.php"
Task: "API 合約測試 DELETE /api/todos/{id} 在 tests/Feature/TodoApiDeleteTest.php"
Task: "整合測試 Todo CRUD 完整流程在 tests/Feature/TodoCrudIntegrationTest.php"

# 同時啟動 T011-T014 基礎建設:
Task: "建立 todos 資料表遷移檔案 database/migrations/xxxx_create_todos_table.php"
Task: "建立 Todo 模型 app/Models/Todo.php"
Task: "建立 StoreTodoRequest 驗證請求 app/Http/Requests/StoreTodoRequest.php"
Task: "建立 UpdateTodoRequest 驗證請求 app/Http/Requests/UpdateTodoRequest.php"

# 同時啟動 T020-T022 單元測試和文件:
Task: "建立 Todo 模型單元測試 tests/Unit/TodoModelTest.php"
Task: "建立驗證規則單元測試 tests/Unit/TodoValidationTest.php"
Task: "更新 README.md 專案說明文件"
```

## Notes

- [P] 任務 = 不同檔案，無依賴關係
- 確保測試在實作前失敗
- 每個任務完成後提交
- 所有程式碼必須包含中文註解
- 遵循 Laravel 最佳實踐
- 使用 TDD 開發流程

## 具體任務內容說明

### T001: Laravel 專案設置

- 建立 `laravel-todo-example` 目錄
- 使用 `curl -s "https://laravel.build/laravel-todo-example?with=mariadb,redis,mailpit" | bash` 建立專案
- 啟動 Sail 環境: `./vendor/bin/sail up -d`

### T004-T010: 測試檔案

每個測試檔案應包含:

- 完整的 HTTP 請求測試
- 預期的回應格式驗證
- 錯誤情境測試
- 資料庫狀態驗證

### T011: 資料庫遷移

```php
Schema::create('todos', function (Blueprint $table) {
    $table->id();                                    // 主鍵 ID
    $table->string('title');                         // 任務標題
    $table->text('description');                     // 任務描述
    $table->boolean('completed')->default(false);   // 完成狀態
    $table->timestamps();                            // created_at, updated_at
    $table->index('completed');                      // 完成狀態索引
    $table->index('created_at');                     // 建立時間索引
});
```

### T012: Todo 模型

- Eloquent 模型定義
- fillable 屬性設定
- casts 屬性設定
- 中文註解說明

### T015: TodoController

必須實作的方法:

- index(): 獲取所有任務
- store(): 建立新任務
- show(): 獲取特定任務
- update(): 完整更新任務
- destroy(): 刪除任務

## Validation Checklist

- [x] 所有 API 端點都有對應的合約測試
- [x] Todo 實體有模型建立任務
- [x] 所有測試都在實作之前
- [x] 平行任務真正獨立
- [x] 每個任務都指定確切的檔案路徑
- [x] 沒有任務修改與其他 [P] 任務相同的檔案
- [x] 包含中文註解要求
- [x] 遵循 TDD 開發流程

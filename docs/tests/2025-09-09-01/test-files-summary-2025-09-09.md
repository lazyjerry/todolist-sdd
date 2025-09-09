# 測試檔案與方法清單

## 測試檔案結構

```
tests/
├── Feature/
│   ├── ExampleTest.php
│   └── TodoApiTest.php
└── Unit/
    ├── ExampleTest.php
    └── TodoModelTest.php
```

## 詳細測試方法清單

### 1. Tests\Unit\ExampleTest

- `test_that_true_is_true()` - 基本真值測試

### 2. Tests\Unit\TodoModelTest

- `testCanCreateTodo()` - 測試模型建立功能
- `testCompletedDefaultsToFalse()` - 測試預設值設定
- `testAttributeCasting()` - 測試屬性類型轉換
- `testFillableAttributes()` - 測試可批量賦值屬性
- `testTimestampsAreManaged()` - 測試時間戳自動管理

### 3. Tests\Feature\ExampleTest

- `test_the_application_returns_a_successful_response()` - 基本 HTTP 響應測試

### 4. Tests\Feature\TodoApiTest

- `testCanGetAllTodos()` - 測試獲取所有任務 API
- `testCanCreateTodo()` - 測試建立任務 API
- `testCanGetSingleTodo()` - 測試獲取單一任務 API
- `testCanUpdateTodo()` - 測試更新任務 API
- `testCanDeleteTodo()` - 測試刪除任務 API
- `testTitleIsRequired()` - 測試標題必填驗證
- `testDescriptionIsRequired()` - 測試描述必填驗證
- `testReturns404ForNonexistentTodo()` - 測試 404 錯誤處理（獲取）
- `testReturns404WhenDeletingNonexistentTodo()` - 測試 404 錯誤處理（刪除）
- `testReturns404WhenUpdatingNonexistentTodo()` - 測試 404 錯誤處理（更新）

## 使用的檔案

### 主要應用檔案

- `app/Models/Todo.php` - Todo 模型
- `app/Http/Controllers/TodoController.php` - Todo 控制器
- `routes/api.php` - API 路由定義
- `database/factories/TodoFactory.php` - Todo 模型工廠
- `database/migrations/2025_09_09_131257_create_todos_table.php` - 資料庫遷移

### 測試配置檔案

- `phpunit.xml` - PHPUnit 測試配置
- `.env.testing` - 測試環境配置
- `tests/TestCase.php` - 基底測試類別

### 測試結果檔案

- `docs/tests/test-report-2025-09-09.md` - 詳細測試報告
- `docs/tests/test-output-raw-2025-09-09.txt` - 原始測試輸出
- `docs/tests/test-files-summary-2025-09-09.md` - 此檔案（測試檔案清單）

## 執行指令

```bash
# 執行所有測試
./vendor/bin/sail artisan test

# 執行特定測試類別
./vendor/bin/sail artisan test tests/Feature/TodoApiTest.php

# 執行特定測試方法
./vendor/bin/sail artisan test --filter testCanCreateTodo
```

## 資料庫連接

### 測試環境

- **連接**: MariaDB
- **主機**: mariadb (Docker 容器)
- **資料庫**: testing
- **使用者**: sail
- **密碼**: password

### 測試資料管理

- 使用 `RefreshDatabase` trait 確保每次測試都有乾淨的資料庫
- 使用 Factory 建立測試資料
- 自動執行遷移建立資料表結構

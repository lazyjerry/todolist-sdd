# GitHub Copilot Instructions for TODO List Laravel Project

## 專案概述

Laravel 12 TODO List API 專案，提供基本的任務管理 CRUD 功能。使用 Laravel Sail + MariaDB 開發環境。

## 技術棧

- **框架**: Laravel 12
- **語言**: PHP 8.3
- **資料庫**: MariaDB 10.11
- **開發環境**: Laravel Sail (Docker)
- **測試**: PHPUnit + Laravel Testing
- **API**: RESTful JSON API

## 程式碼規範

### 註解要求

- **所有類別、方法和重要變數必須有中文註解**
- **複雜邏輯需要中文流程說明**
- **資料庫相關操作需要說明用途**

### 範例格式

```php
/**
 * 任務控制器
 * 處理 TODO 任務的 CRUD 操作
 */
class TodoController extends Controller
{
    /**
     * 獲取所有任務列表
     * 返回 JSON 格式的任務數據
     */
    public function index()
    {
        // 從資料庫獲取所有任務
        $todos = Todo::all();

        // 返回 JSON 響應
        return response()->json([
            'data' => $todos,
            'meta' => ['total' => $todos->count()]
        ]);
    }
}
```

## 資料模型

- **Todo 模型**: id, title (string,255), description (text,1000), completed (boolean), timestamps
- **驗證規則**: title 和 description 必填，completed 可選
- **API 端點**: GET/POST /api/todos, GET/PUT/PATCH/DELETE /api/todos/{id}

## 測試策略

- **TDD 開發**: 先寫測試，後寫實作
- **Feature Tests**: 測試 API 端點完整流程
- **Unit Tests**: 測試個別方法和邏輯
- **Database Tests**: 使用 RefreshDatabase trait

## Laravel 特定指引

### 使用 Laravel 慣例

- 使用 Eloquent ORM 進行資料庫操作
- 使用 Form Request 進行驗證
- 使用 API Resource 格式化回應 (可選)
- 遵循 RESTful 路由慣例

### 目錄結構

```
app/
├── Models/Todo.php              # Eloquent 模型
├── Http/Controllers/TodoController.php  # API 控制器
├── Http/Requests/StoreTodoRequest.php   # 建立驗證
└── Http/Requests/UpdateTodoRequest.php  # 更新驗證

database/
├── migrations/xxxx_create_todos_table.php  # 資料庫遷移
└── seeders/TodoSeeder.php                  # 測試資料

tests/
├── Feature/TodoApiTest.php      # API 功能測試
└── Unit/TodoModelTest.php       # 模型單元測試
```

## 錯誤處理

- 使用 Laravel 標準 HTTP 狀態碼
- 驗證錯誤返回 422 狀態碼
- 資源不存在返回 404 狀態碼
- 伺服器錯誤返回 500 狀態碼

## 開發流程

1. 建立遷移和模型
2. 撰寫失敗的測試 (RED)
3. 實作最少的程式碼讓測試通過 (GREEN)
4. 重構和優化程式碼 (REFACTOR)
5. 重複上述流程

## 最近變更

- 2025-09-09: 初始專案規劃完成
- 2025-09-09: Laravel 12 TODO API 完整實作
- 2025-09-09: Insomnia 5.0 API 集合檔案建立
- 研究文件: /specs/001-todo-list-1/research.md
- 數據模型: /specs/001-todo-list-1/data-model.md
- API 合約: /specs/001-todo-list-1/contracts/api-spec.yaml
- 快速開始: /specs/001-todo-list-1/quickstart.md
- API 測試集合: /docs/insomnia/todo-api-collection.yaml

## API 測試工具

### Insomnia REST Client 支援

專案提供完整的 Insomnia 5.0 格式 API 集合檔案：

- **集合檔案**: `docs/insomnia/todo-api-collection.yaml`
- **文檔說明**: `docs/insomnia/README.md`
- **包含內容**: 10 個預設 API 請求（CRUD + 驗證測試）
- **環境配置**: 開發、測試、生產環境

### 指令模板支援

使用 `.github/instructions/insomnia-api-collection.instructions.md` 和 `.github/prompts/insomnia-api-collection.prompt.md` 來自動生成或更新 Insomnia API 集合檔案。

---

_此文件由 Lazy Jerry 建立於 2025-09-09，請在實作過程中保持更新_

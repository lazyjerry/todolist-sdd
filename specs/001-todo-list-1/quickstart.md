# TODO List API 快速開始指南

## 專案概述

本專案是一個使用 Laravel 12 實現的 TODO List 後端 API，提供基本的任務管理功能，包含新增、查看、更新和刪除任務等 CRUD 操作。

## 環境需求

- Docker 和 Docker Compose
- PHP 8.3+ (如果本地開發)
- Composer (如果本地開發)

## 快速設置

### 1. 建立專案目錄

```bash
# 創建 laravel-todo-example 專案資料夾
mkdir laravel-todo-example
cd laravel-todo-example
```

### 2. 安裝 Laravel 12 (使用 Sail)

```bash
# 使用 Laravel Sail 建立新專案
curl -s "https://laravel.build/laravel-todo-example?with=mariadb,redis,mailpit" | bash

# 進入專案目錄
cd laravel-todo-example

# 啟動 Sail 環境
./vendor/bin/sail up -d
```

### 3. 環境配置

```bash
# 複製環境檔案 (如果需要)
cp .env.example .env

# 生成應用程式金鑰
./vendor/bin/sail artisan key:generate

# 執行資料庫遷移
./vendor/bin/sail artisan migrate
```

## 開發流程

### Phase 1: 建立基礎結構

#### 1.1 建立 Todo 模型和遷移

```bash
# 建立模型和遷移檔案
./vendor/bin/sail artisan make:model Todo -m

# 建立控制器
./vendor/bin/sail artisan make:controller TodoController --api

# 建立表單驗證請求
./vendor/bin/sail artisan make:request StoreTodoRequest
./vendor/bin/sail artisan make:request UpdateTodoRequest
```

#### 1.2 配置資料庫遷移

編輯 `database/migrations/xxxx_create_todos_table.php`：

```php
public function up()
{
    Schema::create('todos', function (Blueprint $table) {
        $table->id();                                    // 主鍵 ID
        $table->string('title');                         // 任務標題
        $table->text('description');                     // 任務描述
        $table->boolean('completed')->default(false);   // 完成狀態
        $table->timestamps();                            // 時間戳

        // 索引
        $table->index('completed');
        $table->index('created_at');
    });
}
```

#### 1.3 執行遷移

```bash
# 執行資料庫遷移
./vendor/bin/sail artisan migrate
```

### Phase 2: API 路由設置

編輯 `routes/api.php`：

```php
use App\Http\Controllers\TodoController;

Route::apiResource('todos', TodoController::class);
```

### Phase 3: 測試驅動開發

#### 3.1 建立功能測試

```bash
# 建立 API 功能測試
./vendor/bin/sail artisan make:test TodoApiTest

# 建立單元測試
./vendor/bin/sail artisan make:test TodoModelTest --unit
```

#### 3.2 執行測試 (RED 階段)

```bash
# 執行所有測試 (應該失敗)
./vendor/bin/sail artisan test

# 執行特定測試
./vendor/bin/sail artisan test --filter TodoApiTest
```

### Phase 4: 實作功能

#### 4.1 實作 Todo 模型

#### 4.2 實作控制器方法

#### 4.3 實作驗證請求

#### 4.4 測試並修正 (GREEN 階段)

### Phase 5: 重構和優化 (REFACTOR 階段)

## API 測試範例

### 使用 curl 測試 API

#### 1. 創建新任務

```bash
curl -X POST http://localhost/api/todos \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "title": "完成專案文件",
    "description": "撰寫技術規格文件和使用者手冊"
  }'
```

#### 2. 獲取所有任務

```bash
curl -X GET http://localhost/api/todos \
  -H "Accept: application/json"
```

#### 3. 獲取特定任務

```bash
curl -X GET http://localhost/api/todos/1 \
  -H "Accept: application/json"
```

#### 4. 更新任務狀態

```bash
curl -X PATCH http://localhost/api/todos/1 \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "completed": true
  }'
```

#### 5. 刪除任務

```bash
curl -X DELETE http://localhost/api/todos/1 \
  -H "Accept: application/json"
```

## 預期回應格式

### 成功回應

```json
{
	"message": "任務創建成功",
	"data": {
		"id": 1,
		"title": "完成專案文件",
		"description": "撰寫技術規格文件和使用者手冊",
		"completed": false,
		"created_at": "2025-09-09T10:00:00.000000Z",
		"updated_at": "2025-09-09T10:00:00.000000Z"
	}
}
```

### 驗證錯誤回應

```json
{
	"message": "驗證失敗",
	"errors": {
		"title": ["標題欄位為必填"],
		"description": ["描述欄位為必填"]
	}
}
```

## 開發工具設置

### 1. 安裝開發依賴

```bash
# 安裝 Laravel Telescope (除錯工具)
./vendor/bin/sail composer require laravel/telescope --dev
./vendor/bin/sail artisan telescope:install
./vendor/bin/sail artisan migrate

# 安裝 Laravel Debugbar
./vendor/bin/sail composer require barryvdh/laravel-debugbar --dev
```

### 2. 程式碼格式化

```bash
# 安裝 PHP CS Fixer
./vendor/bin/sail composer require friendsofphp/php-cs-fixer --dev

# 執行程式碼格式化
./vendor/bin/sail exec laravel.test ./vendor/bin/php-cs-fixer fix
```

## 測試策略

### 1. Feature Tests (功能測試)

- 測試完整的 HTTP 請求/回應週期
- 驗證 API 端點行為
- 測試資料庫互動

### 2. Unit Tests (單元測試)

- 測試個別方法和類別
- 測試業務邏輯
- 測試模型關係和驗證

### 3. 測試資料庫

```bash
# 使用測試資料庫
php artisan config:clear
php artisan test --env=testing
```

## 常用指令

```bash
# 啟動開發環境
./vendor/bin/sail up -d

# 停止開發環境
./vendor/bin/sail down

# 查看日誌
./vendor/bin/sail logs

# 進入容器
./vendor/bin/sail shell

# 執行 Artisan 命令
./vendor/bin/sail artisan [command]

# 執行 Composer 命令
./vendor/bin/sail composer [command]

# 執行測試
./vendor/bin/sail artisan test

# 清除快取
./vendor/bin/sail artisan cache:clear
./vendor/bin/sail artisan config:clear
./vendor/bin/sail artisan route:clear
```

## 下一步

1. 按照測試驅動開發流程實作功能
2. 加入 API 文件產生工具 (如 L5-Swagger)
3. 實作身份驗證和授權 (Laravel Sanctum)
4. 加入 API 速率限制
5. 實作進階功能 (分頁、搜尋、排序)
6. 部署到正式環境

## 故障排除

### 常見問題

1. **Docker 權限問題**

   ```bash
   sudo chown -R $USER:$USER ./laravel-todo-example
   ```

2. **資料庫連線問題**
   檢查 `.env` 檔案中的資料庫設定

3. **Sail 命令無法執行**

   ```bash
   alias sail='./vendor/bin/sail'
   ```

4. **測試失敗**
   確保測試資料庫已正確設置並清空

# TODO List 專案

企業級任務管理 API 系統，採用 Laravel 12 框架實作完整的 RESTful CRUD 功能，包含測試驅動開發、容器化部署和完整文檔。

## 專案簡介

本專案提供生產就緒的 TODO List 管理 API，支援任務的建立、查詢、更新和刪除，具備完整的資料驗證、錯誤處理和 100% 測試覆蓋率。採用 Docker 容器化開發環境，支援快速部署和跨平台開發。

主要亮點：

- 完整的 Laravel 12 後端 API（17 個自動化測試，100% 通過率）
- RESTful API 設計（5 個主要端點，JSON 格式回應）
- 測試驅動開發（PHPUnit + Python 雙重驗證）
- Docker 容器化部署（Laravel Sail + MariaDB）
- 完整的專案文檔（API 規格、測試報告、開發指南）
- 版本控制和變更管理（Git + 自動化文檔生成）

## 系統結構

### 高層級元件架構

```
API 層 (Laravel Controller)
    ↓
業務邏輯層 (Eloquent Model)
    ↓
資料持久化層 (MariaDB)
```

### 目錄結構

```
todo-list/
├── .github/                          # GitHub 相關配置和 AI 指令模板
│   ├── instructions/                 # AI 代理指令模板（changelog、README、API 集合）
│   └── prompts/                      # 標準化 AI 提示詞模板
├── docs/                            # 專案文檔
│   ├── changes/                     # 變更日誌記錄
│   ├── insomnia/                    # API 測試工具集合
│   └── tests/                       # 測試文檔（PHPUnit + Python 測試報告）
├── laravel-todo-api/               # Laravel API 主應用
│   ├── app/                        # 應用程式碼（Controllers、Models、Requests）
│   ├── database/                   # 資料庫相關（migrations、factories、seeders）
│   ├── tests/                      # 測試檔案（Feature + Unit 測試）
│   ├── docker-compose.yml          # Docker 容器編排
│   └── README.md                   # API 專案詳細文檔
├── memory/                         # 專案記憶和狀態管理
├── scripts/                        # 自動化腳本
├── specs/                          # 專案規格文檔
│   └── 001-todo-list-1/           # TODO List 功能規格（API 合約、資料模型）
└── templates/                      # 文檔模板
```

## 安裝與啟動

### 環境需求

- Docker 和 Docker Compose
- Git 版本控制

### 安裝步驟

```bash
# 1. 複製專案
git clone <repository-url>
cd todo-list

# 2. 進入 Laravel API 目錄
cd laravel-todo-api

# 3. 安裝相依套件
docker run --rm -v $(pwd):/app composer install

# 4. 建立環境設定檔
cp .env.example .env

# 5. 啟動 Docker 環境
./vendor/bin/sail up -d

# 6. 產生應用金鑰
./vendor/bin/sail artisan key:generate

# 7. 執行資料庫遷移
./vendor/bin/sail artisan migrate

# 8. 填充示例資料
./vendor/bin/sail artisan db:seed --class=TodoSeeder
```

### 驗證安裝

```bash
# 檢查應用健康狀態
curl http://localhost/up

# 測試 API 端點
curl http://localhost/api/todos -H "Accept: application/json"
```

### 環境變數設定

複製 `.env.example` 至 `.env` 並確認以下設定：

```env
APP_NAME="TODO List API"
APP_ENV=local
APP_KEY=                              # 由 artisan key:generate 產生
APP_DEBUG=true
APP_URL=http://localhost

DB_CONNECTION=mariadb
DB_HOST=mariadb
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=sail
DB_PASSWORD=password
```

## 使用方法

### 常用開發指令

```bash
# 開發環境啟動
./vendor/bin/sail up -d

# 停止開發環境
./vendor/bin/sail down

# 執行測試
./vendor/bin/sail test

# 程式碼格式化
./vendor/bin/sail pint

# 資料庫重置
./vendor/bin/sail artisan migrate:fresh --seed

# 查看即時日誌
./vendor/bin/sail logs -f

# 進入容器 Shell
./vendor/bin/sail shell
```

### API 使用範例

```bash
# 獲取所有任務
curl -X GET http://localhost/api/todos -H "Accept: application/json"

# 建立新任務
curl -X POST http://localhost/api/todos \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"title": "測試任務", "description": "任務描述內容"}'

# 獲取單一任務
curl -X GET http://localhost/api/todos/1 -H "Accept: application/json"

# 更新任務
curl -X PUT http://localhost/api/todos/1 \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"title": "更新的任務", "description": "更新的描述", "completed": true}'

# 刪除任務
curl -X DELETE http://localhost/api/todos/1 -H "Accept: application/json"
```

## 測試

### 測試統計總覽

| 測試工具    | 測試數量 | 成功率   | 執行時間 | 覆蓋範圍       |
| ----------- | -------- | -------- | -------- | -------------- |
| **PHPUnit** | 17       | 100%     | 1.56s    | 框架內部 + API |
| **Python**  | 11       | 100%     | 0.54s    | 外部 API 介面  |
| **總計**    | 28       | **100%** | 2.10s    | 全方位驗證     |

### 自動化測試指令

```bash
# 執行所有測試
./vendor/bin/sail test

# 執行特定測試檔案
./vendor/bin/sail test tests/Feature/TodoApiTest.php

# 執行特定測試方法
./vendor/bin/sail test --filter testCanCreateTodo

# 執行測試並顯示覆蓋率
./vendor/bin/sail test --coverage

# 只執行功能測試
./vendor/bin/sail test tests/Feature/

# 只執行單元測試
./vendor/bin/sail test tests/Unit/
```

### 手動測試腳本

```bash
# 執行 Python API 測試（需要 API 服務運行）
cd docs/tests
python3 python_api_tester.py

# 或指定不同的 API URL
python3 python_api_tester.py http://your-api-url
```

### 測試類型說明

- **功能測試** (tests/Feature/TodoApiTest.php): 10 個 API 端點測試
- **單元測試** (tests/Unit/TodoModelTest.php): 5 個模型測試
- **整合測試** (tests/Feature/ExampleTest.php): 2 個框架測試
- **外部 API 測試** (docs/tests/python_api_tester.py): 11 個跨平台驗證測試

### 測試覆蓋率

- **API 端點覆蓋率**: 100%（5/5 端點）
- **HTTP 方法覆蓋率**: 100%（GET、POST、PUT、DELETE）
- **錯誤處理覆蓋率**: 100%（404、422 錯誤情境）
- **驗證規則覆蓋率**: 100%（必填欄位、資料類型）

### 測試資源連結

- [測試文檔目錄](docs/tests/) - 完整測試報告和工具
- [PHPUnit 測試報告](docs/tests/phpunit-test-report-2025-09-09.md) - 詳細測試分析
- [Python 測試報告](docs/tests/python-api-test-report-2025-09-09.md) - 外部 API 驗證
- [測試總結報告](docs/tests/test-summary-2025-09-09.md) - 綜合測試分析

## 使用情境

### API 整合範例

#### JavaScript 前端整合

```javascript
const apiBase = "http://localhost/api";

// 獲取所有任務
const todos = await fetch(`${apiBase}/todos`, {
	headers: { Accept: "application/json" },
}).then((res) => res.json());

// 建立新任務
const newTodo = await fetch(`${apiBase}/todos`, {
	method: "POST",
	headers: {
		"Content-Type": "application/json",
		Accept: "application/json",
	},
	body: JSON.stringify({
		title: "新任務",
		description: "任務描述",
	}),
}).then((res) => res.json());

// 更新任務狀態
const updatedTodo = await fetch(`${apiBase}/todos/1`, {
	method: "PUT",
	headers: {
		"Content-Type": "application/json",
		Accept: "application/json",
	},
	body: JSON.stringify({
		title: "完成的任務",
		description: "已完成的任務描述",
		completed: true,
	}),
}).then((res) => res.json());
```

#### PHP 客戶端整合

```php
$client = new GuzzleHttp\Client(['base_uri' => 'http://localhost/api/']);

// 建立任務
$response = $client->post('todos', [
    'json' => [
        'title' => '新任務',
        'description' => '任務描述內容'
    ],
    'headers' => ['Accept' => 'application/json']
]);

$todo = json_decode($response->getBody(), true);
```

### 技術棧詳細資訊

#### 後端技術

- **框架**: Laravel 12.x
- **語言**: PHP 8.2+
- **資料庫**: MariaDB 10.11
- **容器化**: Docker + Laravel Sail
- **測試**: PHPUnit 11.5

#### 開發工具

- **版本控制**: Git
- **API 測試**: Insomnia REST Client、curl
- **程式碼品質**: Laravel Pint
- **文檔生成**: Markdown + AI 自動化

### API 測試工具

#### Insomnia REST Client 集合

提供完整的 Insomnia REST Client 匯入檔案，包含所有 API 端點和測試案例：

- **位置**: `docs/insomnia/todo-api-collection.yaml`
- **包含**: 10 個預設請求（CRUD 操作 + 驗證測試）
- **環境**: 開發和生產環境配置

**快速匯入**:

1. 開啟 Insomnia → Import/Export → From File
2. 選擇 `docs/insomnia/todo-api-collection.yaml`
3. 選擇 "development" 環境
4. 執行 "健康檢查" 請求驗證連線

**詳細說明**: 參閱 [docs/insomnia/README.md](docs/insomnia/README.md)

#### 命令列測試範例

```bash
# API 健康檢查
curl -X GET http://localhost/up

# 獲取任務列表
curl -X GET http://localhost/api/todos -H "Accept: application/json"

# 建立任務（JSON 格式）
curl -X POST http://localhost/api/todos \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"title": "新任務", "description": "任務描述內容"}'

# 更新任務狀態
curl -X PUT http://localhost/api/todos/1 \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"title": "完成的任務", "description": "已完成", "completed": true}'
```

## 錯誤排除

### 常見問題與解決方案

#### Docker 相關問題

```bash
# 端口衝突解決
docker ps                                    # 檢查運行中的容器
docker stop <container-name>                 # 停止衝突的容器
./vendor/bin/sail down && ./vendor/bin/sail up -d

# 容器啟動失敗
./vendor/bin/sail down -v                    # 停止並移除 volume
./vendor/bin/sail up -d --build              # 重新建立並啟動容器
```

#### 資料庫問題

```bash
# 資料庫連線錯誤
./vendor/bin/sail artisan migrate:status     # 檢查遷移狀態
./vendor/bin/sail artisan migrate:fresh --seed  # 重置資料庫

# 權限問題
./vendor/bin/sail artisan config:clear       # 清除配置快取
./vendor/bin/sail artisan cache:clear        # 清除應用快取
```

#### 測試相關問題

```bash
# 測試資料庫問題
./vendor/bin/sail artisan migrate --env=testing  # 執行測試環境遷移
./vendor/bin/sail test --recreate-databases      # 重建測試資料庫

# PHP 相依套件問題
./vendor/bin/sail composer install               # 重新安裝相依套件
./vendor/bin/sail composer dump-autoload         # 重新產生自動載入檔案
```

#### API 錯誤訊息對應

- **404 Not Found**: 檢查路由定義 `routes/api.php`
- **422 Unprocessable Entity**: 檢查驗證規則 `app/Http/Requests/`
- **500 Internal Server Error**: 檢查日誌 `./vendor/bin/sail logs`

## 專案文檔

### 核心文檔

- [Laravel API README](laravel-todo-api/README.md) - API 專案詳細文檔
- [API 規格文檔](specs/001-todo-list-1/contracts/api-spec.yaml) - OpenAPI 規格
- [開發計畫](specs/001-todo-list-1/plan.md) - 專案規劃文檔
- [快速開始指南](specs/001-todo-list-1/quickstart.md) - 開發流程說明
- [資料模型設計](specs/001-todo-list-1/data-model.md) - 資料庫設計文檔

### 測試文檔

- [測試文檔目錄](docs/tests/) - 完整測試報告和工具
- [測試總結報告](docs/tests/test-summary-2025-09-09.md) - 綜合測試分析
- [PHPUnit 測試報告](docs/tests/phpunit-test-report-2025-09-09.md) - 詳細測試分析
- [Python 測試報告](docs/tests/python-api-test-report-2025-09-09.md) - 外部 API 驗證

### API 測試工具

- [Insomnia 集合文檔](docs/insomnia/README.md) - REST Client 匯入使用說明
- [Insomnia 集合檔案](docs/insomnia/todo-api-collection.yaml) - 可直接匯入的 API 測試集合

### 變更日誌

- [完整實作變更日誌](docs/changes/feature-laravel-todo-api-complete-implementation.md) - 詳細的實作過程記錄

### AI 代理指令模板

本專案包含完整的 AI 代理指令模板，用於自動化各種開發任務：

| 指令類型          | 檔案路徑                                                       | 描述                                   |
| ----------------- | -------------------------------------------------------------- | -------------------------------------- |
| 變更日誌          | `.github/instructions/changelog.instructions.md`               | 專案變更日誌文件生成規範               |
| README 文檔       | `.github/instructions/copilot-readme.instructions.md`          | 自動產生或更新 README.md 的指令模板    |
| Insomnia API 集合 | `.github/instructions/insomnia-api-collection.instructions.md` | Insomnia 5.0 格式 API 集合檔案生成規範 |

### AI 提示詞模板

專案提供標準化的 AI 提示詞，用於特定開發任務：

| 提示詞類型   | 檔案路徑                                            | 用途                          |
| ------------ | --------------------------------------------------- | ----------------------------- |
| 專案規劃     | `.github/prompts/plan.prompt.md`                    | 功能實作計畫生成              |
| 規格制定     | `.github/prompts/specify.prompt.md`                 | 技術規格文檔撰寫              |
| 任務分解     | `.github/prompts/tasks.prompt.md`                   | 開發任務細分指引              |
| API 集合生成 | `.github/prompts/insomnia-api-collection.prompt.md` | Insomnia 5.0 API 集合生成指引 |

## 授權條款

本專案採用 MIT License 授權條款。詳見 [LICENSE](LICENSE) 檔案。

---

**專案資訊**

- **建立日期**: 2025-09-09
- **當前版本**: 1.0.0
- **維護狀態**: 活躍維護
- **主要語言**: PHP (Laravel 12)
- **文檔語言**: 繁體中文
- **作者**: Lazy Jerry

**技術支援**: 參閱專案文檔或查看測試報告以了解詳細功能說明。

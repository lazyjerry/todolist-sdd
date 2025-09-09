# TODO List 專案

一個完整的任務管理系統專案，包含 Laravel 後端 API 實作、專案規劃文檔和開發流程示例。

## 專案概述

本專案展示了從零開始建立一個現代化 web 應用的完整流程，採用測試驅動開發（TDD）方法，實作了功能完整的 TODO List 管理系統。

### 主要特色

- ✅ **完整的 Laravel 12 後端 API**
- 📋 **RESTful API 設計**
- 🧪 **測試驅動開發（TDD）**
- 🐳 **Docker 容器化部署**
- 📚 **完整的專案文檔**
- 🔄 **版本控制和變更管理**

## 專案結構

```
todo-list/
├── .github/                          # GitHub 相關配置
│   └── instructions/                 # AI 代理指令模板
├── docs/                            # 專案文檔
│   ├── changes/                     # 變更日誌記錄
│   └── insomnia/                    # API 測試工具
├── laravel-todo-api/               # Laravel API 主應用
│   ├── app/                        # 應用程式碼
│   ├── database/                   # 資料庫相關
│   ├── tests/                      # 測試檔案
│   └── README.md                   # API 專案文檔
├── memory/                         # 專案記憶和狀態
├── scripts/                        # 自動化腳本
├── specs/                          # 專案規格文檔
│   └── 001-todo-list-1/           # TODO List 功能規格
└── templates/                      # 文檔模板
```

## 快速開始

### 環境需求

- Docker 和 Docker Compose
- Git 版本控制

### 安裝與啟動

```bash
# 1. 複製專案
git clone <repository-url>
cd todo-list

# 2. 進入 Laravel API 目錄
cd laravel-todo-api

# 3. 啟動 Docker 環境
./vendor/bin/sail up -d

# 4. 執行資料庫遷移
./vendor/bin/sail artisan migrate

# 5. 填充示例資料
./vendor/bin/sail artisan db:seed --class=TodoSeeder

# 6. 執行測試驗證
./vendor/bin/sail test
```

### 驗證安裝

```bash
# 檢查應用健康狀態
curl http://localhost/up

# 測試 API 端點
curl http://localhost/api/todos -H "Accept: application/json"
```

## 功能特點

### API 功能

| 端點              | 方法   | 功能         | 狀態 |
| ----------------- | ------ | ------------ | ---- |
| `/api/todos`      | GET    | 獲取所有任務 | ✅   |
| `/api/todos`      | POST   | 建立新任務   | ✅   |
| `/api/todos/{id}` | GET    | 獲取單一任務 | ✅   |
| `/api/todos/{id}` | PUT    | 更新任務     | ✅   |
| `/api/todos/{id}` | DELETE | 刪除任務     | ✅   |

### 開發特色

- **測試驅動開發**: 15 個測試案例，100% 通過率
- **完整驗證**: 表單驗證和錯誤處理
- **資料庫設計**: 包含索引優化的資料庫結構
- **容器化**: 使用 Laravel Sail 的 Docker 環境
- **假資料生成**: 模型工廠和資料填充器

## 技術棧

### 後端技術

- **框架**: Laravel 12.28.1
- **語言**: PHP 8.4
- **資料庫**: MariaDB 10.11
- **容器化**: Docker + Laravel Sail
- **測試**: PHPUnit 11.5

### 開發工具

- **版本控制**: Git
- **API 測試**: curl / Postman
- **程式碼品質**: Laravel Pint
- **文檔生成**: Markdown

## 測試狀態

### 測試統計

- **總測試數**: 15 個測試
- **斷言數**: 65 個斷言
- **通過率**: 100% ✅
- **覆蓋範圍**: API 端點、模型、驗證

### 測試分類

- **功能測試**: 8 個 API 端點測試
- **單元測試**: 5 個模型測試
- **系統測試**: 2 個預設測試

## 專案文檔

### 核心文檔

- [Laravel API README](laravel-todo-api/README.md) - API 專案詳細文檔
- [API 規格文檔](specs/001-todo-list-1/contracts/api-spec.yaml) - OpenAPI 規格
- [開發計畫](specs/001-todo-list-1/plan.md) - 專案規劃文檔

### API 測試工具

- [Insomnia 集合文檔](docs/insomnia/README.md) - REST Client 匯入使用說明
- [Insomnia 集合檔案](docs/insomnia/todo-api-collection.yaml) - 可直接匯入的 API 測試集合

### 變更日誌

- [完整實作變更日誌](docs/changes/feature-laravel-todo-api-complete-implementation.md) - 詳細的實作過程記錄

## 開發指南與模板

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

### 開發指南

- [快速開始指南](specs/001-todo-list-1/quickstart.md) - 開發流程說明
- [資料模型設計](specs/001-todo-list-1/data-model.md) - 資料庫設計文檔

## 使用情境

### API 整合範例

```javascript
// JavaScript 前端整合
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
```

### API 測試工具

#### Insomnia REST Client 集合

我們提供了完整的 Insomnia REST Client 匯入檔案，包含所有 API 端點和測試案例：

- **位置**: `docs/insomnia/todo-api-collection.yaml`
- **包含**: 10 個預設請求（CRUD 操作 + 驗證測試）
- **環境**: 開發和生產環境配置

**快速匯入**:

1. 開啟 Insomnia → Import/Export → From File
2. 選擇 `docs/insomnia/todo-api-collection.yaml`
3. 選擇 "development" 環境
4. 執行 "健康檢查" 請求驗證連線

**詳細說明**: 參閱 [docs/insomnia/README.md](docs/insomnia/README.md)

#### 命令列測試

```bash
# 快速 API 測試指令
curl -X GET http://localhost/api/todos -H "Accept: application/json"
curl -X POST http://localhost/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "測試任務", "description": "描述內容"}'
```

### 開發工作流程

1. **需求分析** → 撰寫規格文檔
2. **測試設計** → 建立測試案例
3. **TDD 開發** → RED → GREEN → REFACTOR
4. **文檔更新** → 記錄變更日誌
5. **驗證部署** → 確認功能正常

## 常見問題

### 端口衝突

```bash
# 停止衝突的容器
docker ps
docker stop <container-name>
./vendor/bin/sail down && ./vendor/bin/sail up -d
```

### 資料庫問題

```bash
# 重置資料庫
./vendor/bin/sail artisan migrate:fresh --seed
```

### 測試失敗

```bash
# 重新執行遷移
./vendor/bin/sail artisan migrate --env=testing
./vendor/bin/sail test
```

## 未來規劃

### 短期目標

- [ ] 實作用戶認證系統
- [ ] 新增任務分類功能
- [ ] 實作搜尋和篩選
- [ ] 開發前端 SPA 應用

### 長期願景

- [ ] 即時協作功能
- [ ] 行動應用開發
- [ ] 微服務架構演進
- [ ] 效能監控系統

## 貢獻指南

### 開發流程

1. Fork 專案
2. 建立功能分支
3. 撰寫測試案例
4. 實作功能代碼
5. 執行測試驗證
6. 更新文檔
7. 提交 Pull Request

### 程式碼規範

- 遵循 Laravel 編碼標準
- 所有功能必須包含測試
- 提交訊息使用繁體中文
- 重要變更需建立變更日誌

## 授權條款

本專案採用 MIT License 授權條款。

---

## 專案資訊

- **建立日期**: 2025-09-09
- **當前版本**: 1.0.0
- **維護狀態**: ✅ 活躍維護
- **語言**: 繁體中文

**開發團隊**: Laravel TODO List 專案組

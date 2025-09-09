# 研究報告：TODO List Backend API

## Laravel 12 + Sail + MariaDB 技術決策

### Decision: Laravel 12 with Sail Development Environment

**Rationale**:

- Laravel 12 是最新穩定版本，提供現代 PHP 開發體驗
- Laravel Sail 提供完整的 Docker 開發環境，簡化設置過程
- 內建完善的 ORM (Eloquent)、路由、驗證和測試工具
- 強大的 Artisan CLI 工具

**Alternatives considered**:

- Symfony: 更複雜的配置，學習曲線較陡
- CodeIgniter: 功能較少，不適合現代開發
- 原生 PHP: 開發效率低，缺乏框架支援

### Decision: MariaDB as Database

**Rationale**:

- MariaDB 是 MySQL 的開源分支，完全相容 MySQL
- Laravel Sail 原生支援 MariaDB
- 優秀的效能和穩定性
- 社群支援良好

**Alternatives considered**:

- MySQL: 功能相似，但 MariaDB 更開源友善
- PostgreSQL: 功能強大但對此專案可能過於複雜
- SQLite: 適合開發但不適合正式環境

### Decision: PHPUnit + Laravel Testing for Testing Strategy

**Rationale**:

- Laravel 內建 PHPUnit 整合
- 提供 Feature Tests 和 Unit Tests 兩種測試類型
- 支援資料庫測試和 HTTP 測試
- 優秀的測試資料庫管理 (RefreshDatabase trait)

**Alternatives considered**:

- Pest PHP: 較新但 PHPUnit 更成熟穩定
- Codeception: 過於複雜，不需要 BDD 功能

### Decision: 中文註解和文件標準

**Rationale**:

- 提高程式碼可讀性和維護性
- 符合本地化開發需求
- 便於團隊協作和知識傳承

**實作方式**:

- 所有類別、方法和重要變數加上中文註解
- 程式碼邏輯流程使用中文說明
- README 和文件使用中文撰寫

### Decision: 標準 REST API 設計模式

**Rationale**:

- 遵循 RESTful 設計原則
- 使用標準 HTTP 方法和狀態碼
- JSON 格式數據交換
- 清晰的 URL 結構設計

**API 端點規劃**:

- GET /api/todos - 獲取所有任務
- POST /api/todos - 創建新任務
- GET /api/todos/{id} - 獲取特定任務
- PUT/PATCH /api/todos/{id} - 更新任務
- DELETE /api/todos/{id} - 刪除任務

### Decision: Laravel 標準專案結構

**Rationale**:

- 遵循 Laravel 最佳實踐
- 便於其他 Laravel 開發者理解
- 利用框架提供的自動載入和依賴注入
- 標準化的目錄結構

**目錄規劃**:

- app/Models/ - Eloquent 模型
- app/Http/Controllers/ - API 控制器
- app/Http/Requests/ - 表單驗證請求
- database/migrations/ - 資料庫遷移檔案
- tests/Feature/ - API 功能測試
- tests/Unit/ - 單元測試

## 未解決問題處理

原規格中的 [NEEDS CLARIFICATION] 項目解決方案：

1. **任務狀態值規範**:

   - 決定使用簡單的 boolean completed 欄位
   - 0 = 未完成, 1 = 已完成
   - 可在未來擴展為更複雜的狀態系統

2. **身份驗證機制**:

   - 此版本暫不實作身份驗證
   - 專注於基本 CRUD 功能
   - 可在未來加入 Laravel Sanctum 或 Passport

3. **資料驗證規則**:
   - title: required, string, max:255
   - description: required, string, max:1000
   - completed: boolean, default:false

## 技術考量

### 效能考量

- 使用 Eloquent ORM 平衡開發效率和效能
- 合理的資料庫索引設計
- 適當的快取策略 (Laravel Cache)

### 安全考量

- Laravel 內建 CSRF 保護
- Mass Assignment 保護
- SQL Injection 防護 (Eloquent ORM)
- 輸入驗證和清理

### 可維護性

- 遵循 SOLID 原則
- 清晰的程式碼結構
- 完整的測試覆蓋率
- 詳細的中文註解

## 開發環境設定

### Laravel Sail 配置

- Docker + Docker Compose
- PHP 8.3
- MariaDB 10.11
- Redis (快取和會話)
- Mailpit (郵件測試)

### 開發工具

- Laravel Telescope (除錯和分析)
- Laravel Debugbar (開發除錯)
- PHP CS Fixer (程式碼格式化)

# Insomnia REST API 匯入說明

本目錄包含 Laravel TODO List API 的 Insomnia REST Client 匯入檔案。

## 檔案說明

### `todo-api-collection.yaml`

- **格式**: Insomnia Collection v5.0
- **內容**: 完整的 TODO API 端點集合
- **環境**: 包含開發和生產環境配置

## 匯入步驟

### 1. 開啟 Insomnia

確保您已安裝 [Insomnia REST Client](https://insomnia.rest/download)

### 2. 匯入集合

1. 開啟 Insomnia 應用程式
2. 點擊 **Import/Export** 按鈕
3. 選擇 **Import Data** → **From File**
4. 選擇 `todo-api-collection.yaml` 檔案
5. 確認匯入設定並點擊 **Import**

### 3. 設定環境變數

匯入後會自動建立三個環境：

#### Development 環境 (本地開發)

- `base_url`: `http://localhost`
- `todo_id`: `1`

#### Staging 環境 (測試環境)

- `base_url`: `https://staging-api.your-domain.com`
- `todo_id`: `1`

#### Production 環境 (正式環境)

- `base_url`: `https://api.your-domain.com`
- `todo_id`: `1`

### 4. 選擇環境

在 Insomnia 右上角選擇 **development** 環境進行本地測試。

## API 端點說明

### 基本 CRUD 操作

| 請求名稱         | 方法   | 端點              | 說明               |
| ---------------- | ------ | ----------------- | ------------------ |
| 獲取所有任務     | GET    | `/api/todos`      | 取得所有 TODO 任務 |
| 建立新任務       | POST   | `/api/todos`      | 建立新的 TODO 任務 |
| 獲取單一任務     | GET    | `/api/todos/{id}` | 取得指定 ID 的任務 |
| 更新任務         | PUT    | `/api/todos/{id}` | 完整更新任務       |
| 更新任務 (PATCH) | PATCH  | `/api/todos/{id}` | 部分更新任務       |
| 刪除任務         | DELETE | `/api/todos/{id}` | 刪除指定任務       |

### 系統檢查

| 請求名稱 | 方法 | 端點          | 說明              |
| -------- | ---- | ------------- | ----------------- |
| 健康檢查 | GET  | `/api/health` | 檢查 API 服務狀態 |

### 測試和驗證

| 請求名稱            | 說明                     |
| ------------------- | ------------------------ |
| 驗證錯誤 - 缺少標題 | 測試缺少必填欄位的驗證   |
| 驗證錯誤 - 缺少描述 | 測試缺少必填欄位的驗證   |
| 404 錯誤測試        | 測試不存在資源的錯誤處理 |

## 使用方式

### 1. 確保 Laravel API 正在運行

```bash
cd laravel-todo-api
./vendor/bin/sail up -d
```

### 2. 執行請求

1. 先執行 **健康檢查** 確認 API 可用
2. 執行 **獲取所有任務** 查看現有任務
3. 執行 **建立新任務** 新增任務
4. 使用新建立的任務 ID 測試其他操作

### 3. 環境變數使用

- 請求 URL 中的 `{{ _.base_url }}` 會自動替換為環境變數
- `{{ _.todo_id }}` 用於指定要操作的任務 ID
- 可在環境設定中修改這些變數值

## 預期回應格式

### 成功回應範例

#### 獲取所有任務

```json
{
	"data": [
		{
			"id": 1,
			"title": "完成專案文件",
			"description": "撰寫完整的 API 文檔和使用說明",
			"completed": false,
			"created_at": "2025-09-09T13:18:11.000000Z",
			"updated_at": "2025-09-09T13:18:11.000000Z"
		}
	],
	"meta": {
		"total": 1
	}
}
```

#### 建立新任務

```json
{
	"data": {
		"id": 1,
		"title": "完成專案文件",
		"description": "撰寫完整的 API 文檔和使用說明",
		"completed": false,
		"created_at": "2025-09-09T13:18:11.000000Z",
		"updated_at": "2025-09-09T13:18:11.000000Z"
	}
}
```

### 錯誤回應範例

#### 驗證錯誤 (422)

```json
{
	"message": "The title field is required. (and 1 more error)",
	"errors": {
		"title": ["任務標題為必填項目"],
		"description": ["任務描述為必填項目"]
	}
}
```

#### 資源不存在 (404)

```json
{
	"message": "找不到請求的資源",
	"error": "resource_not_found"
}
```

#### 資源不存在 (404)

```json
{
	"message": "No query results for model [App\\Models\\Todo] 999"
}
```

## 疑難排解

### 常見問題

1. **連線失敗**

   - 確認 Laravel Sail 容器正在運行
   - 檢查 `base_url` 環境變數是否正確

2. **404 錯誤**

   - 確認 API 路由已正確設定
   - 檢查 `routes/api.php` 檔案

3. **驗證錯誤**
   - 確認請求包含必要的 `title` 和 `description` 欄位
   - 檢查 Content-Type 標頭為 `application/json`

### 除錯技巧

1. 使用 **健康檢查** 請求驗證 API 可用性
2. 查看 Laravel 日誌：`./vendor/bin/sail artisan log:tail`
3. 檢查請求和回應的 HTTP 狀態碼
4. 確認請求標頭包含正確的 `Accept` 和 `Content-Type`

## 測試執行建議序列

為確保完整測試覆蓋，建議按以下順序執行請求：

1. **健康檢查** - 確認 API 服務正常運行
2. **獲取所有任務** - 查看當前任務狀態
3. **建立新任務** - 測試正常建立流程
4. **獲取單一任務** - 使用剛建立的任務 ID
5. **更新任務 (PATCH)** - 測試部分更新
6. **更新任務 (PUT)** - 測試完整更新
7. **驗證錯誤測試** - 測試錯誤處理
8. **404 錯誤測試** - 測試不存在資源
9. **刪除任務** - 最後測試刪除功能

## 故障排除

### 常見問題

#### 連接失敗

- 確認 Laravel Sail 正在運行：`./vendor/bin/sail up -d`
- 檢查端口是否被占用：`docker ps`
- 確認環境變數 `base_url` 設定正確

#### 驗證錯誤

- 檢查請求 body 格式是否為有效 JSON
- 確認 Content-Type header 設定為 `application/json`
- 檢查必填欄位是否都有提供

#### 404 錯誤

- 確認 API 路由是否正確：`/api/todos`
- 檢查任務 ID 是否存在
- 確認使用正確的 HTTP 方法

## 更新日誌

- **2025-09-09**: 初始版本建立
  - 包含完整的 CRUD 操作
  - 新增驗證錯誤測試
  - 支援開發、測試和生產環境
  - 添加健康檢查端點

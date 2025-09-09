# 數據模型設計：TODO List API

## 實體定義

### Todo 任務實體

**目的**: 代表一個待辦事項，包含基本資訊和完成狀態

**屬性**:

- `id`: 主鍵，自動遞增整數 (Primary Key, Auto Increment)
- `title`: 任務標題，必填，最大 255 字元 (Required, String, Max: 255)
- `description`: 任務詳細描述，必填，最大 1000 字元 (Required, Text, Max: 1000)
- `completed`: 完成狀態，布林值，預設 false (Boolean, Default: false)
- `created_at`: 建立時間，自動時間戳 (Timestamp, Auto)
- `updated_at`: 更新時間，自動時間戳 (Timestamp, Auto)

**Laravel Migration 結構**:

```php
Schema::create('todos', function (Blueprint $table) {
    $table->id();                                    // 主鍵 ID
    $table->string('title');                         // 任務標題
    $table->text('description');                     // 任務描述
    $table->boolean('completed')->default(false);   // 完成狀態
    $table->timestamps();                            // created_at, updated_at
});
```

**Laravel Model 屬性**:

```php
class Todo extends Model
{
    // 可大量賦值的欄位
    protected $fillable = [
        'title',        // 任務標題
        'description',  // 任務描述
        'completed'     // 完成狀態
    ];

    // 欄位型別轉換
    protected $casts = [
        'completed' => 'boolean',  // 確保 completed 為布林值
    ];
}
```

## 驗證規則

### 創建任務驗證

```php
[
    'title' => 'required|string|max:255',           // 標題必填，字串，最大255字元
    'description' => 'required|string|max:1000',   // 描述必填，字串，最大1000字元
    'completed' => 'boolean'                        // 完成狀態為布林值（可選）
]
```

### 更新任務驗證

```php
[
    'title' => 'sometimes|required|string|max:255',        // 標題可選更新，但若提供則必填
    'description' => 'sometimes|required|string|max:1000', // 描述可選更新，但若提供則必填
    'completed' => 'sometimes|boolean'                     // 完成狀態可選更新
]
```

## 狀態轉換

### 任務狀態流程

```
[新建] → completed: false (未完成)
  ↓
[使用者操作] → completed: true (已完成)
  ↓
[使用者操作] → completed: false (重新開啟)
```

**狀態驗證**:

- `completed` 只能是 `true` 或 `false`
- 預設狀態為 `false` (未完成)
- 可以在已完成和未完成之間自由切換

## 資料庫索引策略

### 建議索引

1. **主鍵索引**: `id` (自動建立)
2. **狀態索引**: `completed` (支援按完成狀態查詢)
3. **時間索引**: `created_at` (支援按建立時間排序)

```php
// 在 migration 中加入索引
$table->index('completed');     // 完成狀態索引
$table->index('created_at');    // 建立時間索引
```

## 關聯關係

### 當前版本

- **無關聯**: 此版本為簡化版本，不包含使用者關聯
- **獨立實體**: 每個 Todo 為獨立實體

### 未來擴展可能性

- **使用者關聯**: `belongs_to User` (多對一關係)
- **分類關聯**: `belongs_to Category` (多對一關係)
- **標籤關聯**: `belongs_to_many Tag` (多對多關係)

## JSON API 回應格式

### 單一任務格式

```json
{
	"id": 1,
	"title": "完成專案文件",
	"description": "撰寫技術規格文件和使用者手冊",
	"completed": false,
	"created_at": "2025-09-09T10:00:00.000000Z",
	"updated_at": "2025-09-09T10:00:00.000000Z"
}
```

### 任務列表格式

```json
{
	"data": [
		{
			"id": 1,
			"title": "完成專案文件",
			"description": "撰寫技術規格文件和使用者手冊",
			"completed": false,
			"created_at": "2025-09-09T10:00:00.000000Z",
			"updated_at": "2025-09-09T10:00:00.000000Z"
		}
	],
	"meta": {
		"total": 1
	}
}
```

## 錯誤處理

### 驗證錯誤格式

```json
{
	"message": "驗證失敗",
	"errors": {
		"title": ["標題欄位為必填"],
		"description": ["描述欄位為必填"]
	}
}
```

### 資源不存在錯誤

```json
{
	"message": "找不到指定的任務",
	"error": "Resource not found"
}
```

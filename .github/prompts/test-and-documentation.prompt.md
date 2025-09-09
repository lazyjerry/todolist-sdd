# Execute Comprehensive Testing and Documentation

Execute a complete testing workflow including PHPUnit internal tests and Python external API tests, then generate standardized test documentation organized by date.

This prompt creates a comprehensive testing and documentation pipeline that validates both internal framework functionality and external API behavior.

---

## Context Analysis

1. **Identify the Laravel project structure** and existing test files
2. **Analyze current test coverage** and testing patterns
3. **Determine API endpoints** that need external validation
4. **Review existing test documentation** structure and format
5. **Check Docker/Sail environment** status and configuration

---

## Testing Execution Steps

### Phase 1: Environment Preparation

```bash
# Verify Laravel Sail is running
cd laravel-todo-api
./vendor/bin/sail ps

# Start services if not running
./vendor/bin/sail up -d

# Verify database and services are healthy
./vendor/bin/sail artisan migrate:status
```

### Phase 2: PHPUnit Internal Testing

```bash
# Execute comprehensive PHPUnit tests
./vendor/bin/sail artisan test

# Generate detailed test report with coverage
./vendor/bin/sail test --coverage

# Get structured test output
./vendor/bin/sail phpunit --testdox
```

**Collect the following data:**

- Total test count and execution time
- Pass/fail statistics for each test
- Test method names and descriptions
- File locations and test categories
- Code coverage percentages
- Any warnings or deprecation notices

### Phase 3: Python External API Testing

**Create/Update Python Test Script:**

- HTTP client using `requests` library
- Test same logical scenarios as PHPUnit
- Proper request headers (Content-Type, Accept)
- Test data cleanup and isolation
- JSON response validation
- Error handling and status code verification

**Execute External Tests:**

```bash
cd docs/tests/YYYY-MM-DD-XX
python3 python_api_tester.py
```

**Collect the following data:**

- API connectivity and response times
- CRUD operation validation
- Input validation testing
- Error handling verification
- JSON data format validation
- Comparison with PHPUnit results

---

## Documentation Generation Requirements

### 1. Create Date-Organized Folder Structure

```
docs/tests/YYYY-MM-DD-XX/
├── README.md                              # Execution summary
├── comprehensive-test-report.md           # 📊 Main report (recommended)
├── phpunit-test-report.md                 # PHPUnit detailed report
├── python-api-test-report.md             # Python external test report
├── python-api-test-report-YYYY-MM-DD.json # Raw test data
└── python_api_tester.py                  # Test script
```

### 2. Generate Comprehensive Test Report

**Required Sections:**

- **執行摘要**: Overall testing summary
- **整體測試統計**: Statistics table with test counts, pass rates, execution times
- **測試覆蓋範圍**: Functional and technical coverage analysis
- **詳細測試分析**: Breakdown of PHPUnit and Python tests
- **程式碼品質分析**: Coverage report and quality assessment
- **發現的問題與解決**: Issues found and resolutions
- **效能分析**: Performance metrics and timing analysis
- **建議與後續行動**: Recommendations for improvement

**Statistics Table Format:**

```markdown
| 測試類型        | 測試數量 | 通過數量 | 失敗數量 | 通過率 | 執行時間 |
| --------------- | -------- | -------- | -------- | ------ | -------- |
| PHPUnit 測試    | X        | X        | X        | X%     | Xs       |
| Python 外部測試 | X        | X        | X        | X%     | Xs       |
| **總計**        | **X**    | **X**    | **X**    | **X%** | **Xs**   |
```

### 3. Generate PHPUnit Detailed Report

**Required Content:**

- **測試統計結果**: Counts, pass rates, timing, memory usage
- **測試分類統計**: Feature Tests vs Unit Tests breakdown
- **詳細測試結果**: Individual test method results table
- **程式碼覆蓋率報告**: Class-by-class coverage analysis
- **警告和建議**: PHPUnit warnings and improvement suggestions
- **測試執行環境**: Docker container status and configuration

**Test Method Table Format:**

```markdown
| 測試方法         | 狀態   | 描述             | 執行時間 |
| ---------------- | ------ | ---------------- | -------- |
| `testMethodName` | ✓ PASS | Test description | 0.XXs    |
```

### 4. Generate Python External Test Report

**Required Content:**

- **測試統計結果**: API test counts, success rates, response times
- **測試分類統計**: Connectivity, CRUD, Validation, Error Handling
- **詳細測試結果**: Individual API test results
- **與 PHPUnit 測試對比**: Comparison analysis between internal and external tests
- **技術實作細節**: Request configuration, data cleanup, error handling
- **發現的問題與修正**: Issues discovered and resolution process

### 5. Generate Folder README

**Required Content:**

- **執行資訊**: Execution time, version, test types
- **檔案說明**: File list table with descriptions
- **測試結果摘要**: Key statistics and outcomes
- **版本改進**: Improvements compared to previous versions (if applicable)
- **推薦閱讀順序**: Guide for users on how to read the reports

---

## Quality Standards

### Documentation Quality

- ✅ **Complete**: All required sections included
- ✅ **Accurate**: Statistics and analysis are correct
- ✅ **Readable**: Clear headings and formatting
- ✅ **Consistent**: Follows standardized format
- ✅ **Useful**: Provides valuable insights and recommendations

### Test Coverage

- ✅ **Functional Complete**: All CRUD operations tested
- ✅ **Validation Rules**: All validation scenarios covered
- ✅ **Error Handling**: Various error conditions tested
- ✅ **Boundary Conditions**: Edge cases included
- ✅ **Performance**: Execution times recorded

### Technical Requirements

- ✅ **Dual Validation**: PHPUnit + Python external tests
- ✅ **Automation**: Repeatable test processes
- ✅ **Standardization**: Uniform report format and structure
- ✅ **Traceability**: Complete execution records and history
- ✅ **Comparison**: Support for cross-version analysis

---

## Execution Template

### Step 1: Execute PHPUnit Tests

```
請使用 PHPUnit 執行所有已列出測試並且將測試內容，包括測試方法、使用的檔案與結果等詳細列出，於開頭列出統計結果。放在 /docs/tests 資料夾中。
```

### Step 2: Execute Python External Tests

```
結束後請使用外部 python 方法相同邏輯執行一遍測試結果，同樣放在 /docs/tests 資料夾中作為參考。
```

### Step 3: Organize Documentation

```
最後在 /docs/tests 裡面整理好，以單一日期的時間戳（Y-m-d）分類獨立資料夾。
```

---

## Folder Naming Convention

- **Date Format**: `YYYY-MM-DD-XX`
- **Sequential Numbering**: Use `-01`, `-02`, `-03` for multiple executions on same date
- **Example**: `2025-09-09-01`, `2025-09-09-02`

---

## File Maintenance

### Update Main README

After generating new test documentation:

1. Update the main `/docs/tests/README.md`
2. Add new folder to file structure diagram
3. Update latest test results summary
4. Mark recommended version with ⭐️

### Version Comparison

Include comparison tables showing:

- Execution timeline
- Test count improvements
- Issue resolutions
- Feature enhancements

---

## Success Criteria

✅ **All tests executed successfully**  
✅ **Comprehensive documentation generated**  
✅ **Files organized by date in separate folders**  
✅ **Statistics prominently displayed at report beginning**  
✅ **Both PHPUnit and Python test results included**  
✅ **Main README.md updated with new execution**  
✅ **Clear folder structure with descriptive filenames**  
✅ **Detailed analysis and recommendations provided**

---

_This prompt ensures comprehensive testing validation and documentation generation following established project standards_

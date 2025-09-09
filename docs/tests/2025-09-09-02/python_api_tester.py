#!/usr/bin/env python3
"""
TODO List API 外部測試腳本
使用 Python requests 模組對 Laravel API 進行外部測試
模擬 PHPUnit 測試的相同邏輯和場景
"""

import requests
import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
import sys

class TodoApiTester:
    """Todo API 外部測試器"""
    
    def __init__(self, base_url: str = "http://localhost"):
        self.base_url = base_url.rstrip('/')
        self.api_base = f"{self.base_url}/api/todos"
        self.test_results = []
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.start_time = None
        self.end_time = None
        # 設定請求標頭
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
    def log_test(self, test_name: str, status: str, message: str = "", execution_time: float = 0.0):
        """記錄測試結果"""
        self.test_results.append({
            'test_name': test_name,
            'status': status,
            'message': message,
            'execution_time': execution_time,
            'timestamp': datetime.now().isoformat()
        })
        self.total_tests += 1
        if status == 'PASS':
            self.passed_tests += 1
            print(f"✓ {test_name} - {message} ({execution_time:.3f}s)")
        else:
            self.failed_tests += 1
            print(f"✗ {test_name} - {message} ({execution_time:.3f}s)")
    
    def test_can_get_all_todos(self) -> bool:
        """測試獲取所有任務列表"""
        test_start = time.time()
        try:
            # 先建立測試數據
            test_todos = [
                {"title": "測試任務1", "description": "測試描述1"},
                {"title": "測試任務2", "description": "測試描述2"},
                {"title": "測試任務3", "description": "測試描述3"}
            ]
            
            created_ids = []
            for todo_data in test_todos:
                response = requests.post(self.api_base, json=todo_data, headers=self.headers)
                if response.status_code == 201:
                    created_ids.append(response.json()['data']['id'])
            
            # 測試獲取所有任務
            response = requests.get(self.api_base, headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and 'meta' in data and 'total' in data['meta']:
                    # 清理測試數據
                    for todo_id in created_ids:
                        requests.delete(f"{self.api_base}/{todo_id}", headers=self.headers)
                    
                    self.log_test("test_can_get_all_todos", "PASS", 
                                f"成功獲取任務列表，包含 {len(data['data'])} 個任務", execution_time)
                    return True
            
            self.log_test("test_can_get_all_todos", "FAIL", 
                        f"回應格式不正確或狀態碼錯誤: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_can_get_all_todos", "FAIL", f"請求異常: {str(e)}", execution_time)
            return False
    
    def test_can_create_todo(self) -> Optional[int]:
        """測試建立新任務"""
        test_start = time.time()
        try:
            todo_data = {
                "title": "完成專案文件",
                "description": "撰寫完整的 API 文檔和使用說明"
            }
            
            response = requests.post(self.api_base, json=todo_data, headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 201:
                data = response.json()
                if 'data' in data and 'id' in data['data']:
                    todo_id = data['data']['id']
                    self.log_test("test_can_create_todo", "PASS", 
                                f"成功建立任務 ID: {todo_id}", execution_time)
                    return todo_id
            
            self.log_test("test_can_create_todo", "FAIL", 
                        f"建立失敗，狀態碼: {response.status_code}", execution_time)
            return None
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_can_create_todo", "FAIL", f"請求異常: {str(e)}", execution_time)
            return None
    
    def test_can_get_single_todo(self, todo_id: int) -> bool:
        """測試獲取單一任務"""
        test_start = time.time()
        try:
            response = requests.get(f"{self.api_base}/{todo_id}", headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and 'id' in data['data'] and data['data']['id'] == todo_id:
                    self.log_test("test_can_get_single_todo", "PASS", 
                                f"成功獲取任務 ID: {todo_id}", execution_time)
                    return True
            
            self.log_test("test_can_get_single_todo", "FAIL", 
                        f"獲取失敗，狀態碼: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_can_get_single_todo", "FAIL", f"請求異常: {str(e)}", execution_time)
            return False
    
    def test_can_update_todo(self, todo_id: int) -> bool:
        """測試更新任務"""
        test_start = time.time()
        try:
            update_data = {
                "title": "更新後的標題",
                "description": "更新後的描述",
                "completed": True
            }
            
            response = requests.put(f"{self.api_base}/{todo_id}", json=update_data, headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    updated_todo = data['data']
                    if (updated_todo['title'] == update_data['title'] and 
                        updated_todo['description'] == update_data['description'] and
                        updated_todo['completed'] == update_data['completed']):
                        self.log_test("test_can_update_todo", "PASS", 
                                    f"成功更新任務 ID: {todo_id}", execution_time)
                        return True
            
            self.log_test("test_can_update_todo", "FAIL", 
                        f"更新失敗，狀態碼: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_can_update_todo", "FAIL", f"請求異常: {str(e)}", execution_time)
            return False
    
    def test_can_delete_todo(self, todo_id: int) -> bool:
        """測試刪除任務"""
        test_start = time.time()
        try:
            response = requests.delete(f"{self.api_base}/{todo_id}", headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 204:
                # 驗證任務已被刪除
                check_response = requests.get(f"{self.api_base}/{todo_id}", headers=self.headers)
                if check_response.status_code == 404:
                    self.log_test("test_can_delete_todo", "PASS", 
                                f"成功刪除任務 ID: {todo_id}", execution_time)
                    return True
            
            self.log_test("test_can_delete_todo", "FAIL", 
                        f"刪除失敗，狀態碼: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_can_delete_todo", "FAIL", f"請求異常: {str(e)}", execution_time)
            return False
    
    def test_title_is_required(self) -> bool:
        """測試驗證規則 - 標題必填"""
        test_start = time.time()
        try:
            todo_data = {"description": "只有描述沒有標題"}
            
            response = requests.post(self.api_base, json=todo_data, headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 422:
                data = response.json()
                if 'errors' in data and 'title' in data['errors']:
                    self.log_test("test_title_is_required", "PASS", 
                                "正確驗證標題必填規則", execution_time)
                    return True
            
            self.log_test("test_title_is_required", "FAIL", 
                        f"驗證失敗，狀態碼: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_title_is_required", "FAIL", f"請求異常: {str(e)}", execution_time)
            return False
    
    def test_description_is_required(self) -> bool:
        """測試驗證規則 - 描述必填"""
        test_start = time.time()
        try:
            todo_data = {"title": "只有標題沒有描述"}
            
            response = requests.post(self.api_base, json=todo_data, headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 422:
                data = response.json()
                if 'errors' in data and 'description' in data['errors']:
                    self.log_test("test_description_is_required", "PASS", 
                                "正確驗證描述必填規則", execution_time)
                    return True
            
            self.log_test("test_description_is_required", "FAIL", 
                        f"驗證失敗，狀態碼: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_description_is_required", "FAIL", f"請求異常: {str(e)}", execution_time)
            return False
    
    def test_returns_404_for_nonexistent_todo(self) -> bool:
        """測試 404 錯誤 - 任務不存在"""
        test_start = time.time()
        try:
            response = requests.get(f"{self.api_base}/999999", headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 404:
                self.log_test("test_returns_404_for_nonexistent_todo", "PASS", 
                            "正確返回 404 狀態碼", execution_time)
                return True
            
            self.log_test("test_returns_404_for_nonexistent_todo", "FAIL", 
                        f"狀態碼不正確: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_returns_404_for_nonexistent_todo", "FAIL", f"請求異常: {str(e)}", execution_time)
            return False
    
    def test_returns_404_when_deleting_nonexistent_todo(self) -> bool:
        """測試 404 錯誤 - 刪除不存在的任務"""
        test_start = time.time()
        try:
            response = requests.delete(f"{self.api_base}/999999", headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 404:
                self.log_test("test_returns_404_when_deleting_nonexistent_todo", "PASS", 
                            "正確返回 404 狀態碼", execution_time)
                return True
            
            self.log_test("test_returns_404_when_deleting_nonexistent_todo", "FAIL", 
                        f"狀態碼不正確: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_returns_404_when_deleting_nonexistent_todo", "FAIL", f"請求異常: {str(e)}", execution_time)
            return False
    
    def test_returns_404_when_updating_nonexistent_todo(self) -> bool:
        """測試 404 錯誤 - 更新不存在的任務"""
        test_start = time.time()
        try:
            update_data = {
                "title": "更新標題",
                "description": "更新描述",
                "completed": True
            }
            
            response = requests.put(f"{self.api_base}/999999", json=update_data, headers=self.headers)
            execution_time = time.time() - test_start
            
            if response.status_code == 404:
                self.log_test("test_returns_404_when_updating_nonexistent_todo", "PASS", 
                            "正確返回 404 狀態碼", execution_time)
                return True
            
            self.log_test("test_returns_404_when_updating_nonexistent_todo", "FAIL", 
                        f"狀態碼不正確: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_returns_404_when_updating_nonexistent_todo", "FAIL", f"請求異常: {str(e)}", execution_time)
            return False
    
    def test_api_connectivity(self) -> bool:
        """測試 API 連線性"""
        test_start = time.time()
        try:
            response = requests.get(self.base_url, timeout=5)
            execution_time = time.time() - test_start
            
            if response.status_code in [200, 404]:  # Laravel 預設回應
                self.log_test("test_api_connectivity", "PASS", 
                            f"API 服務正常運行", execution_time)
                return True
            
            self.log_test("test_api_connectivity", "FAIL", 
                        f"API 服務異常，狀態碼: {response.status_code}", execution_time)
            return False
            
        except Exception as e:
            execution_time = time.time() - test_start
            self.log_test("test_api_connectivity", "FAIL", f"連線異常: {str(e)}", execution_time)
            return False
    
    def run_all_tests(self) -> Dict[str, Any]:
        """執行所有測試"""
        print(f"=== TODO List API Python 外部測試 ===")
        print(f"測試開始時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"API 基礎網址: {self.api_base}")
        print()
        
        self.start_time = time.time()
        
        # 測試 API 連線
        if not self.test_api_connectivity():
            print("❌ API 連線失敗，停止測試")
            return self.generate_report()
        
        print("\n=== Feature Tests (功能測試) ===")
        
        # 基本 CRUD 測試
        self.test_can_get_all_todos()
        
        # 建立測試任務
        todo_id = self.test_can_create_todo()
        
        if todo_id:
            # 使用建立的任務進行其他測試
            self.test_can_get_single_todo(todo_id)
            self.test_can_update_todo(todo_id)
            self.test_can_delete_todo(todo_id)
        else:
            # 如果建立失敗，記錄其他測試為跳過
            self.log_test("test_can_get_single_todo", "SKIP", "前置條件失敗 - 無法建立測試任務")
            self.log_test("test_can_update_todo", "SKIP", "前置條件失敗 - 無法建立測試任務")
            self.log_test("test_can_delete_todo", "SKIP", "前置條件失敗 - 無法建立測試任務")
        
        print("\n=== Validation Tests (驗證測試) ===")
        
        # 驗證測試
        self.test_title_is_required()
        self.test_description_is_required()
        
        print("\n=== Error Handling Tests (錯誤處理測試) ===")
        
        # 錯誤處理測試
        self.test_returns_404_for_nonexistent_todo()
        self.test_returns_404_when_deleting_nonexistent_todo()
        self.test_returns_404_when_updating_nonexistent_todo()
        
        self.end_time = time.time()
        
        return self.generate_report()
    
    def generate_report(self) -> Dict[str, Any]:
        """生成測試報告"""
        total_time = self.end_time - self.start_time if self.end_time and self.start_time else 0
        
        print(f"\n=== 測試結果摘要 ===")
        print(f"總測試數量: {self.total_tests}")
        print(f"通過測試: {self.passed_tests}")
        print(f"失敗測試: {self.failed_tests}")
        print(f"通過率: {(self.passed_tests/self.total_tests*100):.1f}%" if self.total_tests > 0 else "0%")
        print(f"總執行時間: {total_time:.3f} 秒")
        
        report = {
            'summary': {
                'total_tests': self.total_tests,
                'passed_tests': self.passed_tests,
                'failed_tests': self.failed_tests,
                'pass_rate': (self.passed_tests/self.total_tests*100) if self.total_tests > 0 else 0,
                'total_execution_time': total_time,
                'start_time': self.start_time,
                'end_time': self.end_time
            },
            'test_results': self.test_results,
            'api_base_url': self.api_base,
            'timestamp': datetime.now().isoformat()
        }
        
        return report

def main():
    """主程式"""
    # 可以從命令列參數讀取 API 基礎網址
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost"
    
    tester = TodoApiTester(base_url)
    report = tester.run_all_tests()
    
    # 儲存報告為 JSON 檔案
    timestamp = datetime.now().strftime('%Y-%m-%d')
    output_file = f"python-api-test-report-{timestamp}.json"
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n📄 詳細報告已儲存至: {output_file}")
    except Exception as e:
        print(f"\n❌ 無法儲存報告: {str(e)}")
    
    # 回傳退出碼
    return 0 if report['summary']['failed_tests'] == 0 else 1

if __name__ == "__main__":
    exit(main())

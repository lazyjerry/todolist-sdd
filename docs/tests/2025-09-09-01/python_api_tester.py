#!/usr/bin/env python3
"""
TODO List API Python 測試腳本
使用 Python requests 模組執行相同邏輯的 API 測試
作為 PHPUnit 測試結果的驗證參考

執行日期: 2025-09-09
Python 版本: 3.x
依賴套件: requests, json
"""

import requests
import json
import time
import sys
from typing import Dict, Any, List, Optional
from datetime import datetime

class TodoApiTester:
    """TODO API 測試類別"""
    
    def __init__(self, base_url: str = "http://localhost"):
        """
        初始化測試器
        
        Args:
            base_url: API 基礎 URL
        """
        self.base_url = base_url.rstrip('/')
        self.api_url = f"{self.base_url}/api/todos"
        self.test_results = []
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        
    def log_test(self, test_name: str, success: bool, message: str = "", response_time: float = 0):
        """記錄測試結果"""
        self.total_tests += 1
        if success:
            self.passed_tests += 1
            status = "✅ PASS"
        else:
            self.failed_tests += 1
            status = "❌ FAIL"
            
        result = {
            "test_name": test_name,
            "status": status,
            "success": success,
            "message": message,
            "response_time": f"{response_time:.3f}s"
        }
        self.test_results.append(result)
        print(f"{status} {test_name} ({response_time:.3f}s)")
        if message and not success:
            print(f"    錯誤: {message}")
    
    def make_request(self, method: str, url: str, **kwargs) -> tuple:
        """
        發送 HTTP 請求
        
        Returns:
            tuple: (response, response_time)
        """
        start_time = time.time()
        try:
            kwargs.setdefault('headers', {})['Accept'] = 'application/json'
            response = requests.request(method, url, **kwargs)
            response_time = time.time() - start_time
            return response, response_time
        except Exception as e:
            response_time = time.time() - start_time
            print(f"請求錯誤: {e}")
            return None, response_time
    
    def test_health_check(self) -> bool:
        """測試應用程式健康狀態"""
        test_name = "應用程式健康檢查"
        
        response, response_time = self.make_request('GET', f"{self.base_url}/up")
        
        if response is None:
            self.log_test(test_name, False, "無法連接到服務器", response_time)
            return False
            
        success = response.status_code == 200
        message = f"狀態碼: {response.status_code}" if not success else ""
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def test_get_all_todos(self) -> bool:
        """測試獲取所有任務列表"""
        test_name = "獲取所有任務列表"
        
        response, response_time = self.make_request('GET', self.api_url)
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return False
        
        try:
            data = response.json()
            success = (
                response.status_code == 200 and
                'data' in data and
                'meta' in data and
                'total' in data['meta']
            )
            
            if success:
                message = f"返回 {data['meta']['total']} 個任務"
            else:
                message = f"狀態碼: {response.status_code}, 回應格式不正確"
                
        except json.JSONDecodeError:
            success = False
            message = "回應不是有效的 JSON 格式"
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def test_create_todo(self) -> Optional[int]:
        """
        測試建立新任務
        
        Returns:
            todo_id: 建立成功時返回任務 ID，失敗時返回 None
        """
        test_name = "建立新任務"
        
        todo_data = {
            "title": "Python 測試任務",
            "description": "這是使用 Python 建立的測試任務"
        }
        
        response, response_time = self.make_request(
            'POST', 
            self.api_url,
            json=todo_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return None
        
        try:
            data = response.json()
            success = (
                response.status_code == 201 and
                'data' in data and
                'id' in data['data'] and
                data['data']['title'] == todo_data['title'] and
                data['data']['description'] == todo_data['description']
            )
            
            if success:
                todo_id = data['data']['id']
                message = f"任務 ID: {todo_id}"
                self.log_test(test_name, success, message, response_time)
                return todo_id
            else:
                message = f"狀態碼: {response.status_code}, 回應格式不正確"
                
        except json.JSONDecodeError:
            success = False
            message = "回應不是有效的 JSON 格式"
        
        self.log_test(test_name, success, message, response_time)
        return None
    
    def test_get_single_todo(self, todo_id: int) -> bool:
        """測試獲取單一任務"""
        test_name = f"獲取單一任務 (ID: {todo_id})"
        
        response, response_time = self.make_request('GET', f"{self.api_url}/{todo_id}")
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return False
        
        try:
            data = response.json()
            success = (
                response.status_code == 200 and
                'data' in data and
                data['data']['id'] == todo_id
            )
            
            if success:
                message = f"標題: {data['data']['title']}"
            else:
                message = f"狀態碼: {response.status_code}"
                
        except json.JSONDecodeError:
            success = False
            message = "回應不是有效的 JSON 格式"
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def test_update_todo(self, todo_id: int) -> bool:
        """測試更新任務"""
        test_name = f"更新任務 (ID: {todo_id})"
        
        update_data = {
            "title": "Python 更新後的任務",
            "description": "使用 Python 更新的任務描述",
            "completed": True
        }
        
        response, response_time = self.make_request(
            'PUT',
            f"{self.api_url}/{todo_id}",
            json=update_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return False
        
        try:
            data = response.json()
            success = (
                response.status_code == 200 and
                'data' in data and
                data['data']['id'] == todo_id and
                data['data']['title'] == update_data['title'] and
                data['data']['completed'] == update_data['completed']
            )
            
            if success:
                message = "任務更新成功"
            else:
                message = f"狀態碼: {response.status_code}"
                
        except json.JSONDecodeError:
            success = False
            message = "回應不是有效的 JSON 格式"
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def test_delete_todo(self, todo_id: int) -> bool:
        """測試刪除任務"""
        test_name = f"刪除任務 (ID: {todo_id})"
        
        response, response_time = self.make_request('DELETE', f"{self.api_url}/{todo_id}")
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return False
        
        success = response.status_code == 204
        message = f"狀態碼: {response.status_code}" if not success else "任務刪除成功"
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def test_validation_title_required(self) -> bool:
        """測試標題必填驗證"""
        test_name = "驗證標題必填"
        
        invalid_data = {
            "description": "沒有標題的任務"
        }
        
        response, response_time = self.make_request(
            'POST',
            self.api_url,
            json=invalid_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return False
        
        try:
            data = response.json()
            success = (
                response.status_code == 422 and
                'errors' in data and
                'title' in data['errors']
            )
            
            if success:
                message = "正確返回驗證錯誤"
            else:
                message = f"狀態碼: {response.status_code}, 預期 422"
                
        except json.JSONDecodeError:
            # 有些驗證錯誤可能不返回 JSON
            success = response.status_code == 422
            message = "返回驗證錯誤但非 JSON 格式"
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def test_validation_description_required(self) -> bool:
        """測試描述必填驗證"""
        test_name = "驗證描述必填"
        
        invalid_data = {
            "title": "沒有描述的任務"
        }
        
        response, response_time = self.make_request(
            'POST',
            self.api_url,
            json=invalid_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return False
        
        try:
            data = response.json()
            success = (
                response.status_code == 422 and
                'errors' in data and
                'description' in data['errors']
            )
            
            if success:
                message = "正確返回驗證錯誤"
            else:
                message = f"狀態碼: {response.status_code}, 預期 422"
                
        except json.JSONDecodeError:
            success = response.status_code == 422
            message = "返回驗證錯誤但非 JSON 格式"
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def test_404_get_nonexistent(self) -> bool:
        """測試 404 錯誤 - 獲取不存在的任務"""
        test_name = "404 錯誤處理 - 獲取不存在任務"
        
        response, response_time = self.make_request('GET', f"{self.api_url}/999999")
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return False
        
        try:
            data = response.json()
            success = (
                response.status_code == 404 and
                'message' in data and
                'error' in data
            )
            
            if success:
                message = f"錯誤訊息: {data['message']}"
            else:
                message = f"狀態碼: {response.status_code}, 預期 404"
                
        except json.JSONDecodeError:
            success = response.status_code == 404
            message = "返回 404 但非 JSON 格式"
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def test_404_delete_nonexistent(self) -> bool:
        """測試 404 錯誤 - 刪除不存在的任務"""
        test_name = "404 錯誤處理 - 刪除不存在任務"
        
        response, response_time = self.make_request('DELETE', f"{self.api_url}/999999")
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return False
        
        success = response.status_code == 404
        message = f"狀態碼: {response.status_code}" if not success else "正確返回 404 錯誤"
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def test_404_update_nonexistent(self) -> bool:
        """測試 404 錯誤 - 更新不存在的任務"""
        test_name = "404 錯誤處理 - 更新不存在任務"
        
        update_data = {
            "title": "嘗試更新不存在的任務",
            "description": "這個更新應該失敗",
            "completed": True
        }
        
        response, response_time = self.make_request(
            'PUT',
            f"{self.api_url}/999999",
            json=update_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response is None:
            self.log_test(test_name, False, "請求失敗", response_time)
            return False
        
        success = response.status_code == 404
        message = f"狀態碼: {response.status_code}" if not success else "正確返回 404 錯誤"
        
        self.log_test(test_name, success, message, response_time)
        return success
    
    def run_all_tests(self) -> Dict[str, Any]:
        """執行所有測試"""
        print("🐍 Python TODO API 測試開始")
        print("=" * 50)
        
        start_time = time.time()
        
        # 1. 健康檢查
        if not self.test_health_check():
            print("\n❌ 服務器無法連接，停止測試")
            return self.generate_report(time.time() - start_time)
        
        print("\n📋 API 功能測試")
        print("-" * 30)
        
        # 2. 基本 CRUD 測試
        self.test_get_all_todos()
        
        # 3. 建立任務並取得 ID
        todo_id = self.test_create_todo()
        
        if todo_id:
            # 4. 使用建立的任務 ID 進行其他測試
            self.test_get_single_todo(todo_id)
            self.test_update_todo(todo_id)
            self.test_delete_todo(todo_id)
        
        print("\n🔍 驗證測試")
        print("-" * 30)
        
        # 5. 驗證測試
        self.test_validation_title_required()
        self.test_validation_description_required()
        
        print("\n❌ 錯誤處理測試")
        print("-" * 30)
        
        # 6. 404 錯誤測試
        self.test_404_get_nonexistent()
        self.test_404_delete_nonexistent()
        self.test_404_update_nonexistent()
        
        total_time = time.time() - start_time
        return self.generate_report(total_time)
    
    def generate_report(self, total_time: float) -> Dict[str, Any]:
        """生成測試報告"""
        
        print("\n" + "=" * 50)
        print("📊 Python 測試報告摘要")
        print("=" * 50)
        
        success_rate = (self.passed_tests / self.total_tests * 100) if self.total_tests > 0 else 0
        
        report = {
            "execution_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_tests": self.total_tests,
            "passed_tests": self.passed_tests,
            "failed_tests": self.failed_tests,
            "success_rate": f"{success_rate:.1f}%",
            "total_time": f"{total_time:.2f}s",
            "test_results": self.test_results
        }
        
        # 打印摘要
        print(f"總測試數: {self.total_tests}")
        print(f"通過測試: {self.passed_tests}")
        print(f"失敗測試: {self.failed_tests}")
        print(f"成功率: {success_rate:.1f}%")
        print(f"執行時間: {total_time:.2f}s")
        
        if self.failed_tests > 0:
            print(f"\n❌ 失敗的測試:")
            for result in self.test_results:
                if not result['success']:
                    print(f"  - {result['test_name']}: {result['message']}")
        
        return report

def main():
    """主函數"""
    
    # 檢查依賴
    try:
        import requests
    except ImportError:
        print("❌ 缺少 requests 模組，請安裝: pip install requests")
        sys.exit(1)
    
    # 檢查命令列參數
    base_url = "http://localhost"
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    
    print(f"🎯 目標 API: {base_url}")
    
    # 執行測試
    tester = TodoApiTester(base_url)
    report = tester.run_all_tests()
    
    # 儲存報告到檔案
    report_file = f"python-api-test-report-{datetime.now().strftime('%Y-%m-%d')}.json"
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\n📄 詳細報告已儲存到: {report_file}")
    except Exception as e:
        print(f"\n⚠️  無法儲存報告檔案: {e}")
    
    # 根據測試結果設定退出碼
    sys.exit(0 if report['failed_tests'] == 0 else 1)

if __name__ == "__main__":
    main()

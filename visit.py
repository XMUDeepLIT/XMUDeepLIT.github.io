import time
import requests

def normal_visit(url, count=10):
    """模拟正常访问"""
    for i in range(count):
        try:
            response = requests.get(url, timeout=5)
            print(f"第{i+1}次访问，状态码: {response.status_code}")
        except Exception as e:
            print(f"访问异常: {str(e)}")
        time.sleep(1)  # 重要：设置较长间隔

if __name__ == "__main__":
    # 请务必遵守目标网站的robots.txt和服务条款
    target_url = "https://xmudeeplit.github.io/"
    normal_visit(target_url, 50000)  # 
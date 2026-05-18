import requests

def test_demo_health_check():
    """一个不会失败的示例测试，验证接口状态码"""
    url = "https://httpbin.org/status/200"
    resp = requests.get(url, timeout=10)
    assert resp.status_code == 200
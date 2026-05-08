import requests
import pytest

@pytest.fixture(scope="module")  # module级: 所有test共享
def base_url():
    """简单fixture: 返回base_url字符串"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_headers():
    """全局headers"""
    return {"Content-Type": "application/json"}

def test_post_ok(base_url, api_headers):
    """正向: fixture注入"""
    url = f"{base_url}/posts"
    payload = {"title": "正向OK", "body": "成功", "userId": 1}
    r = requests.post(url, json=payload, headers=api_headers)
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == "正向OK"
    print("✅ 正向POST通过！")

def test_post_error(base_url, api_headers):
    """负向: 空title"""
    url = f"{base_url}/posts"
    payload = {"title": "", "body": "无效", "userId": 1}
    r = requests.post(url, json=payload, headers=api_headers)
    data = r.json()
    assert r.status_code == 201  # mock总是201
    assert data["title"] == ""  # 验证异常回显
    print("✅ 负向通过！")

@pytest.mark.parametrize("title, valid", [("OK", True), ("", False), (None, False)])
def test_post_param(base_url, api_headers, title, valid):
    """参数化+多fixture"""
    url = f"{base_url}/posts"
    payload = {"title": title or "", "body": "param测试", "userId": 1}
    r = requests.post(url, json=payload, headers=api_headers)
    data = r.json()
    assert r.status_code == 201
    if valid:
        assert len(data["title"]) > 0
    else:
        assert data["title"] == "" or data["title"] is None
    print(f"参数化: title='{title}' -> {'PASS' if valid else '异常OK'}")

print("🎉 CI/CD测试触发啦！")
print("Actions跑啦！")

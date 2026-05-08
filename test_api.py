import requests
import pytest

base_url = "https://jsonplaceholder.typicode.com"

def test_get_post():
    """测试GET接口：获取posts/1"""
    url = f"{base_url}/posts/1"
    response = requests.get(url)
    
    # 断言
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2  # 响应<2s
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    print("GET测试通过！响应数据:", data["body"][:50])  # 打印部分body

def test_post_create():
    """测试POST接口：创建post（模拟数据）"""
    url = f"{base_url}/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    
    # 断言（它会返回201 + 你的数据 + id=101）
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"
    assert data["id"] == 101  # 固定返回
    print("POST测试通过！新ID:", data["id"])

def test_invalid_param():
    """负向测试：无效参数"""
    url = f"{base_url}/posts/99999"
    response = requests.get(url)
    assert response.status_code == 404  # 不存在返回404
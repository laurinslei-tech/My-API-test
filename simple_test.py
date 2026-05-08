import requests  # pip install requests

def test_basic():
    """简单GET测试"""
    url = "https://v1.hitokoto.cn"  # 国内一言API
    r = requests.get(url)
    assert r.status_code == 200  # 核心断言
    data = r.json()
    print("✅ 测试通过！鸡汤:", data["hitokoto"][:30] + "...")

# 直接跑
if __name__ == "__main__":
    test_basic()
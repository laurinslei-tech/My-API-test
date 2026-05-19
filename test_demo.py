import pytest
import requests

# @pytest.mark.skip(reason="网络环境无法访问外部接口，跳过")
def test_demo_health_check():
    url = "https://www.baidu.com"
    resp = requests.get(url, timeout=15)
    assert resp.status_code == 200

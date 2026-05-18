pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh '''
                    # 容器里必须加 root 权限
                    apt-get update -y
                    apt-get install -y python3-pip
                    
                    # 安装测试库
                    pip3 install pytest requests
                    
                    # 运行测试
                    python3 -m pytest test_api_ok.py -v
                '''
            }
        }
    }
}

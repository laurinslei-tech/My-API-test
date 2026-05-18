pipeline {
    agent any
    
    stages {
        // 检查环境
        stage('检查环境') {
            steps {
                sh '''
                    python3 --version || echo "没装Python"
                    pip3 --version || echo "没装pip"
                    pytest --version || echo "没装pytest"
                    ls -l
                '''
            }
        }

        // 安装依赖
        stage('安装依赖') {
            steps {
                sh '''
                    apt-get update -y
                    apt-get install -y python3-pip
                    pip3 install pytest requests
                '''
            }
        }

        // 运行测试
        stage('运行测试') {
            steps {
                sh 'python3 -m pytest test_api_ok.py -v'
            }
        }
    }
}

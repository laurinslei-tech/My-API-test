pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                // 先看看文件到底在不在，避免找不到
                sh 'ls -la'
                
                // 只用你的镜像，纯运行，不装任何东西
                sh 'docker run --rm -v "$PWD":/app -w /app my-pytest:final python3 -m pytest test_api_ok.py -v'
            }
        }
    }
}

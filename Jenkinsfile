pipeline {
    agent any
    stages {
        stage('API自动化测试') {
            steps {
                // 直接运行你的测试文件
                sh 'python3 -m pytest test_api_ok.py -v'
            }
        }
    }
}

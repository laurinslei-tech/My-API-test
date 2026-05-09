pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh 'python3 -m pytest test_api_ok.py -v'
            }
        }
    }
}

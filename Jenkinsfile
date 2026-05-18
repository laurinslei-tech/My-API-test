pipeline {
    agent any
    stages {
        stage('API自动化测试') {
            steps {
                sh 'python3 -m pytest test_api_ok.py -v --junitxml=test-results.xml'
            }
        }
    }
    post {
        always {
            // 把测试报告同步给 Jenkins，再同步回 GitHub
            junit 'test-results.xml'
        }
    }
}

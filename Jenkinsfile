pipeline {
    agent any
    stages {
        stage('测试') {
            steps {
                sh 'docker run --rm -v $PWD:/app -w /app my-pytest python -m pytest -v test_api_ok.py --html=report.html'
            }
        }
    }
    post {
        always {
            publishHTML(reportDir: '.', reportFiles: 'report.html', reportName: '测试报告')
        }
    }
}

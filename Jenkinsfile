pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh 'python -m pytest -v test_api_ok.py --html=report.html'
            }
        }
    }
    post {
        always {
            publishHTML(target: [
                allowMissing: true,
                reportFiles: 'report.html',
                reportDir: '.',
                reportName: '测试报告'
            ])
        }
    }
}
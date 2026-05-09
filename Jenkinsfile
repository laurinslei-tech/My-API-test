pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh 'docker run --rm -v "$PWD:/app" -w /app my-pytest:final pytest -v --html=report.html'
            }
        }
    }
    post {
        always {
            publishHTML(
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: "接口测试报告"
            )
        }
    }
}

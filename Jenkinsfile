pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh 'docker run --rm -v $PWD:/app -w /app my-pytest python simple_test.py -v --html=report.html'
            }
        }
    }
    post {
        always {
            publishHTML(
                allowMissing: true,
                alwaysLinkLink: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: "接口测试报告"
            )
        }
    }
}

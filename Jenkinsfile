pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh 'ls -la'
                sh 'pwd'
                sh 'docker run --rm -v ${WORKSPACE}:${WORKSPACE} -w ${WORKSPACE} my-pytest python -m pytest test_api.py -v --html=report.html'
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

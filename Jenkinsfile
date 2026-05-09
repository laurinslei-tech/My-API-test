pipeline {
    agent any

    stages {
        stage('拉代码') {
            steps {
                checkout scm
            }
        }

        stage('跑测试') {
            steps {
                sh '''
docker run --rm -v ${WORKSPACE}:/app -w /app my-pytest python -m pytest test_api_ok.py -v --html=report.html
                '''
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
                reportName: "API测试报告"
            )
        }
    }
}

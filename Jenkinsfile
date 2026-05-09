pipeline {
    agent any

    stages {
        stage('拉取代码') {
            steps {
                checkout scm
            }
        }

        stage('运行API测试') {
            steps {
                sh '''
docker run --rm -v ${WORKSPACE}:/app -w /app my-pytest python -m pytest -v --html=report.html
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

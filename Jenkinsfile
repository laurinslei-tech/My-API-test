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
                ls -la
                docker run --rm \
                    -v $(pwd):/app \
                    -w /app \
                    python:3.11-slim \
                    bash -c "
                        pip install pytest requests pytest-html
                        pytest test_api_ok.py -v --html=report.html
                    "
                '''
            }
        }
    }

    post {
        always {
            publishHTML(
                target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'API测试报告'
                ]
            )
        }
    }
}

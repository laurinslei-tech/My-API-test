pipeline {
    agent any

    stages {
        stage('拉取代码') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }

        stage('运行API测试') {
            steps {
                sh '''
docker run --rm -v $PWD:/app -w /app python:3.11-slim bash -c "pip install pytest requests pytest-html && python -m pytest test_api_ok.py -v --html=report.html"
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
            })
        }
    }
}

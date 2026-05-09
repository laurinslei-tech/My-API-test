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
                # 直接用 Python 镜像！不用装系统！超快！
                docker run --rm \
                    -v $(pwd):/app \
                    -w /app \
                    python:3.11-slim \
                    bash -c "
                        # 只装依赖，超快！1-3秒完成！
                        pip install pytest requests pytest-html
                        
                        # 运行测试，显示详细结果
                        pytest -v --html=report.html
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

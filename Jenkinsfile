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
                docker run --rm \
                    -v $(pwd):/app \
                    -w /app \
                    ubuntu:22.04 bash -c "
                        apt-get update -qq
                        apt-get install -y python3 python3-pip
                        pip3 install pytest requests pytest-html
                        
                        # 关键在这里！加了 -v 就能看到 pass 数量
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

pipeline {
    agent any
    stages {
        stage('安装依赖') {
            steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip'
                sh 'pip3 install pytest requests'
            }
        }
        stage('运行测试') {
            steps {
                sh 'python3 -m pytest test_api_ok.py -v --html=report.html'
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
                reportName: "测试报告"
            )
        }
    }
}

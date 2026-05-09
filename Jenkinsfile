pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh 'apt-get update -y && apt-get install -y python3-pip && pip3 install pytest requests && python3 -m pytest test_api_ok.py -v'
            }
        }
    }
}

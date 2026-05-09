pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh '''
                    sudo apt-get update -y
                    sudo apt-get install -y python3-pip
                    sudo pip3 install pytest requests
                    python3 -m pytest test_api_ok.py -v
                '''
            }
        }
    }
}

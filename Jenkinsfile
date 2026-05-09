pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh 'docker run --rm -v "${WORKSPACE}":/app -w /app my-pytest:final python3 -m pytest test_api_ok.py -v'
            }
        }
    }
}

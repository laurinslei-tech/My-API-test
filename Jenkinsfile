pipeline {
    agent any
    stages {
        stage('运行测试') {
            steps {
                sh 'docker run --rm -v $(pwd):/app -w /app my-pytest:final python3 -m pytest /app/test_api_ok.py -v'
            }
        }
    }
}

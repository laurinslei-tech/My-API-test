pipeline {
    agent any
    stages {
        stage('API自动化测试') {
            steps {
                sh '''
                    python3 -m pytest test_api_ok.py -v \
                        --junitxml=test-results.xml \
                        --alluredir=allure-results
                '''
            }
        }
    }
    post {
        always {
            junit 'test-results.xml'
            allure results: [[path: 'allure-results']]
        }
    }
}

pipeline {
    agent any

    tools {
        // 和你上面配置的 Name 必须一模一样！
        allure 'allure-2.40.0'
    }

    stages {
        stage('API自动化测试') {
            steps {
                sh 'python3 -m pytest -v --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
            allure(
                results: [[path: 'allure-results']]
            )
        }
    }
}

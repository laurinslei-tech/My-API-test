pipeline {
    agent any
    stages {
        stage('API自动化测试') {
            steps {
                sh '''
                    # 执行 pytest，同时生成 JUnit 和 Allure 报告数据
                    python3 -m pytest test_api_ok.py -v \
                        --junitxml=test-results.xml \
                        --alluredir=allure-results
                '''
            }
        }
    }
    post {
        always {
            // 发布 JUnit 报告（你已经配置了）
            junit 'test-results.xml'
            // 发布 Allure 报告（新增的关键步骤）
            allure includeResults: true, results: [[path: 'allure-results']]
        }
    }
}

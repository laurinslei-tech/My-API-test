pipeline {
  agent {
    docker {
      image 'python:3.11'
    }
  }

  stages {
    stage('Test') {
      steps {
        sh '''
        pip install pytest requests pytest-html allure-pytest -r requirements.txt
        pytest --version
        ls test_api_ok.py
        pytest test_api_ok.py -v --html=report.html --self-contained-html --alluredir=reports
        ls report.html reports/
        '''
      }
    }
  }

  post {
    always {
      publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: '/workspace',
        reportFiles: 'report.html',
        reportName: 'Pytest Report'
      ])
    }
  }
}

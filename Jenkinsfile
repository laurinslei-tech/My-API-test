pipeline {
  agent {
    docker {
      image 'python:3.11'  # Python容器跑
      args '-u root'  # root权限
    }
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Test') {
      steps {
        sh '''
        pip install pytest requests pytest-html allure-pytest -r requirements.txt
        pytest test_api_ok.py -v --alluredir=reports --html=report.html --self-contained-html
        '''
      }
    }
  }

  post {
    always {
      publishHTML([
        allowMissing: false,
        reportDir: '.',
        reportFiles: 'report.html',
        reportName: 'Pytest Report'
      ])
      archiveArtifacts artifacts: 'report.html, reports/**', allowEmptyArchive: true
    }
  }
}

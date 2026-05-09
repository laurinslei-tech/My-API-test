pipeline {
  agent {
    docker {
      image 'python:3.11'
      args '-u root'
    }
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install') {
      steps {
        sh '''
        pip install -r requirements.txt || pip install pytest requests pytest-html allure-pytest
        '''
      }
    }

    stage('Pytest') {
      steps {
        sh '''
        pytest test_api_ok.py -v \\
          --alluredir=reports \\
          --html=report.html \\
          --self-contained-html \\
          --junitxml=report.xml
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
        reportDir: '.',
        reportFiles: 'report.html',
        reportName: 'Pytest HTML'
      ])
      junit 'report.xml'
      archiveArtifacts artifacts: 'report.html, reports/**', allowEmptyArchive: true
    }
    success {
      echo '✅ PASS!'
    }
    failure {
      echo '❌ FAILED!'
    }
  }
}

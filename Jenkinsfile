pipeline {
  agent {
    docker {
      image 'python:3.11-slim'  // slim轻+apt
      args '-u root:root -v $(pwd):/workspace'  // root + 挂载
    }
  }

  stages {
    stage('Test') {
      steps {
        sh '''
        cd /workspace
        ls -la
        pip install --upgrade pip
        pip install pytest requests pytest-html allure-pytest -r requirements.txt
        pytest test_api_ok.py -v --html=report.html --self-contained-html --alluredir=reports
        ls -la report.html reports/
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
        reportName: 'Pytest HTML'
      ])
      archiveArtifacts artifacts: 'report.html, reports/**', fingerprint: true
    }
  }
}

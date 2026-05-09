pipeline {
  agent any

  stages {
    stage('Setup Python') {
      steps {
        sh '''
        sudo apt-get update -qq
        sudo apt-get install -y -qq python3 python3-pip curl
        sudo pip3 install pytest requests pytest-html allure-pytest -r requirements.txt --quiet
        which pytest
        pytest --version
        '''
      }
    }

    stage('Pytest') {
      steps {
        sh '''
        pytest test_api_ok.py -v \\
          --html=report.html \\
          --self-contained-html \\
          --alluredir=reports \\
          --junitxml=report.xml
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
        reportDir: '.',
        reportFiles: 'report.html',
        reportName: 'Pytest HTML Report'
      ])
      junit([
        allowEmptyResults: true,
        testResults: 'report.xml'
      ])
      archiveArtifacts artifacts: 'report.html, reports/**', fingerprint: true
    }
  }
}

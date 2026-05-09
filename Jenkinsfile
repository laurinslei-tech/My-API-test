pipeline {
  agent any

  stages {
    stage('Test') {
      steps {
        sh '''
        apt-get update -qq
        apt-get install -y python3 python3-pip
        pip3 install pytest requests pytest-html
        pytest test_api_ok.py -v --html=report.html --self-contained-html
        ls -la report.html
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
        reportName: 'Pytest Report'
      ])
    }
  }
}

pipeline {
  agent any

  stages {
    stage('Install') {
      steps {
        sh '''
        pip install -r requirements.txt || pip install pytest requests pytest-html
        '''
      }
    }

    stage('Pytest') {
      steps {
        sh 'pytest test_api_ok.py -v --html=report.html --self-contained-html'
      }
    }
  }

  post {
    always {
      publishHTML([
        allowMissing: false,
        reportDir: '',
        reportFiles: 'report.html',
        reportName: 'HTML Report',
        reportTitles: ''
      ])
      archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
    }
  }
}

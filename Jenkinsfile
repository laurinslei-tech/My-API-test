pipeline {
  agent any

  stages {
    stage('Test') {
      steps {
        sh '''
        sudo apt-get update -qq
        sudo apt-get install -y python3 python3-pip
        pip3 install pytest requests pytest-html --user
        export PATH=$HOME/.local/bin:$PATH
        pytest test_api_ok.py -v --html=report.html --self-contained-html
        ls -la report.html
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true, fingerprint: true
    }
    success {
      echo '✅ SUCCESS!'
    }
    failure {
      echo '❌ FAILURE!'
    }
  }
}

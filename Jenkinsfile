pipeline {
  agent any

  stages {
    stage('Test') {
      steps {
        sh '''
        docker run --rm \\
          -v $(pwd):/app \\
          -w /app \\
          ubuntu:22.04 bash -c "
          apt-get update -qq
          apt-get install -y python3 python3-pip curl
          pip3 install pytest requests pytest-html
          pytest test_api_ok.py -v --html=report.html --self-contained-html
          ls -la report.html
          "
        '''
      }
    }
  }

  post {
    always {
      publishHTML([
        allowMissing: true,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: '.',
        reportFiles: 'report.html',
        reportName: 'Report'
      ])
    }
  }
}

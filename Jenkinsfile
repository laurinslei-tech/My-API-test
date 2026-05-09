pipeline {
  agent any  // host节点

  stages {
    stage('Test') {
      steps {
        sh '''
        # 临时Python容器跑
        docker run --rm \\
          -v $(pwd):/app \\
          -w /app \\
          python:3.11 \\
          bash -c "
          pip install pytest requests pytest-html -r requirements.txt
          pytest test_api_ok.py -v --html=report.html --self-contained-html --alluredir=reports
          ls -la report.html reports/
          "
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
      archiveArtifacts artifacts: 'report.html, reports/**', allowEmptyArchive: true
    }
  }
}

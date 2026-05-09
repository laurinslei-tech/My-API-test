pipeline {
  agent any

  stages {
    stage('Debug') {
      steps {
        sh '''
        ls -la  # 查文件
        which python3 || echo "no python"
        pip3 list | grep pytest || echo "no pytest"
        cat requirements.txt || echo "no req"
        pytest --version || echo "pytest fail"
        pytest test_api_ok.py -v --html=report.html || echo "pytest error"
        '''
      }
    }
  }
}

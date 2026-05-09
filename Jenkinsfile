pipeline {
  agent any

  stages {
    stage('Debug Full') {
      steps {
        sh '''
        echo "=== LS ==="
        ls -la test_api_ok.py requirements.txt || echo "文件缺"
        echo "=== Python ==="
        which python3 || which python || echo "no python"
        python3 --version || echo "no py3"
        echo "=== Pip ==="
        which pip3 || which pip || echo "no pip"
        pip3 list || echo "no pip list"
        echo "=== Install ==="
        apt-get update -qq
        apt-get install -y python3 python3-pip || echo "apt fail"
        pip3 install pytest requests pytest-html --user || echo "pip fail"
        echo "=== Pytest ==="
        which pytest || echo "pytest not found"
        pytest --version || echo "pytest version fail"
        pytest test_api_ok.py -v --html=report.html || echo "RUN FAIL: $?"
        ls -la report.html || echo "no report"
        '''
      }
    }
  }
}

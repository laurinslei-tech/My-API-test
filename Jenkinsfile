pipeline {
  agent {
    docker {
      image 'python:3.11'
      args '-u root -v /var/run/docker.sock:/var/run/docker.sock'  // docker权限
    }
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm  // 拉repo
      }
    }

    stage('Install Deps') {
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
      // HTML报告
      publishHTML([
        allowMissing: false,
        reportDir: '.',
        reportFiles: 'report.html',
        reportName: 'Pytest HTML Report',
        reportTitles: ''
      ])
      // Allure报告 (插件)
      allure([
        includeProperties: false,
        jdk: '',
        resultsPath: 'reports'
      ])
      // JUnit XML
      junit 'report.xml'
      // 存档
      archiveArtifacts artifacts: 'report.html, reports/**, report.xml', allowEmptyArchive: true
    }
    success {
      echo '✅ All PASS!'
    }
    failure {
      echo '❌ Test Failed!'
    }
  }
}

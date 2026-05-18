stage('检查环境') {
    steps {
        sh '''
            echo "======== 检查系统版本 ========"
            cat /etc/os-release
            
            echo "======== 检查 Python ========"
            python3 --version || echo "未安装 Python"
            
            echo "======== 检查 pip ========"
            pip3 --version || echo "未安装 pip"
            
            echo "======== 检查 pytest ========"
            pytest --version || echo "未安装 pytest"
            
            echo "======== 查看当前目录文件 ========"
            ls -l
        '''
    }
}

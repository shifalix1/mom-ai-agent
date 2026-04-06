pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
              bat 'python -m pip install -r requirements.txt'
              bat 'python -m pip install pytest pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'set PYTHONPATH=. && pytest tests/ --html=report.html --self-contained-html -v'
            }
        }

        stage('Archive Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest Report'
                ])
            }
        }
    }

    post {
        success {
            echo 'All tests passed'
        }
        failure {
            echo 'Tests failed'
        }
    }
}
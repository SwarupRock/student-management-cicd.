pipeline {
    agent any

    environment {
        // Prepend Python to PATH for Jenkins Windows Service (runs as LocalSystem)
        PATH = "C:\\Users\\Swarup D\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Swarup D\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Run Application') {
            steps {
                bat '.venv\\Scripts\\python.exe app.py'
            }
        }

        stage('Package Release') {
            steps {
                bat '''
                    if not exist release mkdir release
                    copy /Y app.py release\\app.py
                    copy /Y requirements.txt release\\requirements.txt
                '''
                archiveArtifacts artifacts: 'release/**', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All stages completed.'
        }

        failure {
            echo 'FAILED: Check Console Output.'
        }
    }
}
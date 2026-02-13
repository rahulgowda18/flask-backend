pipeline {
    agent any

    environment {
        APP_NAME = "flask-backend"
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/rahulgowda18/flask-backend.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Restart App') {
            steps {
                sh 'pm2 restart flask-backend || pm2 start "venv/bin/python app.py" --name flask-backend'
            }
        }
    }
}

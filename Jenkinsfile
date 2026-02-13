pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/rahulgowda18/flask-backend.git'
            }
        }

        stage('Setup Virtual Environment') {
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
                sh 'pm2 restart flask-app || pm2 start app.py --name flask-app --interpreter ./venv/bin/python'
            }
        }
    }
}

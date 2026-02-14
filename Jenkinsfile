pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/rahulgowda18/flask-backend.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Restart Application') {
            steps {
                sh 'pm2 restart flask-backend || pm2 start "./venv/bin/python app.py" --name flask-backend'
            }
        }
    }
}

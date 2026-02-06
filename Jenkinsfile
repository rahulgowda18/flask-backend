pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/rahulgowda18/flask-backend.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f flask-container || true
                docker run -d -p 5000:5000 --name flask-container flask-app
                '''
            }
        }
    }
}

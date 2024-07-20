pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds' 
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/shayle664/WOG', branch: 'master'
            }
        }

        stage('Build and Run') {
            steps {
                script {
                    bat 'docker-compose up --build -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'python e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    bat 'docker-compose down'
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        docker.image('shayle/shay-wog').push('latest')
                    }
                }
            }
        }
    }
}



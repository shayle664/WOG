pipeline {
    agent any
    environment {
        IMAGE_NAME = 'shayle/shay-wog'
        IMAGE_TAG = 'latest'
    }
    stages {
        stage('Clean UP') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repo') {
            steps {
                bat "git clone https://github.com/shayle664/WOG.git"
            }
        }
        stage('Docker') {
            steps {
                script {
                    dir('WOG') {
                        bat "docker-compose up --build -d"
                    }
                }
            }
        }
        stage('E2E') {
            steps {
                dir('WOG') {
                    bat "python e2e.py"
                }
            }
        }
    }
}




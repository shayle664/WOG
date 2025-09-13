pipeline {
    agent any
    environment {
        IMAGE_NAME = 'shayle/shay-wog'
        IMAGE_TAG = 'latest'
        DOCKER_CREDENTIALS_ID = 'docker-hub-credential'
    }
    stages {
        stage('Clean UP') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repo') {
            steps {
                sh "git clone https://github.com/shayle664/WOG.git"
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    dir('WOG') {
                        sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                        sh "docker-compose up --build -d"
                    }
                }
            }
        }
        stage('Test app/E2E') {
            steps {
                dir('WOG') {
                    sh '''
                        sleep 5
                        if curl -s http://localhost:5000 | grep -q "The score is:"; then
                          echo "✅ App is up and contains expected text"
                        else
                          echo "❌ App test failed"
                          exit 1
                        fi
                    '''
                }
            }
        }
        stage('Finalize') {
            steps {
                dir('WOG') {
                    sh "docker-compose down"
                }
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
}




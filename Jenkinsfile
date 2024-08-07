pipeline {
    agent any
    environment {
        IMAGE_NAME = 'world-of-games-app'
        DOCKER_HUB_REPO = 'your-dockerhub-username/world-of-games-app'
    }
    stages {
        stage('Clean UP') {
            steps {
                deleteDir()
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/liranke99/wog-liran.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Convert Windows path to Unix-style path for Docker
                    def workspaceUnixPath = sh(script: 'echo $WORKSPACE', returnStdout: true).trim().replaceAll('\\\\', '/').replaceAll('C:', '/mnt/c')
                    bat "docker build -t ${IMAGE_NAME} ${workspaceUnixPath}"
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Convert Windows path to Unix-style path for Docker volume mount
                    def workspaceUnixPath = sh(script: 'echo $WORKSPACE', returnStdout: true).trim().replaceAll('\\\\', '/').replaceAll('C:', '/mnt/c')
                    bat "docker run -d -t -v /mnt/c/Users/matan/OneDrive/מסמכים/GitHub/wog-liran/Scores.txt:/app/Scores.txt -p 5000:5000 -w ${workspaceUnixPath} ${IMAGE_NAME} cmd.exe"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    bat "docker exec $(docker ps -q -f name=${IMAGE_NAME}) python e2e.py"
                }
            }
        }
        stage('Docker Compose Down') {
            steps {
                bat "docker-compose down"
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    bat "docker tag ${IMAGE_NAME} ${DOCKER_HUB_REPO}:${BUILD_NUMBER}"
                    bat "docker push ${DOCKER_HUB_REPO}:${BUILD_NUMBER}"
                }
            }
        }
    }
}

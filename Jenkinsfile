pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo-url.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('world-of-games-app')
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    app = docker.run('world-of-games-app', '-p 5000:5000', '-v $PWD/Scores.txt:/Scores.txt')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def result = sh(script: 'python e2e.py', returnStatus: true)
                    if (result != 0) {
                        error "Tests failed"
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    app.stop()
                    docker.build('world-of-games-app').push('your-dockerhub-username/world-of-games-app')
                }
            }
        }
    }
}

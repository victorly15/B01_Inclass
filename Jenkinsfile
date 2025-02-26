pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                 git branch: 'main', url: 'https://github.com/victorly15/B01_Inclass.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Define SonarQube server properties
                    def scannerHome = tool 'SonarQubeScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.host.url=http://sonarqube:9000 \
                            -Dsonar.projectKey=jenkins-sonar \
                            -Dsonar.sources=. \
                        """
                    }
                }
            }
        }
        
        stage('Build') {
            steps {
                // Add your build commands here
                sh 'echo Building...'
            }
        }
        
        stage('Test') {
            steps {
                // Add your test commands here
                sh 'echo Testing...'
            }
        }
    }
}

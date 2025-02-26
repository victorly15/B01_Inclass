pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Define SonarQube server properties
                    def scannerHome = tool 'SonarQubeScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
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

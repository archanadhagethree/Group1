pipeline {
    agent any
    stages {

        stage('Check Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Build and test') {
            steps {
                sh 'python3 Dec2Hex.py 15'
            }
        }

        stage('SCM') {
            checkout scm
        }
        
        stage('SonarQube Analysis') {
            def scannerHome = tool 'cube';
            withSonarQubeEnv() {
            sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }

}

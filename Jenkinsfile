pipeline {
    agent any

    stages {
        stage('SCM') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'cube'
                    withSonarQubeEnv('sonar-server') {

                        sh """
                        ${scannerHome}/bin/sonar-scanner \
                          -Dsonar.projectKey= sqp_977048ebb6924caf19055dcdf34be650221d0096 \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://54.196.167.113:9000/
                        """
                    }
                }
            }
        }
    }
}


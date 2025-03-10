pipeline {
    git https://github.com/archanadhagethree/Group1.git

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

                        sh "${scannerHome}/bin/sonar-scanner"
                          
                    }
                }
            }
        }
    }
}


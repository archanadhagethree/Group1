node {

  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'cube';
    withSonarQubeEnv() {
      
        sh """
        sonar-scanner \
        -Dsonar.projectKey=group1 \
        -Dsonar.host.url=http://localhost:9000\
        -Dsonar.token=sqp_77031b53c19837dd608491e072db80e692e98f95
        """

    }
  }
}

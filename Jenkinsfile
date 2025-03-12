node {

    stage('SCM') {
        // Checkout the source code from the Git repository
        checkout scm
    }
  
    stage('SonarQube Analysis') {
        // Define the SonarQube scanner tool path
        def scannerHome = tool 'cube'  // 'cube' should be the name of your SonarQube scanner tool in Jenkins
        
        // Use the SonarQube environment settings
        withSonarQubeEnv() {
            sh """
            sonar-scanner \
            -Dsonar.projectKey=group1 \
            -Dsonar.host.url=http://localhost:9000 \
            -Dsonar.token=sqp_d7f96b2fee04b8d0ff8f6ee1da3c904f64f21898

            """
        }
    }
}

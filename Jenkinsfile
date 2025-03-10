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
            -Dsonar.token=sqp_77031b53c19837dd608491e072db80e692e98f95
            """
        }
    }
}

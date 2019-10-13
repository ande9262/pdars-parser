pipeline {
  agent {
    docker {image 'arm32v7/centos'}
  }
  stages {

    stage ("Build") {
      steps {
        echo "Building..."
        sh "ls -ahl"
       }
    }

    stage('Test') {
      steps {
        echo "Testing..."
       }
    }

    stage ("Deploy") {
      steps {
        echo "Deploying.."
       }
    }

  }
}
pipeline {
  agent {
    docker {image 'centos8'}
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
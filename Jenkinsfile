pipeline {
  agent {
    docker {image 'centos'}
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
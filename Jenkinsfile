pipeline {
  agent {
    docker {image 'arm32v7/centos'}
  }
  stages {

    stage ("Build") {
      steps {
        echo "Building..."
        sh "ls -ahl"
        sh "python setup.py sdist"
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
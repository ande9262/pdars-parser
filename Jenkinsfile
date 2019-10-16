pipeline {
  agent {
    docker {image 'arm32v7/python'}
  }
  stages {

    stage ("Build") {
      steps {
        echo "Building..."
        sh "ls -ahl"
        sh "python setup.py sdist --formats=zip"
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
		archiveArtifacts 'dist/pdars-parser*.zip'
       }
    }
	
	stage ("Clean") {
	  steps {
	    cleanWs(patterns: [[pattern: '**/*.zip', type: 'EXCLUDE']])
	  }
	}

  }
}
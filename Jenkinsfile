pipeline {
  //agent {
    //any
    //docker {image 'arm32v7/python'}
  //}
  agent any
  stages {

    stage ("Build") {
      steps {
        echo "Building..."
        sh "ls -ahl"
        // sh "python setup.py sdist --formats=zip"

        sh "docker build -t test ."

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
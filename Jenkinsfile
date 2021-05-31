pipeline {
    agent { docker { image 'python:3.8.0' } }
    stages {
        stage('build') {
            steps {
                sh """
                ./bin/activate
                pip install -r requirements.txt
                python -m pytest
                """
            }
        }
    }
}

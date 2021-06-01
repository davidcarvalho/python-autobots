pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                bat 'python -m pytest'
            }
        }
    }
}
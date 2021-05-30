pipeline {
    agent {
        docker {
            label 'windows'
            image 'python:3.8.0'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
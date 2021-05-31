pipeline {
    agent { docker { image 'python:3.8.0' } }
    stages {
        stage('build') {
            steps {
                sh """
                VENV=".venv-$BUILD_NUMBER"
                virtualenv "$VENV"
                PS1="${PS1:-}" source "$VENV/bin/activate"
                pip install -r requirements.txt
                python -m pytest
                """
            }
        }
    }
}

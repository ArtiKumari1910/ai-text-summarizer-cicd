```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out AI Text Summarizer project...'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Validate Python Code') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m compileall app
                '''
            }
        }

        stage('Build Success') {
            steps {
                echo 'AI application CI build completed successfully!'
            }
        }
    }
}
```

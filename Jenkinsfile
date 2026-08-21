
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

            pip install --upgrade pip --retries 10 --timeout 120

            grep -v '^torch==' requirements.txt > requirements-ci.txt
            pip install -r requirements-ci.txt --retries 10 --timeout 120
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
        stage('Docker Build') {
    steps {
        sh '''
            docker build -t ai-text-summarizer:latest .
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

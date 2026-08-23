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
        stage('DockerHub Push') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-credentials',
            usernameVariable: 'DOCKERHUB_USER',
            passwordVariable: 'DOCKERHUB_TOKEN'
        )]) {
            sh '''
                echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USER" --password-stdin

                docker tag ai-text-summarizer:latest \
                    $DOCKERHUB_USER/ai-text-summarizer:latest

                docker push $DOCKERHUB_USER/ai-text-summarizer:latest

                docker logout
            '''
        }
    }
}
        stage('Docker Deploy') {
    steps {
        sh '''
            docker rm -f ai-text-summarizer 2>/dev/null || true

            docker run -d \
                --name ai-text-summarizer \
                -p 8000:8000 \
                ai-text-summarizer:latest
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

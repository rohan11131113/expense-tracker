pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url:'https://github.com/rohan11131113/expense-tracker.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t expense-tracker .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5002:5002 expense-tracker'
            }
        }
    }
}

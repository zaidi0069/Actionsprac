pipeline {
    agent any
 
    stages {
        stage('Delete existing directory') {
            steps {
                sh 'rm -rf Actionsprac'
            }
        }
        
        stage('Cloning the repository') {
            steps {
                sh 'git clone https://github.com/zaidi0069/Actionsprac.git'
            }
        }

        stage('Set up Python') {
            steps {
                    sh 'sudo apt install python3'
            }
        }
        
        stage('Dependencies installation') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Execution of test.py') {
            steps {
                sh 'python test.py'
            }
        }
        stage('Deploying step') {
            steps {
                script {
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                    if (branchName == 'main') {
                        echo 'Deploying to production'
                    } else {
                        echo 'Deploying to UAT'
                    }
                }
            }
        }
    }
}

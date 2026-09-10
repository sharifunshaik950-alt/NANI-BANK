pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat '"C:\\Python314\\python.exe" -m pip install -r requirements.txt'

            }
        }

        stage('Check Python Files') {

            steps {

                bat '"C:\\Python314\\python.exe" -m compileall .'

            }
        }
    }
}
pipeline {
    agent any
    
    stages {
        stage('Clonar Repositorio') {
            steps {
                // Clonar el repositorio de GitHub
                git 'https://github.com/alvaro2042/app_credi-banco.git'
            }
        }
        
        stage('Ejecutar Pruebas Unitarias') {
            steps {
                // Pruebas unitarias
                sh 'python -m unittest discover test'
            }
        }
        
        stage('Analizar Calidad del Código') {
            steps {
                // Analizar la calidad del código con SonarQube
                withSonarQubeEnv('http://localhost:9000') {
                    sh 'sonar-scanner'
                }
            }
        }
        
        stage('Construir y Subir Imagen Docker') {
            steps {
                // Construccion imagen de Docker
                sh 'docker build -t alvaro2042/app_credi-banco:latest .'
                
                // login Docker Hub
                sh 'echo dckr_pat_sIvPJ_rFBpwicBNIi8JTrEaF5ZQ | docker login --username alvaro2042 --password-stdin'
                }
                
                // Subir la imagen a Docker Hub
                sh 'docker push alvaro2042/app_credi-banco:latest'
            }
        }
    }
    
    post {
        always {
        }
    }
}


pipeline {
    agent any
    
    stages {
        stage('Clonar Repositorio') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'Github', variable: 'GITHUB_TOKEN')]) {
                	checkout([$class: 'GitSCM', 
                    	    branches: [[name: '*/develop']],
                    	    doGenerateSubmoduleConfigurations: false, 
                            extensions: [[$class: 'CleanCheckout']], 
                            submoduleCfg: [], 
                            userRemoteConfigs: [[
                        	credentialsId: 'Github', 
                        	url: "https://alvaro2042:${env.GITHUB_TOKEN}@github.com/alvaro2042/app_credi-banco.git"
                    	    ]]
                	])
            	    }
        	}
            }
        }
        
        stage('Ejecutar Pruebas Unitarias') {
            steps {
                // Pruebas unitarias
                sh 'python -m unittest discover tests'
            }
        }
        
        stage('Analizar Calidad del Código en SonarCloud') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube Scanner'
                    withSonarQubeEnv('SonarCloud') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=bf36a1da232c8d349ad360db3426e731f6c84f20"
                    }
                }
            }
        }
        
        stage('Construir y Subir Imagen Docker') {
            steps {
                // Construccion imagen de Docker
                sh 'docker build -t alvaro2042/app_credi-banco:latest .'
                
                // login Docker Hub
                sh 'echo dckr_pat_sIvPJ_rFBpwicBNIi8JTrEaF5ZQ | docker login --username alvaro2042 --password-stdin' 
                
                // Subir la imagen a Docker Hub
                sh 'docker push alvaro2042/app_credi-banco:latest'
            }
        }
    }   
}

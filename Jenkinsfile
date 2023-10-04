pipeline {
    agent any
    
    stages {
        stage('Clonar Repositorio') {
            steps {
		script {
		    git credentialsId: 'GithubSecret', url: 'https://github.com/alvaro2042/test_credi-banco.git', branch: 'develop'
            	    
        	}
            }
        }
        
        stage('Ejecutar Pruebas Unitarias') {
            steps {
                // Pruebas unitarias
                sh 'python3 -m unittest discover test'
            }
	    post {
        	always {
            	    junit '**/test-*.xml'
        	}
    	    }
        }
        
        stage('Analizar Calidad del Cidigo en SonarCloud') {
            steps {
                script {
                    def scannerHome = tool 'SonarCloud'
                    withSonarQubeEnv('SonarCloud') {
                        sh """
			${scannerHome}/bin/sonar-scanner \
			-Dsonar.projectKey=alvaro2042_test_credi-banco\
			-Dsonar.organization=alvaro2042 \
			-Dsonar.sources=. \
		 	-Dsonar.login=bf36a1da232c8d349ad360db3426e731f6c84f20
			"""
                    }
                }
            }
        }
        stage('Construir y Subir Imagen Docker') {
            steps {
		// Eliminar contenedor existente
        	sh 'docker stop app-credibanco || true'
        	sh 'docker rm -f app-credibanco || true'

        	// Eliminar la imagen
        	sh 'docker rmi -f alvaro2042/app_credi-banco:latest || true'
                
		// Construccion imagen de Docker
                sh 'docker build -t alvaro2042/app_credi-banco:latest .'
                
                // login Docker Hub
                sh 'echo dckr_pat_sIvPJ_rFBpwicBNIi8JTrEaF5ZQ | docker login --username alvaro2042 --password-stdin' 
                
                // Subir la imagen a Docker Hub
                sh 'docker push alvaro2042/app_credi-banco:latest'
		
		// Lanzar el contenedor
        	sh 'docker run -d --name app-credibanco -p 5000:5000 alvaro2042/app_credi-banco:latest'
            }
        }
    }
}

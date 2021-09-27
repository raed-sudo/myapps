pipeline{
	agent any
	stages{
		stage('Build'){
				steps{
					echo ' THIS IS BUILD STEP ';
					sh ' echo /etc/hostname;'
					}
				}
		stage('Deploy'){
				steps{
					echo ' THIS IS DEPLOY STEP'
					sh ' systemctl restart tomcat'
					}	
				
				}
		}		
	}

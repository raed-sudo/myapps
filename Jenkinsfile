pipeline{
	agent any
	stages{
		stage('Build'){
				steps{
					echo ' THIS IS BUILD STEP ';
					sh ' cd /root/myapps ;rm myapps;  jar -cvf myapps.war index.html ; '
					sh 'ls /root/myapps ;'
					}
				}
		stage('Deploy'){
				steps{
					echo ' THIS IS DEPLOY STEP'
					}	
				
				}
		}		
	}

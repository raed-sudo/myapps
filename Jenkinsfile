pipeline{
	agent any
	stages{
		stage('Build'){
				steps{
					echo ' THIS IS BUILD STEP ';
					sh ' cd /root/myapps ;  jar -cvf myapps.war index.html ; '
					sh 'ls /root/myapps/myapps.war ;'
					}
				}
		stage('Deploy'){
				steps{
					echo ' THIS IS DEPLOY STEP'
					sh 'sudo mv /root/myapps/myapps.war /var/lib/tomcat/webapps/'
					sh 'sudo systemctl restart tomcat'
					}	
				
				}
		}		
	}

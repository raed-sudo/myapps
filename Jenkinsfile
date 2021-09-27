pipeline{
	agent any
	stages{
		stage('Build'){
				steps{
					echo ' THIS IS BUILD STEP ';
					sh ' cd /root/myapps ;  jar -cvf myapps.war index.html ; '
					sh 'ls /root/myapps/myapps.war ;'
					archiveArtifacts artifacts: '/root/myapps/myapps.war'
					}
				}
		stage('Deploy'){
				steps{
					echo ' THIS IS DEPLOY STEP'
					sh 'sudo  systemctl stop tomcat'
					sh 'sudo  rm -rf /var/lib/tomcat/webapps/*'
					sh 'cp -f /root/myapps/myapps.war /var/lib/tomcat/webapps/'
					sh 'sudo  systemctl start tomcat'
				}	
				
				}
		}		
	}

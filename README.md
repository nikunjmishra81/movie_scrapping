# movie_scrapping



__This Project will scrap movie data on daily basis from IMDB Site : https://www.imdb.com/search/title/?genres=thriller&title_type=feature&explore=genres

* Requirements To run this project You need 

	1. Windows/Ubuntu instance
	2. Docker and docker-compose Installed
	3. Git Installed

* To install Docker

	On windows
	
		1. You can directly download from Docker site https://hub.docker.com/editions/community/docker-ce-desktop-windows/
		
		2. Docker compose is attached with docker while downloading from windows
		
	
	On ubuntu
	
		1. sudo apt update
		
		2. sudo apt install docker.io
		
		3. To check installed or not use command
			docker --version
			& output should be
			Docker version 19.03.8, build afacb8b7f0
		
		4. sudo systemctl status docker(docker is stopped now)
		
		5. sudo systemctl start docker
		
		6. sudo systemctl status docker
			Loaded: loaded (/lib/systemd/system/docker.service; disabled; vendor prese>
			
			Active: active (running) since Sun 2021-04-04 11:28:14 UTC; 5s ago
			
			TriggeredBy: ● docker.socket
			
			Docs: https://docs.docker.com
			
			Main PID: 15092 (dockerd)
			
			Tasks: 8
			
			Memory: 43.2M
			
			CGroup: /system.slice/docker.service
			     └─15092 /usr/bin/dockerd -H fd:// --containerd=/ru

* To install docker-compose
		
	on ubuntu
	
		1. sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

		2. sudo chmod +x /usr/local/bin/docker-compose

* To Install git
	On Windows
	
		1. You can directly download from https://git-scm.com/downloads
	On Ubuntu 	
		
		1. sudo apt update 

		2. sudo apt install git

		3. To check installed or not use command
			git --version
			& output should be like
			git version 2.17.1


* To Run this project use commands as follows


		1. Clone the git repo using:

			* git clone https://github.com/nikunjmishra81/movie_scrapping.git

		2. Make sure docker & docker-compose is Up & running
		3. Make sure port 5000 of server is open
		4. Hit the below commands in CMD or terminal(ignore first command if not using ubuntu)(3rd command is copying of env.ini file shared by developer with you)
			* sudo su
			* cd  movie_scrapping
			* cp <source path of env.ini> /src
			* docker-compose up -d
		5. Once the containers gets build up, You can see below image
			

			
![image](https://user-images.githubusercontent.com/35936741/115464546-e1880700-a24a-11eb-927e-102944d8ae77.png)
		
		6. Just check that 1 container(named as backend) are up and running using command
			* docker ps
			You can see below image
			
			
![image](https://user-images.githubusercontent.com/35936741/115464597-f1075000-a24a-11eb-9c9c-7e4a9c90e886.png)


		7. Once the backend container is up, You can hit the get and post API collection shared to you
	


* __Note : 
* __If You get any error you can revert back to developer's email : nikunjmishra8170@gmail.com
* __Makesure before running the project , that Your env.ini file which is shared by developer seperately, is placed inside the "src" folder 
	

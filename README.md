# culiFlask

### Setup MySQL docker container for db


1. set up container
	docker run --name=testculi -e MYSQL_ROOT_PASSWORD=testpw --publish 6603:3306 -d mysql:5.7
2. connect to db
	mysql -h 0.0.0.0 -P 6603 -u root -p



### Create docker bridge network, user defined

1. command
	docker network create culi-net

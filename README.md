# culiFlask

### Setup 

1. install python3.8 and create virtual env 

		python3.8 venv -m venv

2. install dependencies

		pip install -r reqs.txt

### Run

1. setup db

		flask init db
		flask migrate
		flask upgrade

2. run with flask wsgi

		export FLASK_APP=culinapi
		export FLASK_ENV=development

		flask run

3. run with gunicorn 

		gunicorn -w 4 -b 0.0.0.0:5000 "culinapi:create_app()"

### Setup MySQL docker container for db


1. set up container
	docker run --name=testculi -e MYSQL_ROOT_PASSWORD=testpw --publish 6603:3306 -d mysql:5.7
2. connect to db
	mysql -h 0.0.0.0 -P 6603 -u root -p



### Create docker bridge network, user defined

1. command
	docker network create culi-net

NAME?=zbickham
GID=816966
UID=876441

all: stop-all build-all run-all

images:
	- docker images | grep ${NAME}

ps:
	- docker ps -a | grep ${NAME}

api-stop: 
	docker stop ${NAME}-kepler-api && docker rm -f ${NAME}-kepler-api || true

worker-stop:
	docker stop ${NAME}-kepler-wrk && docker rm -f ${NAME}-kepler-wrk || true

db-stop:
	docker stop ${NAME}-kepler-db && docker rm -f ${NAME}-kepler-db || true

api-build:
	docker build -t ${NAME}/kepler-api:0.1 -f docker/Dockerfile.api . 

worker-build:
	docker build -t ${NAME}/kepler-wrk:0.1 -f docker/Dockerfile.wrk .

db-build:
	docker pull redis:6

api-run:
	RIP=$$(docker inspect ${NAME}-kepler-db | grep \"IPAddress\" | head -n1 | awk -F\" '{print $$4}') && \
	docker run --name ${NAME}-kepler-api --env REDIS_IP=$${RIP} -d -p 5003:5000 ${NAME}/kepler-api:0.1

worker-run:
	RIP=$$(docker inspect ${NAME}-kepler-db | grep \"IPAddress\" | head -n1 | awk -F\" '{print $$4}') && \
	docker run --name ${NAME}-kepler-wrk --env REDIS_IP=$${RIP} -d ${NAME}/kepler-wrk:0.1

db-run: db-build
	docker run --name ${NAME}-kepler-db -p 6403:6379 -d -u ${UID}:${GID} -v ${PWD}/data:/data redis:6 --save 1 1

stop-all: api-stop worker-stop db-stop

build-all: db-build api-build worker-build

run-all: db-run api-run worker-run

cycle-api: api-stop api-build api-run

cycle-wrk: wrk-stop wrk-build wrk-run

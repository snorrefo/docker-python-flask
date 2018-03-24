## Testing docker as a development environment for python running flask with restart on code change


to compile/build and run:
docker-compose up

to rebuild all code:
docker-compose up --build

should start a flask server on localhost:5000
Hello World! I have been seen hello3 times.

If using docker toolbox, find server ip from
docker-toolbox ip

docker-compose.yml:
volumes:
  - ./web/src:/code
This command mounts host dir ./web/src to container dir /code , enabling restart of
container every time code changes are made in host dir ./web/src

. means host dir where docker-compose.yml is located
build: ./web means that Dockerfile can be found in host dir ./web

volumes:
  - ./web/src:/code
This command mounts host dir ./web/src to container dir /code , enabling restart of
container every time code changes are made in host dir ./web/src

Dockerfile:
. means host dir where Dockerfile is located
WORKDIR /code means container dir /code
COPY ./src/requirements.txt /tmp/
 left side host, right side container

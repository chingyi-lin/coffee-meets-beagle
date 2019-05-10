# How to build and run this project in a webserver container

The instruction is derived from Kay's slide: https://slides.com/kayashaolu/backend-webarch-running-servers-in-containers#/7

1. This command build the image and tags it with a name that you can refer to later
`docker build -t coffee-meets-beagle .`

2. This command executes an container based on the image built above. It assigns an  environment variable `FLASK_APP`, and it maps `http://localhost:5000` on your host machine to the flask app on port 5000 one he container. 
The `EXPOSE` keyword in the docker file tells docker that the container is communicating on port `5000`, but your docker run command must map that port to a port on the host machine
`docker run -dit --name=coffee-meets-beagle -p 5000:5000 coffee-meets-beagle`

3. To see and follow the logs of a running container (`Ctrl-C` to exit)
`docker logs -f coffee-meets-beagle`

4. Now check http://localhost:5000 on host computer to see if it worked

5. To kill the container, please use:
`docker container kill <container_name>` or `docker rm <container_id>`

###Option 1 Pull docker image from Docker Hub </br>
To run
In terminal run command, enter in <> API key for OMDB and give the container a name.
Th
```shell
 docker run -ti --platform linux/amd64 -e OMDB_API_KEY="<api key>" --name <container_name> nl900/omdb-query
 ```
Follow on screen instructions

###Option 2 Build the image locally###</br>
In the app dir, open terminal and run to build the image giving inside <> a name for the image
```shell
 docker build -t <img_name> . 
 ```

Run the image interactively, enter in <> API key for OMDB and give a name to the container and the image name you ad previously
```shell
docker run -ti -e OMDB_API_KEY= "<api key>" --name <container_name> <img_name>
```

###Re run###</br>
Once you press q in the application, the docker container stops.
To re-run it , need to start the docker container again.
In terminal, run the command below, there's no need to give the API key again
```shell
docker start -i <container_name>
```

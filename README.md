build 
 docker build -t <cisco_img> . 

run interactively
docker run -ti -e OMDB_API_KEY= "<api key>" --name <cisco_container> <cisco_img>

re-running it (no need to enter api key again)
docker start -i <cisco_container>

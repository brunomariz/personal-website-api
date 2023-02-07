# Run from root of project. Command:
# sh shell/build.sh
docker rm -f pw-api
docker rmi -f pw-api

docker build -t pw-api .
docker run -d --name pw-api -p 5000:80 pw-api

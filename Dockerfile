# Travelex test implementation of a simple micro service using Python-Bottle 

# Pull a prebuilt container with Python-Bottle already installed
FROM joshuaconner/hello-world-docker-bottle

# copy a new version of server.py over the one in this container
COPY server.py /home/bottle/server.py

EXPOSE 8080


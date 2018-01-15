# Travelex 
Small project for the Travelex Interview

# Creates a simple REST API implementing the following 2 APIs

## /api/v1/countries/source
returns a json list of countries in { name, isoCode } that can be transfered from

## /api/v1/countries/destination
returns a json list of countries in { name, isoCode } that can be transfered to

# Pull the repo
git pull 

# Start the server using docker
cd ./travelex
docker build -t lester/bottle .
docker run -itd --rm --name="bottle" -p 8080:8080 lester/bottle

## Run the unit tests on the local machine (requires: python 2.7 with requests)
cd ./travelex
pythoon tests.py


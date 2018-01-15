from bottle import route, run, response
import json 

def fetchData(target):
	if target == "source":
		# Retrieve data from a DB e.g. MySQL
		# "SELECT name, isoCode FROM countries WHERE target=SOURCE ORDER BY name"
		# SOURCE is a MySQL enum
		data = [
			{ "name" : "Australia",		 "isoCode" : "AU" },
			{ "name" : "Ireland", 		 "isoCode" : "IE" },
			{ "name" : "Japan", 		 "isoCode" : "JP" },
			{ "name" : "Poland", 		 "isoCode" : "PL" },
			{ "name" : "United Kingdom", "isoCode" : "GB" },
		]
	elif target == "dest":
		# Retrieve data from a DB e.g. MySQL
		# "SELECT name, isoCode FROM countries WHERE target=DEST ORDER BY name" 
		# DEST is a MySQL enum
		data = [
			{ "name" : "France",    "isoCode" : "FR" },
			{ "name" : "Germany",   "isoCode" : "DE" },
			{ "name" : "Spain", 	"isoCode" : "SP" },			
		]
	else:
		## May need to return this in json as that is what the caller is expecting
		return "error"

	# Convert the data dict to json an return it
	return json.dumps(data)

@route('/api/v1/countries/source', method='GET')
def source():
	response.content_type = 'application/json'
	return fetchData("source")

@route('/api/v1/countries/destination', method='GET')
def destination():
	response.content_type = 'application/json'
	return fetchData("dest")	

run(host='0.0.0.0', port=8080, debug=True)


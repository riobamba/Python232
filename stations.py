import json
import requests

class Stations:
	"""docstring for Stations """
	def __init__(self):
		response = requests.get("http://10.100.100.232:8081/query/stations.json")
		if response.status_code == 200:
		   results = response.json()
		   for result in results['Inventory']['network']:
		       for station in result['station']:
			       	for location in station['sensorLocation']:
			       		for channel in location['stream']:
			       			print result['code'],station['code'],location['code'],channel['code']
		else:
		   print "Error code %s" % response.status_code






app = Stations()
		
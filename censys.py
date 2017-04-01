import sys
import json
import requests
   
API_URL = "https://www.censys.io/api/v1"
UID = "02c06402-a862-4ccb-addb-dfe13ff37d56"
SECRET = "5PKzasYccj92E5UeFi6MES4MtVt6YxWk"

data = {
    "query":"80.http.get.headers.server: apache", 
    "page":1, 
    "fields":["ip", "location.country"]
}

res = requests.post(API_URL + "/search/ipv4", data=json.dumps(data), auth=(UID, SECRET))
results = res.json()
if res.status_code != 200:
    print "error occurred: %s" % results["error"]
    sys.exit(1)
for result in results["results"]:
    print "%s in %s" % (result["ip"], result["location.country"][0])
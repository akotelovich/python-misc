import sys
import csv
import json
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from jinja2 import Environment, FileSystemLoader

$ip='10.91.107.213'
$adm_user='admin'
$adm_passwd='passwd'

env = Environment(loader = FileSystemLoader('.'))
print("Please paste device data in the following format:\nhostname,ip-address,vendor,model,username,password\n")
reader = csv.reader(sys.stdin)
for row in reader:
  #print(row)
  t = env.get_template('tufin-add-device.jinja')
  o = t.render(name = row[0], ip = row[1], vendor = row[2], model = row[3], username = row[4], password = row[5])
  
  url = 'https://'+$ip+'/securetrack/api/devices/bulk.json'
  #payload = json.loads(o)
  #curl -X POST -H "Content-Type: application/json" --data @add-device.json https://10.0.1.2/securetrack/api/devices/bulk.json --user "admin:passwd" --insecure
  headers = {'content-type': 'application/json'}
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  r = requests.post(url, data=o, headers=headers, verify=False, auth = HTTPBasicAuth($adm_user, $adm_password))
  print (r.text)
  

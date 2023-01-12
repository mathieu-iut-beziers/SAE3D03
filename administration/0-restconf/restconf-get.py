# import json
# import requests
# requests.packages.urllib3.disable_warnings()

# ############### GET ###############

# api_url="https://10.202.17.200/restconf/data/ietf-interfaces:interfaces"

# headers={"Accept":"application/yang-data+json","Content-type":"application/yang-data+json"}

# basicauth=("admin1", "Root123#")

# resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

# print(resp)

# response_json = resp.json()

# print(json.dumps(response_json, indent=4))

############### POST ###############
import json
import requests
requests.packages.urllib3.disable_warnings()

headers={"Accept":"application/yang-data+json","Content-type":"application/yang-data+json"}

basicauth=("admin1", "Root123#")

api_url2 = "https://10.202.17.200/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"

YangConfig = {
"ietf-interfaces:interface": {
    "name": "Loopback2",
    "description": "La loopback deux retour",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
        "address": [
            {
                "ip": "5.5.5.5",
              "netmask":"255.255.255.255"
            }
        ]
    },
    "ietf-ip:ipv6": {}
    }
}

resp = requests.put(api_url2,data=json.dumps(YangConfig),auth=basicauth,headers=headers,verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Code d\'état : {} \n Message d\'erreur : {} '.format(resp.status_code, resp.json()))

from secrets import *
#import print
import requests

API_URL = "https://api.github.com"
payload = '{"name":"bhagya lakshmi deepika"}'
headers = {
"Authorization": "token " + "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"
"Accept" "application/vnd.github.v3.json"
}

github = requests.post(API_URL+"/user/repos", data=payload, headers=headers)

pprint(github.json())
pprint(github)

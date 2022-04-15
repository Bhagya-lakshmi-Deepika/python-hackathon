import requests
import os
from pprint import pprint
token = os.getenv('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', '...')
owner = "MartinHeinz"
repo = "python-project-blueprint"
query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
params = {"state": "open",}
headers = {'Authorization': f'token {token}'}
r = requests.get(query_url, headers=headers, params=params)
pprint(r.json())

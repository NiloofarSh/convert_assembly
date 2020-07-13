import argparse
import requests, sys


server = "https://grch37.rest.ensembl.org"
ext = "/map/human/GRCh38/X:1000000..1000100:1/GRCh37?"

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
print(repr(decoded))

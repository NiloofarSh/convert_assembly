import requests, sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store', help='your input file')
parser.add_argument('-f', action='store', help ='Name of species')
args = parser.parse_args()

'''
A python program to map slices from GRCh38 assembly to GRCh37 assembly using REST API
Developed by Niloofar Shirvanizadeh 2020.

Usage:
GRCh38_to_GRCh37.py --species=species --file=filename

Example usage:
python3 GRCh38_to_GRCh37.py -s human -f sample_input.in

'''
file = open(args.f, 'r')
lines = file.readlines()
for line in lines:
    if line[0] != '#':
        i =line.strip().split(':')

server = "https://grch37.rest.ensembl.org"
ext = '/map/human/' + i[1] + '/' + i[2] + ':' + i[3] + '..' + i[4] + ':' + i[5] + '/GRCh37?'

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
print(repr(decoded))


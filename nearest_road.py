import googlemaps
import argparse

from datetime import datetime

# Secure way
parser = argparse.ArgumentParser(description='Google Key')
parser.add_argument('key', type=str, help='Write your google key')
args = parser.parse_args()

key = args.key

print(key)

gmaps = googlemaps.Client(key=key)

nearest = gmaps.nearest_roads(points='60.170880,24.942795|60.170879,24.942796|60.170877,24.942796')

print(nearest)
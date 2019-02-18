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

nearby = gmaps.places_nearby(
                            location=(4.6580162, -74.1097673),
                            radius=1500,
                            type='restaurant',
                            )

print(nearby)
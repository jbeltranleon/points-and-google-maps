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

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print(geocode_result)
print(reverse_geocode_result)
print(directions_result)
#!/usr/bin/env python3
"""
Usage: bin/make_geojson.py [<yaml_file> | <address>]

Runs through all the documents in a YAML file, looking for `coordinates`, and
then creates a GeoJSON file version of the YAML file. Outputs to stdout.

Example:

  python bin/make_geojson.py hotels.yml > hotels.geojson


Requirements:

  pip3 install PyYAML geopy
"""
import json
import os
import sys


def format_geojson_from_docs(docs):
    out = {
        'type': 'FeatureCollections',
        'features': []
    }
    for doc in docs:
        data = doc.copy()  # don't modify original for some reason
        coordinates = data.pop('coordinates')
        out['features'].append({
            'type': 'Feature',
            'properties': data,
            'geometry': {
                'type': 'Point',
                'coordinates': coordinates.split(', ')[::-1],
            },
        })
    return out


def geojsonize(path):
    try:
        import yaml
    except ImportError:
        sys.exit('need to install PyYAML')

    with open(path) as fp:
        docs = yaml.load_all(fp)
        # filter and load into memory so the file can be closed
        docs = [x for x in docs if 'coordinates' in x]
    data = format_geojson_from_docs(docs)
    print(json.dumps(data))


def geocode(address):
    try:
        from geopy import geocoders
    except ImportError:
        sys.exit('need to install geopy')

    geolocator = geocoders.Nominatim()  # you may also want to try GoogleV3
    location = geolocator.geocode(address)
    print(location.address)
    print('{}, {}'.format(location.latitude, location.longitude))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    if os.path.exists(path):
        geojsonize(path)
    else:
        geocode(path)

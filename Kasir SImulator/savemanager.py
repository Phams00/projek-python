import json
import os

def save(status):
    status_data = status.to_dict()
    with open('status.json', 'w') as f:
        json.dump(status_data, f, indent=4)
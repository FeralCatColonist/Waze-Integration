#! python3
# Waze_JSON_Pull, pulls down Waze feed from URL to write location.
import requests
import json
import time
import os

timestamp = time.strftime('%m.%d.%H%M')

WazeURL = #Your Waze CCP URL HERE
print(os.getcwd())
print(timestamp)
save_path = r'D:\_WazeJSON_pull'
file_name = r'{}.json'.format(timestamp)
complete_name = os.path.join(save_path, file_name)
print(complete_name)

response = requests.get(WazeURL)

print(response.json())
with open(complete_name, 'w') as file:
	json.dump(response.json(), file)


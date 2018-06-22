#! python3
# Waze_XML_Pull, pulls down Waze feed from URL to write location.
import requests
import time
import os

timestamp = time.strftime('%m.%d.%H%M')

WazeURL = #Your Waze CCP URL HERE
print(os.getcwd())
print(timestamp)
save_path = r'D:\_WazeXML_pull'
file_name = r'{}.xml'.format(timestamp)
complete_name = os.path.join(save_path, file_name)
print(complete_name)

response = requests.get(WazeURL)
with open(complete_name, 'wb') as file:
	file.write(response.content)

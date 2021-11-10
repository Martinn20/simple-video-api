import requests
import time
BASE = "http://127.0.0.1:5000"


response = requests.put(BASE + "/video/1", {'likes': 1, 'views': 1, 'name': "Baby video"});
print(response)
time.sleep(2)
response = requests.put(BASE + "/video/1", {'likes': 1, 'views': 1, 'name': "Baby video"});
print(response)
time.sleep(2)
response = requests.put(BASE + "/video/2", {'likes': 123, 'views': 231, 'name': "Baby video 2"});
print(response)
time.sleep(2)
response = requests.get(BASE + "/video/1");
print(response)
time.sleep(1)
response = requests.patch(BASE + "/video/1", {'views': 99});
print(response)
time.sleep(1)
response = requests.get(BASE + "/video/1");
print(response.json())
time.sleep(1)
response = requests.delete(BASE + "/video/1");
print(response)
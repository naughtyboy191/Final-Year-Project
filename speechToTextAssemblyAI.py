import sys
import time
import requests
from playsound import playsound

# filename = "machine-learning_speech-recognition_16-122828-0002.wav"
# filename="sample-0.mp3"

# filename="final.mp3"
# filename = "harvard.wav"
filename="harvard1.wav"
# filename="harvard2.wav"

# playsound(filename)

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization': "5f2ff64ecc064e598ea8b39587c1954d"}
response = requests.post('https://api.assemblyai.com/v2/upload',
                         headers=headers,
                         data=read_file(filename))

res=response.json()
# print(res["upload_url"])


endpoint = "https://api.assemblyai.com/v2/transcript"

json = {
  "audio_url": res["upload_url"]
}

headers = {
    "authorization": "5f2ff64ecc064e598ea8b39587c1954d",
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)

Res=response.json()
# print(Res["id"])

while response.json()["status"]!="completed":
    endpoint = "https://api.assemblyai.com/v2/transcript/"+Res["id"]

    headers = {
        "authorization": "5f2ff64ecc064e598ea8b39587c1954d",
    }

    response = requests.get(endpoint, headers=headers)
print()
print("Result : ",response.json()["text"])




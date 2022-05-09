import requests
import time

# curl -L -X POST https://asr.api.speechmatics.com/v2/jobs/ -H "Authorization: Bearer vN9Mkji45rWCxB9iKiQJy3B7CiPT5bwB" -F data_file=@harvard1.wav -F config='{"type": "transcription","transcription_config": { "operating_point":"enhanced", "language": "en" }}'

# curl -L -X GET "https://asr.api.speechmatics.com/v2/jobs/INSERT_JOB_ID/transcript?format=txt" -H "Authorization: Bearer vN9Mkji45rWCxB9iKiQJy3B7CiPT5bwB"

filename="harvard1.wav"
url='https://asr.api.speechmatics.com/v2/jobs/'
def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'Authorization': "Bearer vN9Mkji45rWCxB9iKiQJy3B7CiPT5bwB"}
data_dict={"config":'{"type": "transcription","transcription_config": { "operating_point":"enhanced", "language": "en" }}'}

# UPLOAD DATA
response = requests.post(url,headers=headers,files={"data_file":open(filename,'rb')},data=data_dict)

res=response.json()
job_id=response.json()["id"]
print("Job Id:",job_id)
time.sleep(1)
response=requests.get(url+job_id+"/transcript?format=txt",headers=headers)

while "running" in response.json()["detail"]:
    response=requests.get(url+job_id+"/transcript?format=txt",headers=headers)
    # print(response.text)
    print(".",end="")

    try:
        res=response.json()
    except:
        break

print()
print("Result : ",response.text)
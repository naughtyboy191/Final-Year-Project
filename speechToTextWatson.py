from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

apikey = 'OtvtJXZvRLv7CWJURpDtirlKzpMOMcjeKpY201ZDVvz7'
url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/89fdd9cc-c5c5-4cb6-908e-ba3e3143f80d'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)

stt.set_service_url(url)
# filename="final.mp3"
# filename="test3.wav"
# filename="Welcome.mp3"
# filename = "sample-0.mp3"
# filename = "machine-learning_speech-recognition_16-122828-0002.wav"
# filename="harvard.wav"
filename="harvard1.wav"
# playsound(filename)
with open(filename, 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-US_NarrowbandModel',split_transcript_at_phrase_end=True).get_result()
# print(res)

i=0
print()
print("Result : ")
while res['results'][i]['end_of_utterance']!='end_of_data':
    print(res['results'][i]['alternatives'][0]['transcript'])
    i=i+1
print(res['results'][i]['alternatives'][0]['transcript'])

# split_transcript_at_phrase_end=true
# end_of_phrase_silence_time=0.8
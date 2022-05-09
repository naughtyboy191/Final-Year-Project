import sys
import time
import requests
# from playsound import playsound
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer

# filename="final.mp3"
# filename="Welcome.mp3"
# filename = "machine-learning_speech-recognition_16-122828-0002.wav"
# filename="sample-0.mp3"
# filename = "harvard.wav"
filename="input_speech.wav"
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
print("Result of speech to text : ",response.json()["text"])


#Text summariation
text=response.json()["text"]

# text="Thank you for choosing the Olympus Dictation Management System the Olympus Dictation Management System" \
#      " gives you the power to manage your dictations transcriptions and documents seamlessly and to improve the productivity of your daily work. " \
#      "For example, you can automatically send the Dictation files or transcribe documents to your assistant or the author via email or FTP." \
#      "We hope you enjoy the simple, flexible, reliable, and secure solutions from Olympus."

stop_words = stopwords.words("english")
stop_words.append(".")
stop_words.append(",")

# print("stop words",stop_words)
words = word_tokenize(text)
# print(words)
sentences = sent_tokenize(text)
# print(sentences)

#creating hashmap (frequency table)
ps = PorterStemmer()
hash_map=dict()
for wd in words:
        wd=ps.stem(wd)
        if wd in stop_words:
            continue
        if wd in hash_map:
            hash_map[wd] += 1
        else:
            hash_map[wd] = 1
# print(hash_map)


#calculating sentences score
sentence_score=dict()
for sen in sentences:
       sentence_length = (len(word_tokenize(sen)))
       wordcount = 0
       for word in hash_map:
              if word in sen.lower():
                     wordcount+=1
                     if sen in sentence_score:
                            sentence_score[sen]+=hash_map[word]
                     else:
                            sentence_score[sen] = hash_map[word]
       sentence_score[sen]=sentence_score[sen]/(wordcount)

# print(sentence_score)

#calculating average score
sum_val=0
for x in sentence_score:
       sum_val+=sentence_score[x]
avg_score=sum_val/len(sentence_score)
# print(avg_score)

#
summary=""
for sentence in sentences:
       if sentence in sentence_score and sentence_score[sentence]>=avg_score:
              summary+=" "+sentence

print()
print("Summary of the paragraph:")
print(summary)



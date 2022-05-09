import speech_recognition as sr
from playsound import playsound


# filename = "harvard.wav"
filename="harvard1.wav"
# filename="final.mp3"
# filename="final.wav"

# playsound(filename)

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
    # r.adjust_for_ambient_noise(source,duration=0.5)
    # r.energy_threshold += 280
    audio_data = r.record(source)
    # print(type(audio_data))
text= r.recognize_google(audio_data)
print()
print("Result : ",text)









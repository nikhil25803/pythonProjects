from gtts import gTTS

# For a quick mp3 file
# tts = gTTS('hello', lang='en')
# tts.save('hello.mp3') 

from playsound import playsound

audio='speech.mp3'
language='en'
sp=gTTS(text="Hello World ! My name is Nikhil Raj",lang=language,slow=False)

sp.save(audio)
playsound(audio)
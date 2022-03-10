from gtts import gTTS

def play_sound(lang1, lang2, lang3, lang4, lang5):

    lang1.save('english.mp3')

    lang2.save('french.mp3')

    lang3.save('mandarin.mp3')

    lang4.save('portuguese.mp3')

    lang5.save('spanish.mp3')

    print("All mp3 files are created")


english = gTTS('Good Morning', lang='en')
french = gTTS('bon matin', lang='fr')
mandarin = gTTS('Zǎoshang hǎo', lang='zh-TW')
portuguese = gTTS('bom dia', 'pt')
spanish = gTTS('buenos días', 'es')
play_sound(english, french, mandarin, portuguese, spanish)

from playsound import playsound

audio=['english.mp3', 'french.mp3', 'mandarin.mp3', 'spanish.mp3']

for i in audio:
    playsound(i)
import pyttsx3

tts_engine = pyttsx3.init()
tts_engine.setProperty('voice', 'com.apple.speech.synthesis.voice.moira.premium')

class TextToSpeech:
  def say(self, message):
    tts_engine.say(message)
    tts_engine.runAndWait()

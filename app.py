from src.speech_recognition.speech_recognizer import SpeechRecognizer
from src.text_to_speech.text_to_speech import TextToSpeech
from src.commands.resolver import CommandResolver

speaker = TextToSpeech()
speech_recognizer = SpeechRecognizer()
command_resolver = CommandResolver()

if __name__ == "__main__":
  print('you can speak now')
  audio = speech_recognizer.get_audio_from_mic()
  interpreted_speech = speech_recognizer.recognize_speech_from_audio(audio)

  print('command interpreted: %(interpreted_speech)s' % locals())

  response = command_resolver.response_from_speech(interpreted_speech)

  speaker.say(response)

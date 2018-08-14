from src.speech_recognition.speech_recognizer import SpeechRecognizer
from src.text_to_speech.text_to_speech import TextToSpeech
from src.commands.resolver import CommandResolver

speaker = TextToSpeech()
speech_recognizer = SpeechRecognizer()
command_resolver = CommandResolver()

testing = True
test_phrase = "what's the weather like today?"

if __name__ == "__main__":
  if not testing:
    print('you can speak now')
    audio = speech_recognizer.get_audio_from_mic()
    interpreted_speech = speech_recognizer.recognize_speech_from_audio(audio)
  else:
    interpreted_speech = test_phrase

  print('command interpreted: %(interpreted_speech)s' % locals())

  response = command_resolver.response_from_speech(interpreted_speech)

  if not testing:
    speaker.say(response)
  else:
    print('RESPONSE: ' + response)

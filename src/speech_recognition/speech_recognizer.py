import speech_recognition

recognizer = speech_recognition.Recognizer()

mic = speech_recognition.Microphone()

class SpeechRecognizer:
  def get_audio_from_mic(self):
    with mic as source:
      audio = recognizer.listen(source)
    return audio

  def recognize_speech_from_audio(self, audio):
    return recognizer.recognize_google(audio)

import speech_recognition

recognizer = speech_recognition.Recognizer()

mic = speech_recognition.Microphone()

class SpeechRecognizer:
  # Accepts google or sphinx
  current_recognition_software = 'google'

  def get_audio_from_mic(self):
    with mic as source:
      recognizer.adjust_for_ambient_noise(source)
      audio = recognizer.listen(source)
    return audio

  def recognize_speech_from_audio(self, audio):
    return getattr(recognizer, 'recognize_' + self.current_recognition_software)(audio)

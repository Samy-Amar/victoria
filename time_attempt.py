import time
def my_func(speech):
  if 'what time' not in speech.lower():
    return None

  return 'It is currently ' + time.strftime('%l %M %p')

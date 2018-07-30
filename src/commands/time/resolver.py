import time
from datetime import datetime
from pytz import timezone

class TimeResolver():
  time_format = '%l %M %p'
  def matches_time_command(self, speech):
    speech = speech.lower()
    return 'what time' in speech and 'kitty' not in speech

  def time_answer(self, speech):
    current_local_time = datetime.now()
    return 'The current local time is ' + current_local_time.strftime(self.time_format)


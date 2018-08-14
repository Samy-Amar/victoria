import re as regexp # Importing as regexp because "re" also sounds like "recognition"
from time.resolver import TimeResolver
from weather.resolver import WeatherResolver

class CommandResolver():
  def response_from_speech(self, speech):
    if self.matches_name_command(speech):
      return self.name_answer(speech)

    time_resolver = TimeResolver()
    if time_resolver.matches_time_command(speech):
      return time_resolver.time_answer(speech)

    weather_resolver = WeatherResolver()
    if weather_resolver.matches_weather_command(speech):
      return weather_resolver.weather_answer(speech)

    return self.command_not_found(speech)

  def matches_name_command(self, speech):
    return 'my name is' in speech

  def name_answer(self, speech):
    name = regexp.search(r'.*my name is (\w+)', speech).group(1)
    return 'hello ' + name + ', my name is Victoria'

  def command_not_found(self, speech):
    print(speech)
    return "Sorry, I couldn't quite get that. I've printed out what I think you said."


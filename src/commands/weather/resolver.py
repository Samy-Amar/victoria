import requests
from weather import Weather, Unit

class WeatherResolver():
  def matches_weather_command(self, speech):
    speech = speech.lower()
    return 'weather' in speech

  def weather_answer(self, speech):

    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('paris')
    condition = location.condition

    # Print the status code of the response.
    return str(condition.text)

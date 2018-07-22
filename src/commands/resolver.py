import re as regexp # Importing as regexp because "re" also sounds like "recognition"

class CommandResolver():
  def response_from_speech(self, speech):
    if self.matches_name_command(speech):
      return self.name_answer(speech)
    return self.command_not_found(speech)

  def matches_name_command(self, speech):
    return regexp.search('.*my name is.*', speech) != None

  def name_answer(self, speech):
    name = regexp.search(".*my name is (\w+)", speech).group(1)
    return 'hello ' + name + ', my name is Victoria'

  def command_not_found(self, speech):
    print(speech)
    return "Sorry, I couldn't quite get that. I've printed out what I think you said."


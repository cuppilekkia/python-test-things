import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
  word = w.lower()
  if word in data:
    return data[word]
  elif word.title() in data:
    return data[word.title()]
  elif word.upper() in data:
    return data[word.upper()]
  elif len(get_close_matches(word, data.keys())):
    suggested = get_close_matches(word, data.keys())[0]
    yn = input("Did you mean '%s' instead? [y/n] " % suggested)
    if yn.lower() == "y":
      return data[suggested]
    else:
      return "The word doesn't exist!"
  else:
    return "The word doesn't exist!"

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
  for item in output:
    print("* ", item)
else:
  print(output)
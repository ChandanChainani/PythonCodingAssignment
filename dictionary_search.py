import requests
import json

dictionaryapi_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def error_message():
    print("Something went wrong")

try:
    word = input("> Word? ")
    if (len(word) > 0):
        response = requests.get(dictionaryapi_url + word)
        if response.status_code == 200:
            data = json.loads(response.text)
            try:
                print("Output: %s. Noun. %s" %(data[0]['word'].capitalize(), data[0]['meanings'][0]['definitions'][0]['definition'].capitalize()))
            except Exception as e:
                print("Word not found in dictionary")
        else:
            error_message()
    else:
        print("Please provide word")
except KeyboardInterrupt:
    print("\nProgram closed")
except Exception as e:
    print(e)
    error_message()


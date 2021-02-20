import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("did you mean %s ? enter y/n: " %
                   get_close_matches(word, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "word doesnt exists"
        else:
            return "pls input again"

    else:
        return "data is not available"


w = input("enter your word: ")
output = (translate(w))
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

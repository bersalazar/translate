import sys
import json
import requests
from pprint import pprint
from xml.etree import ElementTree

lang = raw_input("Please enter the language code to translate to: ")
if lang not in ["pt_PT", "de_DE"]:
    print("Invalid option. Available options are pt_PT, de_DE")
    sys.exit(1)

with open('words.json') as f:
    data = json.load(f)

translated_as_object = {
    "words": []
}
for word in data["words"]:
    request = "http://localhost:5000/translate?word=" + str(word["name"]) + "&lang=" + str(lang)
    
    # This is the actual code for handling the request/response using the translation server
    # response = requests.get(request)
    # response = requests.get(request.content)
    # tree = Element.Tree.fromstring(response.content)

    # This is a dummy simulation of the XML response from the server due to lacking the translation server
    print("Simulate a request to " + request)
    response = {
        "content": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><word><id>" + str(word["id"]) + "</id><name>casa</name></word>"
    }
    tree = ElementTree.fromstring(response["content"])
    # End of dummy XML response

    # Read each XML response and add to a dict
    item = {
        "id": tree[0].text,
        "name": tree[1].text
    }
    translated_as_object["words"].append(item)

output_file = "words_translated.json"
with open(output_file, "w") as the_file:
    pprint(translated_as_object, stream=the_file)

print("The translated object is:")
pprint(translated_as_object)
print("The output file with the translation can be found in \'" + output_file + "\'")
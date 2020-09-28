# Python program to read
# json file
import json
# Opening JSON file
f = open('adhar_data.json',)
# returns JSON object as
# a dictionary
data = json.load(f)
# Iterating through the json
# list
for i in data['analyzeResult']:
	print(i)


# Closing file
f.close()

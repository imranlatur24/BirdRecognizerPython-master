# Python program to demonstrate
# Conversion of JSON data to
# dictionary


# importing the module
import json

# Opening JSON file
with open('adhar_data.json') as json_file:
    data = json.load(json_file)
    data_d = json.dumps(data)
    print("dumps",data_d)
    # Print the type of data variable
    print("Type:", type(data))

    # Print the data of dictionary
    #print("\nemp_details:", data['analyzeResult'])
    #print("\nemp_details:", data['documentResults'])

for text in data['analyzeResult']:
    print(text['version'])

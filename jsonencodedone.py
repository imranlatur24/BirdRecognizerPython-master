# importing json library
import json

geek = '{"Name": "nightfury1", "Languages": ["Python", "C++", "PHP"]}'
geek_dict = json.loads(geek)

# prining all elements of dictionary
print("Dictionary after parsing: ", geek_dict)

# printing the values using key
print("\nValues in Languages: ", geek_dict['Languages'])


input_file = open ('stores-small.json')
json_array = json.load(input_file)
store_list = []

for item in json_array:
    store_details = {"name":None, "city":None}
    store_details['name'] = item['name']
    store_details['city'] = item['city']
    store_list.append(store_details)

print(store_list)
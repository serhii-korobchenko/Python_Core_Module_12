import json

dict =  {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
with open ("your_json_file.txt", 'w') as f:
    json.dump(dict, f)



with open("your_json_file.txt", 'r') as f:
    data = json.loads(f.read()) #data becomes a dictionary



#and then just write the data back on the file
with open("your_json_file.txt", 'w') as f:
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
#I added some options for pretty printing, play around with them!
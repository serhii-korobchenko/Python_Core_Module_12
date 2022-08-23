import json


some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
file_name = 'data.json'

with open(file_name, "w") as fh:
    json.dump(some_data, fh)


with open(file_name, "r") as fh:
    unpacked = json.load(fh)


print(unpacked is some_data)    # False
print(unpacked == some_data)    # False

print(unpacked['key'] == some_data['key'])    # True
print(unpacked['a'] == some_data['a'])         # True
print(unpacked['2'] == some_data[2])           # True
print(unpacked['tuple'] == [5, 6])          # True
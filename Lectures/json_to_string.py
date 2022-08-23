import json


some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

byte_string = json.dumps(some_data)
unpacked = json.loads(byte_string)

unpacked is some_data    # False
unpacked == some_data    # False

unpacked['key'] == some_data['key']     # True
print(unpacked['key'] == some_data['key']  )
unpacked['a'] == some_data['a']         # True
print( unpacked['a'] == some_data['a'] )
unpacked['2'] == some_data[2]           # True
print( unpacked['2'] == some_data[2]     )
unpacked['tuple'] == [5, 6]             # True
print(unpacked['tuple'] == [5, 6])
import copy  # use  for more than 1 level of nesting


my_list = [1, 2, {1: 'a'}]
copy_list = copy.deepcopy(my_list)
copy_list.append(4)
print(my_list)      # [1, 2, {1: 'a'}]
print(copy_list)    # [1, 2, {1: 'a'}, 4]

copy_list[2][2] = 'b'
print(my_list)    # [1, 2, {1: 'a'}]
print(copy_list)  # [1, 2, {1: 'a', 2: 'b'}, 4]    ----> !!!
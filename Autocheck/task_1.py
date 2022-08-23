import pickle

dict =  {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}


def write_contacts_to_file(filename, contacts):
    with open (filename, 'wb') as fh:
        pickle.dump(contacts, fh)

    
        


def read_contacts_from_file(filename):
    with open (filename, 'rb') as fh:
        unpacked = pickle.load(fh)
        return unpacked


write_contacts_to_file ('test1.txt', dict)
red = dict
print(dict is red)

print("id(dict)", id(dict))


print("id(red)", id(red))
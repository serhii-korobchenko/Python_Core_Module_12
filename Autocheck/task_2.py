import json

dict =  [
    {
   "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": False
},  
{
   "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": False
}]



def write_contacts_to_file(filename, contacts):

    
  
    with open (filename, 'w') as fh:
        json.dump({'contacts': [x for x in contacts]}, fh)
           


def read_contacts_from_file(filename):
    with open (filename, 'r') as fh:
        
        unpacked_dict = json.load(fh)
        return unpacked_dict['contacts']
           


write_contacts_to_file('test2.json', dict)
print (read_contacts_from_file('test2.json'))



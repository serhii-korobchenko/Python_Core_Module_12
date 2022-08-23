import pickle
import copy



class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
       
    def __init__(self, filename: str, contacts: list[Person] = None):
                       
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts        
        self.count_save = 0
        self.is_unpacking = False
              
    def save_to_file(self):             
        with open(self.filename, "wb") as file:                        
            pickle.dump(self, file)

    def read_from_file(self):       
        with open(self.filename, "rb") as file:            
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['count_save'] += 1              
        return attributes


    def __setstate__(self, value): # write data from file to class attributes
        self.__dict__ = value
        self.__dict__['is_unpacking'] = True
   
def copy_class_person(person):
    return copy.copy(person)



def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]  

persons = Contacts("user_class.dat", contacts)
print(dir(persons))
new_persons = copy_class_contacts(persons)

new_persons.contacts[0].name = "Another name"

print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name
    
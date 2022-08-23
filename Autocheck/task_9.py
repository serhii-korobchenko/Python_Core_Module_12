import pickle
import copy



class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


    def __copy__(self):
        
        copy_obj = Person (self.name, self.email, self.phone, self.favorite )
        #copy_obj.name = self.name
        #copy_obj.email = self.email
        #copy_obj.phone = self.phone
        #copy_obj.favorite = self.favorite
        print('*COPY*')
        return copy_obj
        


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
   
    
    def __copy__(self):
        copy_obj = Contacts(self.filename, self.contacts)
        #copy_obj.filename = self.filename
        #copy_obj.contacts = self.contacts
        #copy_obj.count_save = self.count_save
        #copy_obj.is_unpacking = self.is_unpacking
        return copy_obj
        

    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename, self.contacts)
        memo[id(copy_obj)] = copy_obj
        copy_obj.contacts = copy.deepcopy(self.contacts)
        print('*DEEPCOPY*')
        return copy_obj

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

person_1 = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

person_2 = copy.copy(person_1)
print(person_2.__dict__)

contact_1 = Contacts("user_class.dat", contacts)

contact_2 = copy.deepcopy(contact_1)
print(contact_2.__dict__)
print(contact_2.contacts[1].__dict__)
#new_persons.contacts[0].name = "Another name"

#print(persons.contacts[0].name)  # Allen Raymond
#print(new_persons.contacts[0].name)  # Another name
import csv

dict =   [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False
}]



def write_contacts_to_file(filename, contacts):

    
  
    with open (filename, 'w', newline='') as fh:
        fields_names = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter (fh, fieldnames=fields_names)
        writer.writeheader()
        for item in contacts:        
            writer.writerow(item)
           


def read_contacts_from_file(filename):
    final_list =[]
    with open (filename, 'r', newline='') as fh:
        for row in csv.DictReader(fh):
            if row['favorite'] == 'False':
                row['favorite'] = False
            elif row['favorite'] == 'True':
                row['favorite'] = True
            final_list.append(row)

        
        return final_list



write_contacts_to_file('test3.csv', dict)
print (read_contacts_from_file('test3.csv'))



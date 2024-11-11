'''
    @Author: VEMULA DILEEP
    @Date: 07-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 07-11-2024
    @Title : Address Book 

'''


import log

log = log.logger_init('AddressBookProblem')

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}")

class AddressBook:
    def __init__(self):
        self.contacts = {}
        
    
    
class AddressBookMain:
    def __init__(self):
        
      self.address_books ={}

    def welcome_message(self):
        '''
        Description:
             printing welcome message
        parameters:
             self as a parameter
        Return:
             none
        '''
        print("WELCOME TO ADDRESS BOOK PROGRAM")
                

def main():
    address_main = AddressBookMain() 
    address_main.welcome_message()
    
if __name__=="__main__":
    main()
    
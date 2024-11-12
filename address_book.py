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
    def add_contact(self, contact):
      '''
        Description:
            function to add contact
        parameters:
             self as a parameter
        Return:
             none
      '''
      key = f"{contact.first_name} {contact.last_name}"  
      if key not in self.contacts:
          
       self.contacts[key] = contact
       log.info(self.contacts.items())
       log.info(f"Contact {key} added successfully.")
       
      else:
       log.info(f"{key} contact already exists")   
        
    def edit_contact(self, f_name, l_name):
        key = f"{f_name} {l_name}"
        if key not in self.contacts:
            log.info(f"{key} not found in Contacts")
        else:
            self.contacts[key].address = input("Enter new address: ")
            self.contacts[key].city = input("Enter new city: ")
            self.contacts[key].state = input("Enter new state: ")
            self.contacts[key].zip_code = input("Enter new zipcode: ")
            self.contacts[key].phone = input("Enter new phone number: ")
            self.contacts[key].email = input("Enter new email: ")
            
    def delete_contact(self, f_name, l_name):
     """
     Description:
        Deletes a contact from the address book based on the first and last name.
    Parameters:
        f_name (str): First name of the contact to delete.
        l_name (str): Last name of the contact to delete.
    Return:
        None
     """
     key = f"{f_name} {l_name}"
     if key in self.contacts:
        del self.contacts[key]
        log.info(f"Contact {key} deleted successfully.")
     else:
        log.info(f"Contact {key} not found in the address book.")
    
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
    
    def add_contact_console(self):
        '''
        Description:
             function to take input from console to add contact
        parameters:
             self as a parameter
        Return:
             none
        '''
        key = input("enter the Adress book key: ")
        print("Enter the following contact details:")
        if key in self.address_books:
            
         first_name = input("First Name: ")
         last_name = input("Last Name: ")
         address = input("Address: ")
         city = input("City: ")
         state = input("State: ")
         zip_code = input("Zip Code: ")
         phone = input("Phone Number: ")
         email = input("Email: ")

         contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
         self.address_books[key].add_contact(contact)           
        else:
            log.error(f"{key} address book doesn't exist")
    
        
    def add_new_address_book(self):
        
        name = input("Enter the name of the new Address Book: ")
        if name not in self.address_books:
            self.address_books[name] = AddressBook()
            log.info(f"Address Book '{name}' created successfully.")
        else:
            log.info(f"Address Book '{name}' already exists.")
    
    def edit_contact_console(self):
        key = input("enter the Adress book key")
        
        if key in self.address_books:
            
         print("Enter the Following Details: ")

         f_name = input("Enter first name: ")
         l_name = input("Enter last name: ")

         self.address_books[key].edit_contact(f_name,l_name)
        else:
            log.error(f"{key} address book doesn't exist")
        
    def delete_contact_console(self):
     """
     Description:
        Deletes a contact from the address book based on the first and last name.
    Parameters:
         self
    Return:
        None
     """
     key = input("enter the Adress book key: ")
     
     if key in self.address_books:
         
      print("Enter the Following Details: ")

      f_name = input("Enter first name: ")
      l_name = input("Enter last name: ")

      self.address_books[key].delete_contact(f_name,l_name)
      
     else : 
         log.error(f"{key} address book doesn't exist")
    
    def search_by_city_or_state(self, location):
        
     results = [] 
     for book_name, book in self.address_books.items():
        for contact in book.contacts.values():
            if ( contact.city == location) or (contact.state == location):
                results.append(f"{contact} in Address Book: {book_name}")
     return results
         
                          
    def choice(self):
        '''
        Description:
             function for making choice 
        parameters:
             self as a parameter
        Return:
             none
        '''
        
        while True:
           
            print("1. Add New Contact")
            print("2. edit existing contact")
            print("3. delete contact")
            print("4. new Address book from console")
            print("5. search by city or state")
            print("7. exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                count =int(input("enter the no.of contacts want to enter: "))
                
                while count:
                 self.add_contact_console()
                 count = count-1
                
            elif choice =="2":
                self.edit_contact_console()
            elif choice =="3":
                self.delete_contact_console()
            elif choice =="4":
                self.add_new_address_book()
                
            elif choice =="5":
                self.search_by_city_or_state()
            
            elif choice =="7":
                exit
            else:
                print("Invalid choice. Please try again.")
                
def main():
    address_main = AddressBookMain() 
    address_main.welcome_message()
    address_main.choice()
    
if __name__=="__main__":
    main()
    
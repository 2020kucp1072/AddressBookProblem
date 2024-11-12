'''
    @Author: VEMULA DILEEP
    @Date: 07-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 07-11-2024
    @Title : Address Book 

'''


import log
from collections import defaultdict
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
        self.city_dict = defaultdict(list)
        self.state_dict = defaultdict(list)
        
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
       self.city_dict[contact.city].append(contact)
       self.state_dict[contact.state].append(contact)
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
        
    def view_by_city_or_state(self, location):
        '''
        Description:
            function to view by city or state
        parameters:
            self and location
        Return:
            no 
        '''
        if location in self.city_dict:
            log.info(f"Contacts in city {location}:")
            for contact in self.city_dict[location]:
                log.info(contact)
        elif location in self.state_dict:
            log.info(f"Contacts in state {location}:")
            for contact in self.state_dict[location]:
                log.info(contact)
        else:
            log.info("No contacts found for the given location.")
    
    def count_by_city_or_state(self, location):
        '''
        Description:
            function to count persons in a city or a state in an address book
        parameters:
            self and location
        Return:
            no 
        '''
        city_count = len(self.city_dict.get(location, []))
        state_count = len(self.state_dict.get(location, []))
        if city_count > 0:
            log.info(f"{city_count} contact(s) found in city {location}.")
        if state_count > 0:
            log.info(f"{state_count} contact(s) found in state {location}.")
    
    def display_sorted_contacts_alpha(self):
        
        '''
        Description:
            function to display sorted contacts alphabetical order
        parameters:
            self 
        Return:
            no 
        '''
        
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: (c.first_name, c.last_name))
        log.info("Contacts sorted alphabetically:")
        for contact in sorted_contacts:
            log.info(contact)

    def display_sorted_by_city(self):
        '''
        Description:
            function to display sorted contacts by city 
        parameters:
            self 
        Return:
            no 
        '''
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.city)
        log.info("Contacts sorted by city:")
        for contact in sorted_contacts:
            log.info(contact)

    def display_sorted_by_state(self):
        '''
        Description:
            function to display sorted contacts by state 
        parameters:
            self 
        Return:
            no 
        '''
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.state)
        log.info("Contacts sorted by state:")
        for contact in sorted_contacts:
            log.info(contact)

    def display_sorted_by_zip(self):
        '''
        Description:
            function to display sorted contacted by zipcode
        parameters:
            self 
        Return:
            no 
        '''
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.zip_code)
        log.info("Contacts sorted by zip:")
        for contact in sorted_contacts:
            log.info(contact)
    
    def save_to_text_file(self, filename):
        '''
        
        Description:
            Saves the address book to a text file with each contact on a new line.
            
        parameters:
            filename
            
        Return :
            no
        '''
        with open(filename, 'w') as file:
            for contact_key, contact in self.contacts.items():
                file.write(f"{contact_key}: {contact}\n")
        log.info(f"Address Book saved to text file '{filename}'.")

    
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
     
    def view_state_or_city_console(self):
     """
    Description:
         view_state_or_city from console
    Parameters:
         self
    Return:
        None
     """
     key = input("enter the Adress book key: ")
     
     if key in self.address_books:
         
         location =input("enter city or state: ")
         self.address_books[key].view_by_city_or_state(location)
        
    def count_by_city_state_console(self):
        '''
        Description:
            function to count no.of contacts in a city or a state in an address book
        parameters:
            self and location
        Return:
            no 
        '''  
        key = input("enter the Adress book key: ")
     
        if key in self.address_books: 
            location = input("enter the city or state: ")
            self.address_books[key].count_by_city_or_state(location)
    
    
    def sort_contacts_from_console(self):
        '''
        Description:
            function to display sorted contacts alphabetical order
        parameters:
            self 
        Return:
            no 
        '''
        key = input("enter the Adress book key: ")
     
        if key in self.address_books: 
            
            self.address_books[key].display_sorted_contacts_alpha()
        
    
    def display_sorted_by_city_console(self):
        '''
        Description:
            function to display sorted contacts by city 
        parameters:
            self 
        Return:
            no 
        '''
        key = input("enter the Adress book key: ")
     
        if key in self.address_books: 
            
            self.address_books[key].display_sorted_by_city()
        else:
            log.error(f"{key} address book not found")

    def display_sorted_by_state_console(self):
        '''
        Description:
            function to display sorted contacts by state 
        parameters:
            self 
        Return:
            no 
        '''
        key = input("enter the Adress book key: ")
     
        if key in self.address_books: 
            
            self.address_books[key].display_sorted_by_state()
        else:
            log.error(f"{key} address book not found")

    def display_sorted_by_zip_console(self):
        '''
        Description:
            function to display sorted contacted by zipcode
        parameters:
            self 
        Return:
            no 
        '''
        key = input("enter the Adress book key: ")
     
        if key in self.address_books: 
            
            self.address_books[key].display_sorted_by_zip()
        else:
            log.error(f"{key} address book not found")
         
    
    def save_to_text_file_console(self):
        '''
        Description:
            Saves the address book to a text file with each contact on a new line.
            
        parameters:
            self
            
        Return :
            no
        '''
        key = input("enter the Adress book key: ")
     
        if key in self.address_books: 
            
            self.address_books[key].save_to_text_file("AddressBookData.txt")
        else:
            log.error(f"{key} address book not found")
            
        
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
            print("4. new Address book from console:")
            print("5. search by city or state: ")
            print("6. view by city or state: ")
            print("8. count_by_city_state")
            print("9. sort contacts alphabetically")
            print("10. sort contacts by city")
            print("11. sort contacts by state")
            print("12. sort contacts by zipcode")
            print("13. to write address book to file")
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
            elif choice =="6":
                self.view_state_or_city_console()
            elif choice =="8":
                self.count_by_city_state_console()
            elif choice =="9":
                self.sort_contacts_from_console()
            elif choice =="10":
                self.display_sorted_by_city_console()
            elif choice =="11":
                self.display_sorted_by_state_console()
            elif choice =="12":
                self.display_sorted_by_zip_console()
            elif choice =="13":
                self.save_to_text_file_console()
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
    
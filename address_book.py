'''
    @Author: VEMULA DILEEP
    @Date: 07-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 07-11-2024
    @Title : Address Book 

'''


import log

log = log.logger_init('AddressBookProblem')

    
class AddressBookMain:
    
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
    
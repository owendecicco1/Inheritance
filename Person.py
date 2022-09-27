class Person:
    def __init__(self,name,address,telephone_number):
        self.__name = name 
        self.__address = address
        self.__telephone_number = telephone_number
    
    def get_name(self):
        return self.__name 

    def get_address(self):
        return self.__address
    
    def get_telephone_number(self):
        return self.__telephone_number

    def print_person(self):
        print


    

class Customer(Person):
    def __init__(self,customer_number):
       







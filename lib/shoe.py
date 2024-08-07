#!/usr/bin/env python3
import ipdb

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Initialize the private attribute
        self.size = size   # Use the property setter to validate the size
        self.condition = None

# class Shoe:
#     def __init__(self, brand, size):
#         self.brand = brand
#         self.size = size
#         self._size = None   
#         self.condition = None
        
        #private attribute to store actual size

# FAILED Shoe in shoe.py has the brand and size passed to __init__, and values can be set to new instance. - assert None == 9

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"


    



        
# FAILED Shoe in shoe.py prints "size must be an integer" if size is not an integer. - AssertionError: assert '' == 'size must be an integer\n'

# FAILED Shoe in shoe.py says that the shoe has been repaired. - AttributeError: 'Shoe' object has no attribute 'cobble'

# FAILED Shoe in shoe.py creates an attribute on the instance called 'condition' and set equal to 'New' after repair. - AttributeError: 'Shoe' object has no attribute 'cobble'
# ipdb.set_trace()
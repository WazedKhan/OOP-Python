class Person:
    
    # class attributes
    species = "Homo Sapiens"
    
    # We use __init__ method to assign values to objects propertis, or other operation that are necessary to do when the object are being called
    def __init__(self, name, age): # All classes have a method called __init__ which is always called when class is being initiated
        """Every time a Person class's object is created __init__ sets the initial state of the object 
        by assigning the values of the obejct's properties, Which means __init__ create a instance of the class"""
        self.name = name
        self.age = age
    

p1 = Person('John', 32) #__init__ creates an initance of the Person class and assign it in p1 obejct
p2 = Person("Doe", 36) #__init__ creates another new instance of Person for p2 object

# Attributes created in __init__() are called Instance Attributes 

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
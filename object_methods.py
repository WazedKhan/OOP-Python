class Person:
    #class attribute
    species = "Canis familiaris"
    
    # dunder method
    def __str__(self):
        return f'Its a Person class its current instacne is "{self.name}"'
    
    #Instance Attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # method of Person class
    def introduction(this): # self(name can be whatever we like but it have to be first parameter) parameter is a reference of the class current instance and also use for accessing class variables
        print(f'Hello my name is { this.name } and Im {this.age} years old. Its nice to meet you!')
        

p1 = Person('John', 32)

print(p1)

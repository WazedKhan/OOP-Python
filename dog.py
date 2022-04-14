class Dog:
    """A simple attemp to model a dog"""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title()+' is now sitting.')
        
    def roll_over(self):
        """Simulate rolling over in responce to a command"""
        print(self.name.title()+' is now rolling over.')
        

my_dog = Dog('Snowy', 3)
my_dog.sit()
my_dog.roll_over()
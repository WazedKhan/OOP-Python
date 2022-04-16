class Dog:
    species = 'Canis Familiaris'


    def __str__(self):
        return "Its a Dog Class"
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def speak(self, sound = "Woof"):
        print(f"{self.name} says {sound}")

class WireFoxTerrier(Dog):
    pass


class JackRussellTerrier(Dog):
    def speak(self, sound = 'Arf'):
        print( f"{self.name} says {sound}" )
        
snowy = WireFoxTerrier('Snowy', 3, 'Wire Fox Terrier')
snowy.speak()
jack = JackRussellTerrier('Jack', 3, 'Wire Fox Terrier')

jack.speak("Grr")


print(f'Species: {snowy.species}')
print(type(snowy))
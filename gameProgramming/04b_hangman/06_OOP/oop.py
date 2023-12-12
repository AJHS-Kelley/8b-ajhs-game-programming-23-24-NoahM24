# Object-Oriented Progamming, Truitte Moreland, v0.0

class Person: # Use PascalCase for ClassNames 
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    # To string Function -- How the object appears as a string.
    def __str__(self):
            return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds.\n"
    
    def classFunction(self):
         print("This is an example class function.\n")
         print("It only works when called on an object of that class.")


person1 = Person("Maqui Moreland", 13, 255.5)
person2 = Person("Roana Zoro", 52, 167.5)
print(person1)
print(person2)

if person1.weight > person2.weight:
    print(f"{person1.name} weighs more than {person2.name}.")
elif person1.weight == person2.weight:
    print("Each person weighs the same.\n")
else:
    print(f"{person2.name} weighs more than {person1.name}.")

person1.classFunction()
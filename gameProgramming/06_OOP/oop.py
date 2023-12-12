# Object-Oriented Programming, Noah Mulder, v1.1

class Person: # Yse PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    # To String Function -- How the object appears as a string.
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds.\n"
    
    def classfunction(self):
        print("This is an example class function.\n")
        print("It only works when called on an object of that class.")



person1 = Person("Terry Bogard", 32, 156)
person2 = Person("Mario", 59, 112)
# print(person1)
# print(person2)

# if person1.weight > person2.weight:
#    print(f"{person1.name} weighs more than {person2.name}.")
# elif person1.weight == person2.weight:
#    print("Each person weighs the same.\n")
# else:
#    print(f"{person2.name} weighs more than {person1.name}.")

# if person1.age > person2.age:
#    print(f"{person1.name} is older than {person2.name}.")
# elif person1.age == person2.age:
#    print(f"{person1.name} is the same age as {person2.name}")
# else:
#    print(f"{person2.name} is older than {person1.name}")

# person1.classfunction()

# Changing Properties After Creation
print(person1.name)
person1.name = "William Butcher"
print(person1.name)

print(person1.age)
person1.age = 83
print(person1.age)

# Deleting Properties -- DANGER WILL ROBINSON, DANGER
# THIS IS DOES NOT 'RESET' A PROPERTY, IT DELETES IT COMPLETELY.
print(person1.name)
del person1.name
#print(person1.name)
print(person1.age)
del person1.age
#print(person1.age)

# Deleting Objects -- Delete them if you're finished with them.
del person1

# Adding Properties to Objects -- USE CAREFULLY
person2.weakness = "Kryptonite"
print(person2)
print(person2.weakness)
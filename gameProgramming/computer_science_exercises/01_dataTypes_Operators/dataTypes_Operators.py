# Data Types and Operators, Noah Mulder, v0.6

# Variable Rules
# CANNOT START WITH A NUMBER!!!!!!!!!!!!!!!!!!
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORED
# snake_case variable use _ to seperate words, all lower case
# camelCase variables do not use spaces, 1st word lower, all other upper

# String Literal Examples
playerName = "Rando Rambo Lanbdo"
emptyString = ""
spaceString = " "
sped = "1092091209102910920192019201920910290192019201920"

# Integer Data Types
health = 100
extraLives = 5
temperature = -17
sped = 192019201029109201920192019209102910920192019201920

# Floating Point Data Types
pi = 3.1415678
lapTime = 3.5
velcity = -2.0
sped = 19201029019201920192019201920912091029109201920.1920

# Boolean Data Types
isFiretype = False
weaponEquipped = True
pvpEnabled = False
running = True

#Arithmatic Operators
#PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(30 + 100) # Addition
print(8 - 2) # Subtraction
print(2 * 50) # Multiplication
print(5 / 7) # Division
print(5 ** 10) #Exponent
print(50 % 20) # Modulus - Divides the two numbers and gives you the remainder

# Comparison Operators
# Evaluate the expresson then return True or False
print(6 > 3) # Greater Than
print(6 >= 9) # Greater Than or Equal to
print(6 < 3) # Less Than
print(6 >= 9) #Less Than or Equal to
print(6 == 3) #Equal to
print(6 != 9) # Not Equal to

# Assaignment Operators
myVariable = "myValue" # Give variable on left the value on the right, throw out any current value
myOtherVariable = (100 + 10)
myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# Addition Assignment -- Add the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logical Operators
print(5 > 3 and 3 < 4) # and requires ALL expressions to be True
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favcolor == "Blue" and temp == -5)
# When writing and expression, put the value most likely to be False first

# Logical OR -- Requires ONE expression to be True
print(5 > 2 or 2 < -2)
print(3 != 3 or 5 == 5)

# AND OR Combined
print(3 > 2 and 4 < 3 or 5 != 7)
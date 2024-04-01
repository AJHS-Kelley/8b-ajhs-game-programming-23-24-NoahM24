# input the integers
# .split() the 3 intergers into seperate variables
# cast the 3 variables into integers
# assign correct values from least to greatest
# A < B < C

integers = input()
a, b, c = integers.split()
a = int(a) 
b = int(b)
c = int(c)

print(f"a: {a} b: {b} c: {c}")
if a >= b:
    a, b = b, a
if b >= c:
    b, c = c, b
if b <= a:
    b, a = a, b
print(f"a: {a} b: {b} c: {c}")

# input the string variable
# determine order of A, B, C
# create correct string
# output string

order = input()
my_string = ""

for i in range(len(order)):
    if order[i] == "A":
        my_string += str(a) + " "
    elif order[i] == "B":
        my_string += str(b) + " "
    else:
        my_string += str(c) + " "
print(my_string)
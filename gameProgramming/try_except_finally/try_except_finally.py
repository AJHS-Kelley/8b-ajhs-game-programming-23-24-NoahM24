# This is a method for testing code and preventing crashes.
# try -- except -- else -- finally

try: # The code in this block is ALWAYS executed
    my_variable = 1
    print(my_variable)
    my_string = "Five"
    print(float(my_string))
except ValueError: # This code will run if there is an error (exception) raised.
    print("There is an incorrect variable in your code. Fix it dummy.")
#except:
    #print("Something else has gone wrong.")
else: # This code runs when there are NO ERRORS
    print("Good job. Your code worked correctly for once. =)\n")
finally: # THIS CODE ALWAYS RUNS, IT'S LIKE THE TERMINATOR
    print("This is not power of your creation, b###h")
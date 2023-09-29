# Collections Examples, Noah Mulder, v0.2c

# LIST -- ORDERED, CHANGEABLE, ALLOWS US TO DUPLICATE VALUES
breakfast_foods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk"]
# Each item on the list is known as an ELEMENT
# The position in the list for each is the INDEX
# The element "Bacon" is at index 0
# Python Only: index -1 it is the last item on the list
test_scores = [95, 100, 25, 15, 27, 35]
class_gpa = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25]

# Printing Contents of an List
#print(breakfast_foods)
#print(test_scores)
#print(class_gpa)

# Access Specific List Elements -- REMEMBER FIRST ELEMENT IS INDEX 0
#print(breakfast_foods[0])
#print(test_scores[0])
#print(class_gpa[0])

# Access Last Element in Lists
#print(breakfast_foods[-1])
#print(test_scores[-1])
#print(class_gpa[-1])

# Pause -- WYOC -- Accessing the 3rd Element in Each List
#print(breakfast_foods[3])
#print(test_scores[3])
#print(class_gpa[3])
#print(breakfast_foods[2])
#print(test_scores[2])
#print(class_gpa[2])

# Changing Items in a List
#breakfast_foods[0] = "Sausage"
#test_scores[0] = "97"
#class_gpa[0] = 3.57
#print(breakfast_foods[0])
#print(test_scores[0])
#print(class_gpa[0])
#print(breakfast_foods)
#print(test_scores)
#print(class_gpa)

# Pause -- WYOC -- Change 5th Element
#breakfast_foods[5] = "paper"
#test_scores[5] = 90
#class_gpa[5] = 4.44
#breakfast_foods[4] = "Bagel"
#test_scores[4] = 45
#class_gpa[4] = 2.46
#print(breakfast_foods)
#print(test_scores)
#print(class_gpa)

# Adding and Inserting Items to a List
# .append() adds an item to the END of a list.
#breakfast_foods.append("hash browns")
#print(breakfast_foods)
#test_scores.append(99)
#print(test_scores)
#class_gpa.append(1.99)
#print(class_gpa)

# .insert() allows you to place an item at a specific index in the list
#breakfast_foods.insert(3, "Parfait")
#print(breakfast_foods)
#test_scores.insert(3, 55)
#print(test_scores)
#class_gpa.insert(3, 0.0)
#print(class_gpa)

#PAUSE -- WYOC -- .append() another item in each list. .insert an item at index 5 in each list
#breakfast_foods.append("sabage")
#print(breakfast_foods)
#test_scores.append(1)
#print(test_scores)
#class_gpa.append(1.12)
#print(class_gpa)

#breakfast_foods.append("honey bun")
#print(breakfast_foods)
#test_scores.append(100)
#print(test_scores)
#class_gpa.append(4.0)
#print(class_gpa)

# Deleting Items from a List
# Use .remove() to remove a specific item from the list
#breakfast_foods.remove("Waffles")
#print(breakfast_foods)
#test_scores.remove(100)
#print(test_scores)
#class_gpa.remove(2.25)
#print(class_gpa)

# To delete using the index value we use .pop()
#breakfast_foods.pop(4)
#print(breakfast_foods)
#test_scores.pop(4)
#print(test_scores)
#class_gpa.pop(4)
#print(class_gpa)

# PAUSE - WYOC -- .pop() te 2nd element from each list. .remove() any item from the list
#breakfast_foods.remove("Pancakes")
#breakfast_foods.pop(1)
#print(breakfast_foods)
#test_scores.remove(95)
#test_scores.pop(1)
#print(test_scores)
#class_gpa.remove(3.14)
#class_gpa.pop(1)
#print(class_gpa)

#breakfast_foods.remove("Bacon")
#print(breakfast_foods)
#test_scores.remove(15)
#print(test_scores)
#class_gpa.remove(0.99)
#print(class_gpa)


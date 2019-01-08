# source code from medium article python zero to hero
# The basics
## 1. Variables
one = 1
two = 2
true_boolean = True
false_boolean = False

# string
my_name = "Harshvardhan Scindia"


# float
book_price = 15.80

# control flow : conditional statements

if True:
    print("Hello python if")

if 2 > 1:
    print("2 is greater than 1")

elif 1 > 2:
    print("1 is greater than 2")

else:
    print("1 is equal to 2")

# Looping / iterator
num = 1 
while num <= 10:
    print(num)
    num += 1

loop_condition = True
while loop_condition:
    print("Loop condition keeps %s" % (loop_condition))
    loop_conditon = False

for i in range(1, 11):
    print(i)

# List: Collection | Array| Data Structure
my_integers = [1,2,3,4,56,7,5,4,23]
my_integers = [1,2,3,4,5,5343,4,2]
print(my_integers[0])
print(my_integers[3])
# list of strings
Relative_name = ["fdsfs","fsfsdfds","fsdfdsfd","dfsfsd", "fsdfsdfdsf"]

# Dictionary Key-Value Data Structure
dictionary_example = { "Key1": "Value1", "Key2": "Value2", "Key3":"Value3"}


# Dictionary Accessing key value pairs in python
dictionary_hks = {"name":"harshvardhan", "nickname":"harsh", "nationality":"Indian"}
print("My name is %s" % (dictionary_hks["name"])) # prints my name
print("but you can call me %s" % (dictionary_hks["nickname"])) # prints my name
print("and by the way I'am %s" % (dictionary_hks["nationality"])) # prints my nationality

# iteration: Looping through data structures
bookshelf = ["The effective engineer", "The 4 hours work week", "zero to one", "lean startup",
        "hooked" ]
for book in bookshelf:
    print(book)

dictionary = {"some_key": "some_value"}

for key in dictionary:
    print("%s --> %s" % (key, dictionary[key]))

# some key --- some value

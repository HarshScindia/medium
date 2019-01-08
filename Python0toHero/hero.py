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


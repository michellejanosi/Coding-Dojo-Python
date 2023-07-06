num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True  # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dict
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration; initialize list of strings
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, list access value
pizza_toppings.append('Mushrooms') # list add value
print(person['name']) # log statement, dict access value
person['name'] = 'George' # dict change value
person['eye_color'] = 'blue' # dict add value
print(fruit[2]) # log statement list access value

if num1 > 45: # conditional if
    print("It's greater") # log statement, string
else: # conditional else
    print("It's lower") # log statement, string

if len(string) < 5: # conditional if else if
    print("It's a short word!") # log statement, string
elif len(string) > 15: # length check
    print("It's a long word!") # log statement
else:
    print("Just right!") # log statement, string

for x in range(5): # for loop
    print(x) # log statement numbers
for x in range(2,5): # for loop
    print(x) # log statement
for x in range(2,10,3): # for loop
    print(x) #log statement
x = 0 # variable declaration and initialize
while(x < 5): #while loop
    print(x) # log statement
    x += 1 # increment

pizza_toppings.pop() #list, delete value
pizza_toppings.pop(1) #list, delete value

print(person) # log statement, dict
person.pop('eye_color') #dict, delete value
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional if
        continue # continue
    print('After 1st if statement') # log statement, string
    if topping == 'Olives': # conditional if
        break # break

def print_hello_ten_times(): # function
    for num in range(10): # for loop
        print('Hello') # log statement, string

print_hello_ten_times() # function call

def print_hello_x_times(x): # function, parameter
    for num in range(x): # for loop
        print('Hello') # log statement, string

print_hello_x_times(4) # function call, argument

def print_hello_x_or_ten_times(x = 10): # function, parameter
    for num in range(x): # for loop
        print('Hello') #log statement, string

print_hello_x_or_ten_times() # function call
print_hello_x_or_ten_times(4) # function call, argument


"""
Bonus section
"""

# print(num3) — NameError: name <variable name> is not defined
# num3 = 72 — ?? No error here
# fruit[0] = 'cranberry' — TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) KeyError: 'favorite_team'
# print(pizza_toppings[7]) IndexError: list index out of range
#   print(boolean)  IndentationError: unexpected indent
# fruit.append('raspberry') AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) AttributeError: 'tuple' object has no attribute 'pop'

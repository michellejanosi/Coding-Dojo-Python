#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# this will print 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# this will print an error because number_of_days_in_a_week_silicon_or_triangle_sides() is not defined at this point. Functions need to be defined before you call it unlike JavaScript where function definitions are hoisted to the top

# #3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# 5 will be printed. We exit the function when it returns the output. The second return statement is ignored.

# #4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# 5 is printed. Same here as in the previous function, we exit the function when we return the output.

# #5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# 5 and None are printed. There is no return in the function so the return is None which is the default value

# #6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# We get an error here because the function returns None as there is no return statement in the function. You cannot add None to None

# #7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# 25 is printed. Since the function is convertiing the number type to string, we concatenate the result

# #8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# 100 and 10 because we first print the value of b and then return the result of the conditional. The conditional evaluates to false so we return the output after the else statement. Remaining returns are ignored.

# #9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#7; 14; 21 The final return is ignored

# #10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# 8. The second return is ignored

# #11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# 500; 500; 300; 500

# #12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# 500; 500; 300; 500

# #13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# 500; 500; 300; 300 The function, as in the previous, prints and returns the value of b inside the function

# #14
def foo():
    print(1)
    bar()
    print(2)

def bar():
    print(3)

foo()
# 1; 3; 2 There is no explicit return but the values are all still printed

# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10

def bar():
    print(3)
    return 5

y = foo()
print(y)
#1; 3; 5; 10 We print 1 from foo plus the print and return from bar and then we return 10 from foo

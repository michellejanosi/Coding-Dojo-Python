# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# use a loop that starts with the input number. for each iteration, push the next number to a list. return the list
def countdown(num):
    countdown_list = []

    for i in range(num, -1, -1):
        countdown_list.append(i)

    return countdown_list

print(countdown(5))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

# Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(nums):
    print(nums[0])
    return nums[1]

print(print_and_return([1,2]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# create a variable sum to hold the result of first value and length of list
# lst[0] + (len[lst])
# return sum
def first_plus_length(lst):
    sum = lst[0] + len(lst)
    return sum

print(first_plus_length([1,2,3,4,5]))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# if the input list is less than 2 items, return false
# declare a new list variable to hold the result
# use a for loop to iterate the input list
# use a conditional statement to evaluate each item with it's second item
# if the item is greater than it's second item, append to new list
# print the length of the new list and then return it

def values_greater_than_second(values):
    if len(values) < 2:
        return False

    greater_values = []

    for i in values:
        if i > values[1]:
            greater_values.append(i)

    print(len(greater_values))
    return greater_values

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

# return a list of the input value and multiply it by size
def length_and_value(size, value):
    return [value] * size

print(length_and_value(4,7))
print(length_and_value(6,2))

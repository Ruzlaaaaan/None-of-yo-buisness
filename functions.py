#Passing parameters and arguments
def greet_user(name):
    #Calling function with argument
    greet_user("HERO")

#Function argument types:
#positional arguments
def add(a,b):
    print("Sum is:", a+b)
    add(5,10)
#Keyword arguments
def introduce(name,age):
    print(f'My name is {name} and I am {age} years old')
    introduce(age = 29, name="hero")

#Default arguments
def greet(name='guest'):
    print("Hello,", name)
    greet()
    greet("Ruzlan")

#Higher order functions
def square(x):
    return x*x
numbers=[1,2,3,4,5]
squared = list(map(square, numbers))
print(squared)

#filter()
def is_even(x):
    return x%2 == 0
numbers = [1,2,3,4,5,6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

#Reduce()
from functools import reduce
def add(x, y):
    return x+y
numbers = [1,2,3,4,5]
sum_numbers = reduce(add, numbers)
print(sum_numbers)
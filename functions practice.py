def mult_numbers(a, b):
    print(a*b)
mult_numbers(a=5, b=5)

#Even or Odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        
# Example 
check_even_odd(int(input("Enter a Number")))

#Factorial
def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial of {n} is {result}")
factorial(n=int(input("Enter A Number")))

#Largest from a,b,c

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    
    else:
        return c

# Example
print(largest_of_three(a=int(input("Enter 'a' value: ")), b=int(input("Enter 'b' value: ")), c=int(input("Enter 'c' value: "))))

#Reverse String
str = input("Enter a string")
def reverse_string(s):
    return s[::-1]
print(reverse_string(str))

#aeiou

word = input("Enter your name")
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in vowels:
        count+=1
    return count
print(count_vowels(word)) 

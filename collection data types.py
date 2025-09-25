#adding an element
fruits = ['apple', 'banana', 'mango']
print(fruits)
fruits.append('orange')
#remove an element

fruits = ['apple', 'banana', 'mango', 'orange']
fruits.remove('banana')
print(fruits)

#changing an element

fruits[1] = 'grapes'
print(fruits)

#access elements from a list
fruits = ['apple', 'banana', 'mango', 'grapes' ,'orange']
print(fruits[-1]) # [0] = first element and [-1] = last element

#sort the list
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
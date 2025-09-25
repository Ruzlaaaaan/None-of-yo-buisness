# Easy Type Conversions in Python
# Type conversion means changing one data type to another.
# Python has built-in functions like int(), float(), str(), bool(), list(), tuple(), set(), dict()
# Let's see examples with outputs.

print("=== Basic Type Conversions ===")

# 1. String to Integer
# If a string has numbers, you can turn it into an integer.
str_num = "42"
int_num = int(str_num)
print(f"String '{str_num}' to int: {int_num}, type: {type(int_num)}")

# 2. Integer to String
# Turn a number into text.
num = 123
str_num = str(num)
print(f"Int {num} to string: '{str_num}', type: {type(str_num)}")

# 3. Float to Integer
# Float (decimal) to whole number. It removes the decimal part.
float_num = 3.99
int_num = int(float_num)
print(f"Float {float_num} to int: {int_num}, type: {type(int_num)}")

# 4. Integer to Float
# Whole number to decimal.
num = 5
float_num = float(num)
print(f"Int {num} to float: {float_num}, type: {type(float_num)}")

# 5. String to Float
str_float = "2.5"
float_num = float(str_float)
print(f"String '{str_float}' to float: {float_num}, type: {type(float_num)}")

# 6. Boolean to Integer
# True becomes 1, False becomes 0.
bool_true = True
bool_false = False
int_true = int(bool_true)
int_false = int(bool_false)
print(f"Bool {bool_true} to int: {int_true}")
print(f"Bool {bool_false} to int: {int_false}")

# 7. Integer to Boolean
# 0 becomes False, any other number becomes True.
zero = 0
one = 1
bool_zero = bool(zero)
bool_one = bool(one)
print(f"Int {zero} to bool: {bool_zero}")
print(f"Int {one} to bool: {bool_one}")

print("\n=== Collection Type Conversions ===")

# 8. List to Tuple
# List is changeable, tuple is not.
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"List {my_list} to tuple: {my_tuple}, type: {type(my_tuple)}")

# 9. Tuple to List
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(f"Tuple {my_tuple} to list: {my_list}, type: {type(my_list)}")

# 10. List to Set
# Set removes duplicates and is unordered.
my_list = [1, 2, 2, 3, 4, 5]
my_set = set(my_list)
print(f"List {my_list} to set: {my_set}, type: {type(my_set)}")

# 11. Set to List
my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
print(f"Set {my_set} to list: {my_list}, type: {type(my_list)}")

# 12. Dictionary to List of Keys
# Get all the keys from a dict as a list.
student = {'Name': 'Ruzlan', 'age': 17, 'grade': 'A'}
keys_list = list(student.keys())
print(f"Dict {student} keys to list: {keys_list}")

# 13. Dictionary to List of Values
values_list = list(student.values())
print(f"Dict {student} values to list: {values_list}")

# 14. Dictionary to List of Items (key-value pairs)
items_list = list(student.items())
print(f"Dict {student} items to list: {items_list}")

print("\nThat's it! Type conversions help you change data types as needed.")

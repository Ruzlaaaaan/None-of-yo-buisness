import array
numbers = array.array('i', [1,2,3,4,5,6,7,8,9])
print(numbers[0])
print(numbers[-1])

#2
print(numbers[1:4])

#3
print(numbers[:-1])

#4
print(numbers[::2])

#5 Given,
import array
nums = array.array('i', [5,10,15,20,25,30])
print(nums[0:4])
nums_slice = nums[0:4]
total = 0
for num in nums_slice:
    total += num
print("Sum of first four elements:", total)


#6
print(numbers[::-1])

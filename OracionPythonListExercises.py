#Oracion Python List Exercises

#1. Creating a list
fruits = ["Mango", "Apple", "Pineapple", "Grapes", "Strawberry" ]
print(fruits) 

#2. Accessing Elements
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print('First Color:', colors[0]) # will print 'red'
print('Third Color:', colors[2]) # will print 'green'
print('Last Color:', colors[4]) # will print 'purple'

#3. Modifying a List
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25 # this line of code replaces 20 with 25
numbers.append(60) # this will add the number 60 to the list
print(numbers)

#4. List Slicing
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3] # will create a new list with the first 3 names
print(subset) 

#5. Looping through a List
numbers_1 = list(range(1,11))
for number in numbers_1:
    print(number ** 2)

#6. List methods: Append and Extend
shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs') #.append adds all these items into the list
shopping_cart.extend(['butter', 'cheese']) #extends the list and adds butter and cheese to the 'shopping_cart' list
print(shopping_cart)

#7. Finding Minimum and Maximum
number = [45, 22, 88, 56, 92, 33]
print('Maximum Value:', max(number)) # will print out the highest nubmer in the list
print('Minimum Vlaue:', min(number)) # will print out the lowest number in the list

#8. Counting occurences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
counting_of_a = letters.count('a')
print('Count of a:', counting_of_a) 

#9. List comprehension
even_numbers = [x ** 2 for x in range (0,11) if x % 2 == 0]
print(even_numbers)

#10. Removing duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
single_nums = list(set(nums)) # this line of code removes duplicates by converting it into a set then making it a list again
print(single_nums)



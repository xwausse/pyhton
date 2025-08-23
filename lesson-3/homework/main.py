##Create a list containing five different fruits and print the third fruit.
fruits = ['olma', 'nok', 'tarvuz', 'qovun', 'hurmon']
print(fruits[2])

##Create two lists of numbers and concatenate them into a single list.
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1 + list2)

##Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
num = [1, 2, 3, 4, 5, 6]

first = num[0]               # birinchi element
middle = num[len(num)//2]    # o‘rtadagi element
last = num[-1]               # oxirgi element

new_list = [first, middle, last]
print(new_list)

##Create a list of your five favorite movies and convert it into a tuple.
movies = ["Inception", "Avatar", "Titanic", "Gladiator", "Interstellar"]
film = tuple(movies)
print(film)

##Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["London", "Paris", "Rome", "Berlin"]
if "Paris" in cities:
    print('ha bor')
else: ('yoq')

##Create a list of numbers and duplicate it without using loops.
numbers = [1,2,3,4] *2
print(numbers)

##Given a list of numbers, swap the first and last elements.
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

##Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers = [1,2,3,4,5,6,7,8,9,10,11]
nums = numbers[2:6]
print(nums)

##Create a list of colors and count how many times "blue" appears in the list.
colors = ["red", "blue", "green", "blue", "yellow"]
topish = colors.count("blue")
print(topish)

##Given a tuple of animals, find the index of "lion".
animals = ["cat", "dog", "lion", "tiger", "elephant"]
sher = animals.index("lion")
print(sher)

##Create two tuples of numbers and merge them into a single tuple.
numbers = (1,2,3,4)
numbers2 = (5,6,7,8)
print(numbers + numbers2)

##Given a list and a tuple, find and print their lengths.
my_list = [1,2,3,4]
tuple = (5,6,7,8)
print(len(list))
print(len(tuple))

##Create a tuple of five numbers and convert it into a list.
##Create a tuple of five numbers and convert it into a list.
numbers4 = (1,2,3,4,5)
ozgar = list(numbers4)
print(len(ozgar))

##Given a tuple of numbers, find and print the maximum and minimum values.
sonla = [12, 5, 8, 20, 3, 15]
kotta = max(sonla)
kichik = min(sonla)
print(kotta)
print(kichik)

##Create a tuple of words and print it in reverse order.
words = ("apple", "banana", "cherry", "date", "elderberry")
print(words[::-1])

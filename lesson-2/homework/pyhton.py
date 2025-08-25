##Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
from datetime import datetime
name = input('ismingizni kiriting')
birthday_year = int(input('tugulgan yilingiz'))

current_year = datetime.now().year
age = current_year - birthday_year
print('sizning ismingiz:', name)
print('tugulgan yilingiz:', birthday_year)
print('siz', age, 'dasiz')

##Extract car names from the following text:
txt = 'LMaasleitbtui'
car1 = txt[::2]
car2 = txt[1::2]
print(car1)
print(car2)

##Extract car names from the following text:
txt = 'MsaatmiazD'
moshn1 = txt[::2]
moshn2 = txt[:1:-2]
print(moshn1)
print(moshn2)

##Extract the residence area from the following text:
txt = "I'am John. I am from London"
txt.index('L')
txt[txt.index('L'):]

##Write a Python program that takes a user input string and prints it in reverse order.
name = input('ismingizni kiriting')
ozgar = name[::-1]
print('ismingiz:', ozgar)

##Write a Python program that counts the number of vowels in a given string.
matn = input("Matn kiriting: ")
unlilar = "aeiouAEIOU"
soni = 0
for harf in matn:
    if harf in unlilar:
        soni += 1
print("Unli harflar soni:", soni)

##Write a Python program that takes a list of numbers as input and prints the maximum value.
sonlar = input("Sonlarni kiriting (vergul bilan): ")
sonlar_list = [int(x) for x in sonlar.split(",")]
kotta = max(sonlar_list)
print("Eng katta son:", kotta)

##Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word = input("So'z kiriting: ")
word_clean = word.lower()
if word_clean == word_clean[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

##Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Email manzilingizni kiriting: ")
domain = email.split("@")[-1]
print("Domen:", domain)

##Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
length = 12
password = "".join(random.choice(characters) for _ in range(length))
print("Tasodifiy parol:", password)

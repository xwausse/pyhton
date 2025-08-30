a = int(input('enter your year'))
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 ==0:
            print(f'{a} is leap year')
        else:
            print(f'{a} is not leap year')
    else: 
        print(f'{a} is a leap year')
else:
    print(f'{a} is not lear')                


n = int(input('enter your number'))
if n % 2 != 0:
    print('Weird')

n = int(input("Enter a number: "))
if n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")

n = int(input("Enter a number: "))

if n % 2 == 0 and 6 <= n <= 20:
    print("Weird")


n = int(input("Enter a number: "))
if n % 2 == 0 and n > 20:
    print('Weird')


n = int(input("You entered:"))  
if 1 <= n <= 100:
    print('Weird')
else:
    print('not Weird')

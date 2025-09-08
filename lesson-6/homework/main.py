def modify_string(txt):
    vowels = "aeiou"
    result = ""
    count = 0
    
    i = 0
    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3:
           
            if i < len(txt) - 1:
                if txt[i] not in vowels and (i+1 >= len(txt) or txt[i+1] != "_"):
                    result += "_"
            count = 0
        i += 1
    
    return result

print(modify_string("hello"))          
print(modify_string("assalom"))        
print(modify_string("abcabcabcdeabcdefabcdefg"))


n = int(input("Enter n: "))

for i in range(n):
    print(i**2)


i = 1
while i <= 10:
    print(i)
    i += 1


num = int(input("Enter number: "))
for i in range(1, 11):
    print(num * i)

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0 and num < 200:
        print(num)


n = int(input("Enter number: "))
print("Digits:", len(str(n)))

n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

for i in range(-10, 0):
    print(i)

for i in range(5):
    print(i)
else:
    print("Done!")

start, end = 25, 50
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)
n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! = {fact}")

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

print(squared)   




def is_prime(n):
    if n < 2:   
        return False
    
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False
    return True  




def digit_sum(n):
    s = 0
    for raqam in str(n):  
        s += int(raqam)
    return s
print(digit_sum(24))   
print(digit_sum(502))  
print(digit_sum(1234)) 


def power_of_two(n):
    k = 1
    while 2**k <= n:  
        print(2**k, end=" ")
        k += 1
power_of_two(10)

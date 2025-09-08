
d = {1: 20, 2: 5, 3: 15}
asc = dict(sorted(d.items(), key=lambda item: item[1]))
print("Ascending:", asc)
desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc)



d = {0: 10, 1: 20}
d[2] = 30
print(d)  

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged = {}
for d in (dic1, dic2, dic3):
    merged.update(d)

print(merged)  
def squares(n):
    return {x: x*x for x in range(1, n+1)}

print(squares(5)) 

d = {x: x**2 for x in range(1, 16)}
print(d)


s = {"apple", "banana", "cherry"}
for item in s:
    print(item)

s = {1, 2, 3}
s.add(4)              
s.update([5, 6, 7]) 
print(s)

s = {1, 2, 3, 4}
s.remove(2)   
print(s)

s.discard(10) 
print(s)


s = {1, 2, 3, 4}
if 3 in s:
    s.remove(3)
print(s)

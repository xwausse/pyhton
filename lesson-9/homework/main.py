import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())



from datetime import date

class Person:
    def __init__(self, name, country, birth_date):  
        self.name = name
        self.country = country
        self.birth_date = date.fromisoformat(birth_date)

    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )


p = Person("Ali", "Uzbekistan", "2000-05-10")
print(p.name, "age is", p.age())



class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"


calc = Calculator()
print(calc.add(5, 3))
print(calc.divide(10, 0))


import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


sq = Square(4)
print("Square area:", sq.area())
print("Square perimeter:", sq.perimeter())


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)


tree = BST()
root = None
for num in [50, 30, 70, 20, 40, 60, 80]:
    root = tree.insert(root, num)

print("Found:", tree.search(root, 40) is not None)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else "Stack is empty"


s = Stack()
s.push(10)
s.push(20)
print(s.pop()) 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.display()
ll.delete(10)
ll.display()


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total(self):
        return sum(self.items.values())


cart = ShoppingCart()
cart.add_item("Apple", 3)
cart.add_item("Banana", 2)
print("Total:", cart.total())


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else "Stack is empty"

    def display(self):
        print(self.items)


s = Stack()
s.push(1)
s.push(2)
s.display()
s.pop()
s.display()


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else "Queue is empty"


q = Queue()
q.enqueue(5)
q.enqueue(10)
print(q.dequeue())  # 5


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount
        else:
            print("Insufficient funds")

    def balance(self, name):
        return self.accounts.get(name, "Account not found")


bank = Bank()
bank.create_account("Ali", 100)
bank.deposit("Ali", 50)
bank.withdraw("Ali", 30)
print("Balance:", bank.balance("Ali"))

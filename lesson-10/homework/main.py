from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} - {self.description} - Due: {self.due_date} - [{self.status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def list_incomplete(self):
        for task in self.tasks:
            if task.status == "Incomplete":
                print(task)


def main():
    todo = ToDoList()
    while True:
        print("\n--- ToDo List ---")
        print("1. Add Task\n2. Mark Task Complete\n3. List All Tasks\n4. List Incomplete Tasks\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(Task(title, desc, due))
        elif choice == "2":
            title = input("Enter task title to mark complete: ")
            todo.mark_complete(title)
        elif choice == "3":
            todo.list_tasks()
        elif choice == "4":
            todo.list_incomplete()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


            class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nBy: {self.author}\n{self.content}\n"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for post in self.posts:
            print(post)

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post)

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content

    def latest_posts(self, n=5):
        for post in self.posts[-n:]:
            print(post)



def main_blog():
    blog = Blog()
    while True:
        print("\n--- Blog System ---")
        print("1. Add Post\n2. List All Posts\n3. Show Posts by Author\n4. Delete Post\n5. Edit Post\n6. Latest Posts\n7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == "2":
            blog.list_posts()
        elif choice == "3":
            author = input("Author: ")
            blog.posts_by_author(author)
        elif choice == "4":
            title = input("Title to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            title = input("Title to edit: ")
            new_content = input("New Content: ")
            blog.edit_post(title, new_content)
        elif choice == "6":
            blog.latest_posts()
        elif choice == "7":
            break
        else:
            print("Invalid choice")



class Account:
    def __init__(self, acc_no, holder, balance=0):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"Account {self.acc_no}: {self.holder} - Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_no] = account

    def get_account(self, acc_no):
        return self.accounts.get(acc_no, None)

    def transfer(self, from_acc, to_acc, amount):
        acc1 = self.get_account(from_acc)
        acc2 = self.get_account(to_acc)
        if acc1 and acc2 and acc1.balance >= amount:
            acc1.withdraw(amount)
            acc2.deposit(amount)
        else:
            print("Transfer failed")


def main_bank():
    bank = Bank()
    while True:
        print("\n--- Bank System ---")
        print("1. Add Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Show Accounts\n7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            acc_no = input("Account Number: ")
            name = input("Holder Name: ")
            balance = float(input("Initial Balance: "))
            bank.add_account(Account(acc_no, name, balance))
        elif choice == "2":
            acc_no = input("Account Number: ")
            acc = bank.get_account(acc_no)
            print(acc if acc else "Not found")
        elif choice == "3":
            acc_no = input("Account Number: ")
            amount = float(input("Amount: "))
            acc = bank.get_account(acc_no)
            if acc: acc.deposit(amount)
        elif choice == "4":
            acc_no = input("Account Number: ")
            amount = float(input("Amount: "))
            acc = bank.get_account(acc_no)
            if acc: acc.withdraw(amount)
        elif choice == "5":
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amount = float(input("Amount: "))
            bank.transfer(from_acc, to_acc, amount)
        elif choice == "6":
            for acc in bank.accounts.values():
                print(acc)
        elif choice == "7":
            break
        else:
            print("Invalid choice")

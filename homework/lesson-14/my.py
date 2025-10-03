import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")import requests

API_KEY = "YOUR_API_KEY"  # bu yerga o‘z API key’ingizni yozing
city = "Tashkent"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"Shahar: {data['name']}")
    print(f"Harorat: {data['main']['temp']}°C")
    print(f"Namlik: {data['main']['humidity']}%")
    print(f"Ob-havo: {data['weather'][0]['description']}")
else:
    print("Xatolik:", data.get("message", "Ma'lumot topilmadi"))
import json

def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def add_book():
    books = load_books()
    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    year = input("Yili: ")
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print("Kitob qo‘shildi ✅")

def update_book():
    books = load_books()
    title = input("Yangilanadigan kitob nomi: ")
    for book in books:
        if book["title"].lower() == title.lower():
            book["author"] = input("Yangi muallif: ")
            book["year"] = input("Yangi yil: ")
            save_books(books)
            print("Kitob yangilandi ✅")
            return
    print("Kitob topilmadi ❌")

def delete_book():
    books = load_books()
    title = input("O‘chiriladigan kitob nomi: ")
    books = [book for book in books if book["title"].lower() != title.lower()]
    save_books(books)
    print("Kitob o‘chirildi ✅")

# Test menyu
while True:
    print("\n1. Kitob qo‘shish\n2. Kitob yangilash\n3. Kitob o‘chirish\n4. Chiqish")
    choice = input("Tanlang: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        break
    else:
        print("Noto‘g‘ri tanlov!")
import requests
import random

API_KEY = "YOUR_API_KEY"  # bu yerga OMDb API key'ingizni yozing

genre = input("Qaysi janrdan kino xohlaysiz? (masalan: Action, Comedy, Drama): ")

# OMDb’da janr bo‘yicha qidiruv to‘liq emas, shuning uchun mashhur filmlardan tanlaymiz
movies_list = ["Inception", "The Dark Knight", "Titanic", "Avengers", "The Matrix", "Interstellar", "Joker", "Gladiator"]

random_movie = random.choice(movies_list)

url = f"http://www.omdbapi.com/?t={random_movie}&apikey={API_KEY}"
response = requests.get(url)
data = response.json()

if data["Response"] == "True" and genre.lower() in data["Genre"].lower():
    print(f"Tavsiya qilinadigan kino: {data['Title']} ({data['Year']})")
    print("Janr:", data["Genre"])
    print("Reyting:", data["imdbRating"])
    print("Izoh:", data["Plot"])
else:
    print("Siz xohlagan janrga mos kino topilmadi, qaytadan urinib ko‘ring.")


import sqlite3

with sqlite3.connect("zoo.db") as con:
    cur = con.cursor()

    # Jadval yaratish
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    """)

    print("Roster jadvali yaratildi!")

with sqlite3.connect("zoo.db") as con:
    cur = con.cursor()

    cur.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)",
                ("Benjamin Sisko", "Human", 40))
    cur.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)",
                ("Jadzia Dax", "Trill", 30))
    cur.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)",
                ("Kira Nerys", "Bajoran", 29))

    cur.execute("SELECT * FROM Roster")
    rows = cur.fetchall()
    for r in rows:
        print(r)

with sqlite3.connect("zoo.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Roster")
    rows = cur.fetchall()

    # Ustun nomlarini chiqarish
    col_names = [desc[0] for desc in cur.description]
    print(" | ".join(col_names))

    # Ma'lumotlarni chiqarish
    for row in rows:
        print(row)


with sqlite3.connect("zoo.db") as con:
    cur = con.cursor()
    cur.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
    cur.execute("SELECT * FROM Roster")
    rows = cur.fetchall()
    for r in rows:
        print(r)

with sqlite3.connect("zoo.db") as con:
    cur = con.cursor()
    
    # faqat Bajoran bo'lganlarni chiqarish
    cur.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
    rows = cur.fetchall()
    
    # ustun nomlarini chiqarish
    col_names = [desc[0] for desc in cur.description]
    print(" | ".join(col_names))
    
    # ma'lumotlarni chiqarish
    for r in rows:
        print(r)

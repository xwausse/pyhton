import sqlite3

# 1. Yangi database yaratamiz (fayl sifatida saqlanadi)
con = sqlite3.connect("startrek.db")
cur = con.cursor()

# 2. Jadval yaratish
cur.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 3. Ma'lumot qo'shish
cur.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

con.commit()

# 4. Update qilish (Jadzia Dax → Ezri Dax)
cur.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")
con.commit()

# 5. Bajoranlarni chiqarish (Name, Age)
cur.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")

rows = cur.fetchall()
for row in rows:
    print(row)

# Bog'lanishni yopish
con.close()

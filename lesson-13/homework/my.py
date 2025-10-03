from datetime import date

birthdate = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
birthdate = date.fromisoformat(birthdate)
today = date.today()

years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days

if months < 0:
    years -= 1
    months += 12

print(f"Siz {years} yil, {months} oy, {days} kun yashagansiz.")
from datetime import date, timedelta

birthdate = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
birthdate = date.fromisoformat(birthdate)
today = date.today()

next_birthday = date(today.year, birthdate.month, birthdate.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, birthdate.month, birthdate.day)

days_left = (next_birthday - today).days
print(f"Keyingi tug‘ilgan kuningizgacha {days_left} kun qoldi.")
from datetime import datetime, timedelta

current_time = input("Hozirgi vaqtni kiriting (YYYY-MM-DD HH:MM): ")
current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")

hours = int(input("Uchrashuv davomiyligi (soat): "))
minutes = int(input("Uchrashuv davomiyligi (daqiqa): "))

end_time = current_time + timedelta(hours=hours, minutes=minutes)
print("Uchrashuv tugash vaqti:", end_time)
from datetime import datetime
import pytz

dt_str = input("Sanani va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_tz = input("Joriy timezone (masalan: Asia/Tashkent): ")
to_tz = input("O‘zgartirish kerak bo‘lgan timezone: ")

dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
from_zone = pytz.timezone(from_tz)
to_zone = pytz.timezone(to_tz)

dt = from_zone.localize(dt)
converted = dt.astimezone(to_zone)

print("Natija:", converted)

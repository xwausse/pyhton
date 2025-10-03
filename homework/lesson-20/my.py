import sqlite3
import pandas as pd

# DB bilan ulanamiz
conn = sqlite3.connect("chinook.db")

# Invoices va Customersdan kerakli ma'lumotlarni olish
invoices = pd.read_sql("SELECT InvoiceId, CustomerId, Total FROM invoices", conn)
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM customers", conn)

# 1. Har bir customer qancha xarajat qilgan
customer_spending = invoices.groupby("CustomerId")["Total"].sum().reset_index()
customer_spending = customer_spending.merge(customers, on="CustomerId")

# 2. Top 5 customer
top5_customers = customer_spending.sort_values("Total", ascending=False).head(5)

print("Top 5 Customers (ID, Name, Total Spent):\n")
print(top5_customers[["CustomerId", "FirstName", "LastName", "Total"]])
# Kerakli jadvalni olish
invoice_lines = pd.read_sql("SELECT InvoiceLineId, InvoiceId, TrackId FROM invoice_items", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM tracks", conn)

# Invoice_items + tracks merge
sales = invoice_lines.merge(tracks, on="TrackId")

# Har bir Customer va Album bo‘yicha nechta track sotib olganini hisoblash
customer_albums = sales.merge(invoices[["InvoiceId", "CustomerId"]], on="InvoiceId")
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracksInAlbum"}, inplace=True)

# Customer qaysi albomdan nechta track olganini hisoblash
customer_album_tracks = customer_albums.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index()
customer_album_tracks = customer_album_tracks.merge(album_track_counts, on="AlbumId")

# Agar customer albomdagi hamma treklarni sotib olgan bo‘lsa → Full Album
customer_album_tracks["PurchaseType"] = customer_album_tracks.apply(
    lambda row: "Full Album" if row["TrackId"] == row["TotalTracksInAlbum"] else "Individual Tracks", axis=1
)

# Har bir customerning preference’ini aniqlash
customer_pref = customer_album_tracks.groupby("CustomerId")["PurchaseType"].apply(lambda x: "Individual Tracks" if "Individual Tracks" in x.values else "Full Album").reset_index()

# Percentage hisoblash
summary = customer_pref["PurchaseType"].value_counts(normalize=True) * 100

print("\nPercentage of customers (Full Album vs Individual Tracks):\n")
print(summary)

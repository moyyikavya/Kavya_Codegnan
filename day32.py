'''import matplotlib.pyplot as plt
plt.bar([2024,2025,2026],[67,89,50],color="Gray")
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of Cars sold")
plt.show()


import matplotlib.pyplot as plt
plt.bar([2024,2025,2026],[67,89,50],color = "purple")
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of cars sold")
plt.show()

plt.bar([2024,2025,2026],[67,89,50],color = "Gray")
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of cars sold")
plt.show()

import matplotlib.pyplot as plt
plt.pie([40,15,35,20],labels=["Backend(Python)","Frontend(HTML,CSS)","Database(MySQL)","Testing"])
plt.title("ATM Application(Project)")
plt.legend(["Sai","Niral","Abdul","Teja"])
plt.show()


import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[200,400,100,800],color="Yellow",s=100)
plt.title("Swift Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of Sales")
plt.show()

import matplotlib.pyplot as plt
plt.bar(["mini cooper","Toyota yaris","Renault 5","Honda jazz","LADa classic"],[100000,64000,90000,54000,67000],color = "purple")
plt.title("Cars")
plt.xlabel("Prise")
plt.ylabel("Number of cars sold")
plt.show()
'''
#WEB scraping
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

# Step 1: Web Scraping
url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'    # Fix encoding issue
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

names = []
prices = []

for book in books:
    name = book.h3.a["title"]

    # Get raw price text
    price_text = book.find("p", class_="price_color").text

    # Extract numeric value using regex (fix for Â£ issue)
    price = float(re.findall(r'\d+\.\d+', price_text)[0])

    names.append(name)
    prices.append(price)

#step2
df=pd.DateFrame({
    "BookName":names,
    "price":prices
    })   
print("\n Table Data:\n")
print(df.head())

# Save to CSV
df.to_csv("books_data.csv", index=False)
print("\n CSV file 'books_data.csv' created successfully!")

# Step 3: Data Visualization
plt.figure()
plt.bar(names[:10], prices[:10])  # Top 10 books
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices (Top 10)")
plt.tight_layout()
plt.show()
print("\n Table Data:\n")
print(df.head())

# Save to CSV
df.to_csv("books_data.csv", index=False)
print("\n CSV file 'books_data.csv' created successfully!")

# Step 3: Data Visualization
plt.figure()
plt.bar(names[:10], prices[:10])  # Top 10 books
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices (Top 10)")
plt.tight_layout()
plt.show()

















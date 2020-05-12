import pandas as pd
import requests
from bs4 import BeautifulSoup

Hotel_name = []
Hotel_Add = []
Hotel_Highlights = []
Bookings = []

print("This is to scrape the 'weddingz.in' data")

url = 'https://weddingz.in/banquet-halls/pune/all/'

r = requests.get("https://weddingz.in/banquet-halls/pune/all/")
# print(r.content)
soup = BeautifulSoup(r.content, features="lxml")
soup.prettify()
# print(soup.find_all("a"))
for links in soup.find_all("a"):
    #    print(links.text, links.get("href"))
    #    print("<a href='%s'>%s</a>" % (links.get("href"), links.text))

    g_data = soup.find_all("div", {"class": "info-box"})

    col_names = ['Hotel_name', 'Hotel_Add']
    my_df = pd.DataFrame(columns=col_names)

    list_halls = []
    for item in g_data:
        Hotel_name1 = item.contents[1].text.replace(',', '')  # Name of hotel
        Hotel_name.append(Hotel_name1)
        # print(Hotel_name1)

        Hotel_Add1 = item.contents[3].text.replace(',', '')  # Address of hotel
        # print(Hotel_Add1)
        Hotel_Add.append(Hotel_Add1)

        list_hotel = [Hotel_name1, Hotel_Add1]
        list_halls.append(list_hotel)

        # Hotel_Highlights1 = item.contents[7].text  # high lights
        # print(Hotel_Highlights1)
        # Hotel_Highlights.append(Hotel_Highlights1)

        # Bookings1 = item.contents[9].text.replace('  ', '')  # Shortlisted , booking
        # print(Bookings1)
        # Bookings.append(Bookings1)
        # item.contents[12].text
print(list_halls)

df = pd.DataFrame(list_halls, columns=["Hotel_name", "Hotel_Add"])
print(df)
# df = pd.DataFrame(
#    {'Hotel Name': Hotel_name, 'Hotel Address': Hotel_Add})
df.to_csv('Hotels.csv', index=False, encoding='utf-8')

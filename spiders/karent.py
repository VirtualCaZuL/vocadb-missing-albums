from bs4 import BeautifulSoup
import requests
page = 1

# Getting all the "a" html elements of the first page
html_text = requests.get(f"https://karent.jp/album/p/{page}").text
soup = BeautifulSoup(html_text, "lxml")
albums = soup.find_all("a", class_ = "boxlist__clm boxlist__clm--pc6sp3")
links = []

# Getting individual data about albums (name, artist, link, number of tracks)
for album in albums:
    album_name = album.find("p", class_ = "boxlist__p").text
    album_link = album["href"]
    links.append(album_link)
    artist_name = album.find("p", class_ = "boxlist__p--small").text
    print(f"Name : {album_name}")
    print(f"Artist : {artist_name}")
    print(f"Link : {album_link}\n")
    
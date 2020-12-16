#! python3
#lucky.py

import requests, sys, webbrowser, bs4

print("Googling...")
res = requests.get("https://www.google.com/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html5lib")
link_elems = soup.select(".r a")

num_open = min(5, len(link_elems))
for i in range(num_open):
  webbrowser.open("https://google.com" + link_elems[i].get("href"))
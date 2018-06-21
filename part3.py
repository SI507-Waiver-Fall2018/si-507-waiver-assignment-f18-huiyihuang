# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py
r = requests.get("https://www.michigandaily.com/")
soup = BeautifulSoup(r.text,'html.parser')
most_read = soup.find_all(class_ = 'view-most-read')
for everyone in most_read:
	text = everyone.find_all("li")
	for everylist in text:
		name = everylist.string
		link = everylist.a['href']
		r_author = requests.get("http://michigandaily.com" + link)
		author_soup = BeautifulSoup(r_author.text,'html.parser')
		if author_soup.find_all("div",class_="byline"):
			author_link = author_soup.find_all(class_ = 'byline')
			for everylink in author_link:
				author_name = everylink.find_all( 'div', attrs = {'class':'link'})
				for everyauthor in author_name:
					author = everyauthor.contents[0].string
		else:
			author = 'DAILY STAFF WRITER'
		print(name, '\n', 'by', author)

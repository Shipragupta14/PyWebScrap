import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

film = []
duration = []
category = []
scores = []

page = requests.get("http://www.imdb.com/search/title?at=0&start=1&title_type=feature&year=1950,2012&sort=num_votes,desc")
soup = BeautifulSoup(page.content , 'html.parser')

name = soup.find_all(class_ = "lister-item-content")

for i in name:
	#print (i)
	title = i
	#print (title)
	movie = title.find('a')
	film_name = movie.get_text()
	print(film_name)
	film.append(film_name)


	head = title.find_all(class_ = "text-muted")
	time = head[1]
	#print (time)

	runtime = time.find(class_="runtime").get_text()
	print(runtime)
	duration.append(runtime)
	genre = time.find(class_= "genre").get_text()
	print(genre)
	category.append(genre)

	heading = title.find (class_ = "inline-block ratings-metascore")
	vote = heading.find_all(True,{'class':["metascore favorable", "metascore mixed"]})
	score = vote[0]
	metascore = score.get_text()
	print (metascore)
	scores.append(metascore)

	film_info = pd.DataFrame({
	"title": film, 
    "runtime": duration, 
    "genre": category,
    "metascore" : scores
	})
print(film_info)

film_info.to_csv("film.csv" , sep=',')
import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
#from urllib2 import urlopen



f = open('movie.txt','r')
title = []
review = []
year = []
for line in f:
	url = "http://www.imdb.com/title/"
	urls = url + (line.strip())
	page = requests.get(urls)
    
	soup = BeautifulSoup(page.content , 'html.parser')

	name = soup.find(class_= "title_wrapper")
	title_name = name.find_all(itemprop="name")
	item = title_name[0]
	movie_name = item.get_text()
	print(movie_name)
	title.append(movie_name.strip())


	block = soup.find_all(class_= "ratingValue")
	rate = block[0]
	rating = rate.get_text()
	print (rating)

	review.append(rating.strip())


	release = soup.find(class_="titleBar")
	r_array = release.find_all(class_="subtext")
	info = r_array[0]
#date = info.get_text()
	tag = info.findAll('a', title = "See more release dates")
	date = tag[0]
	release_date = date.get_text()
	print(release_date)

	year.append(release_date.strip())


movie_info = pd.DataFrame({
	"title": title, 
    "rating": review, 
    "Releasing_date": year
	})
print(movie_info)

movie_info.to_csv("movie.csv" , sep=',')
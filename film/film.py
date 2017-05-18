'''
Author - Shipra Gupta
Website Scrapped - http://www.imdb.com/search/title?at=0&start=1&title_type=feature&year=1950,2012&sort=num_votes,desc

'''
import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import re

film = []
duration = []
category = []
scores = []
dur = []

page = requests.get("http://www.imdb.com/search/title?at=0&start=1&title_type=feature&year=1950,2012&sort=num_votes,desc")
soup = BeautifulSoup(page.content , 'html.parser')

#finding all contents from the given class and store it into an array
name = soup.find_all(class_ = "lister-item-content")


for i in name:
	#print (i)
	#assigning the array values to the title variable one by one 
	title = i
	#print (title)
	#Extracting the <a> value from title 
	movie = title.find('a')
	#Extractacting the text value
	film_name = movie.get_text()
	print(film_name)
	#Store the movie title for each loop in 'film' array
	film.append(film_name)


	head = title.find_all(class_ = "text-muted")
	#Extracting the value from the 1st element of head array as the runtime and genre information is present in 1st element only
	time = head[1]
	#print (time)
	runtime = time.find(class_="runtime").get_text()
	#print(runtime)
	#Extracting substring from a string like extracting 142 from 142 min 
	m = re.search('(.+?) min', runtime)
	if m :
		#group(1) works to match like 'abc' = 'abc'
		found = m.group(1)  
		print(found)

	duration.append(found)
	dur.append(runtime)
	#print(duration)
	genre = time.find(class_= "genre").get_text()
	print(genre)
	category.append(genre)


	heading = title.find (class_ = "inline-block ratings-metascore")
	#Finding all the contents present in either 'metascore favorable' class or 'metascore mixed' class and store them into an array
	vote = heading.find_all(True,{'class':["metascore favorable", "metascore mixed"]})
	score = vote[0]
	metascore = score.get_text()
	print (metascore)
	scores.append(metascore)

#Making a dataframe  
film_info = pd.DataFrame({
	#dictionary = "key" : "value" where value must be in array form
	"title": film, 
    "runtime": dur, 
    "genre": category,
    "metascore" : scores
})
print(film_info)
#converting string into int 
time_duration = film_info["runtime"].str.extract("(?P<time_duration>\d+)", expand=False)
film_info["time_duration"] = time_duration.astype('int')

#print (film_info["runtime"].describe())

#film_info["runtime"] = film_info["runtime"].astype('int')
film_info["metascore"] = film_info["metascore"].astype('int')

#converting dataframe into .csv file 
film_info.to_csv("film.csv" , sep=',')


#Draw a graph using dataframe values where we have drawn 4 kinds of graphs in a matrix form
fig, axes = plt.subplots(nrows = 2,ncols = 2)
#xlim sets the range on x axis 
film_info.plot.scatter(subplots = True, x='metascore', y='time_duration',xlim = [50,100], style='o' , ax = axes[0,0])
film_info.plot( subplots = True,x='metascore', y='time_duration', style='o',kind = "bar", ax = axes[0,1])
film_info.plot( subplots = True,x='metascore', y='time_duration', style='o',kind = "hist", ax = axes[1,0])
film_info.plot( subplots = True,x='metascore', y='time_duration', style='o',kind = "pie" ,ax = axes[1,1])


#Draw a graph using array values b/w scores and runtime 
plt.figure(2)
plt.subplot(211)
t1 = np.arange(0.0, 5.0, 0.1)
plt.plot(t1,scores)
plt.plot(t1,duration)
plt.xlabel('movies')
plt.ylabel('blue-scores red-runtime')


plt.subplot(212)
plt.plot(duration,scores, 'ro')
plt.xlabel('runtime')
plt.ylabel('scores')
plt.show()

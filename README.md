# PyWebScrap
Python Web Scraping using Python 3.6 and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library and analyzing them using the [Pandas](http://pandas.pydata.org/) library.


__Install dependencies__ - ``pip install -r requirements.txt``

## Example 1 -  IMDB Movies List
Here we have done the data scraping from a webpage by using the **BeautifulSoup** library to find and print the **movie title, list of genres, runtime and scores of all movies.**
```python
page = requests.get("http://www.imdb.com/search/title?at=0&start=1&title_type=feature&year=1950,2012&sort=num_votes,desc")
soup = BeautifulSoup(page.content , 'html.parser')
```

and after extracting the data, we used **Pandas** library to make the DataFrame of that extracted data.
```python
film_info = pd.DataFrame({
	#dictionary = "key" : "value" where value must be in array form
	"title": film, 
    "runtime": dur, 
    "genre": category,
    "metascore" : scores
})
```
We have also use [matplotlib](https://matplotlib.org/) for data visualization by plotting the graph.
Then we have **Plotted the Graph** -
  * Using dataframe values where we have drawn 4 kinds of graphs in a matrix form.
  ```python
  fig, axes = plt.subplots(nrows = 2,ncols = 2)
film_info.plot.scatter(subplots = True, x='metascore', y='time_duration',xlim = [50,100], style='o' , ax = axes[0,0])
film_info.plot( subplots = True,x='metascore', y='time_duration', style='o',kind = "bar", ax = axes[0,1])
film_info.plot( subplots = True,x='metascore', y='time_duration', style='o',kind = "hist", ax = axes[1,0])
film_info.plot( subplots = True,x='metascore', y='time_duration', style='o',kind = "pie" ,ax = axes[1,1])
  ```
  * Using array values b/w scores and runtime
  ```python
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
  ```
Now, to import dataframe values into Excel sheet, we use 
```python
film_info.to_csv("film.csv" , sep=',')
```
How to Run - `` cd film && python film.py ``

## Example 2 - IMDB Movies Url from txt file
Here we have done the data scraping from movie.txt file bu using the **BeautifulSoup** library to find and print the **movie title, its ratings and its release date **. First we read the .txt file and then we access the page by concatenating each line of .txt file with the url.
```python
f = open('movie.txt','r')
for line in f:
	url = "http://www.imdb.com/title/"
	urls = url + (line.strip())
	page = requests.get(urls)
	soup = BeautifulSoup(page.content , 'html.parser')
```
Then, we made the DataFrame after extracting data from the page bu using **Pandas** library.
```python
movie_info = pd.DataFrame({
	"title": title, 
    "rating": review, 
    "Releasing_date": year
})
```
Now, we have convert the DataFrame into .csv file
```python
movie_info.to_csv("movie.csv" , sep=',')
```
How to Run - `` cd movie && python movie.py ``

## Example 3 - Weather forecast
Here we have done the web scraping using **BeautifulSoup** library to find and print the **period , short description, temperatue and weather description.**
```python
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content , 'html.parser')
```
Then, we made the DataFrame by using **Pandas** library.
```python
weather_forecast = pd.DataFrame({
        "period": period, 
        "short_desc": short_desc, 
        "temp": temp, 
        "desc":desc
 })
```
We added one more column to the DataFrame by converting the string value to the integer one to find the minimum, maximum and mean values of the temperature and let them sort in the ascending order.
```python
temp_num = weather_forecast["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather_forecast["temp_num"] = temp_num.astype('int')
print(weather_forecast["temp_num"].mean())
print(weather_forecast["temp_num"].max())
print(weather_forecast["temp_num"].min())
print(weather_forecast.sort(["temp_num","period"] , ascending=[True,True]))
```
Now, we have convert the DataFrame in the form of Excel sheet 
```python
weather_forecast.to_csv("weather.csv" , sep=',')
```
How to Run - `` cd weather && python weather.py ``




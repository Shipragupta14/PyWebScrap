import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content , 'html.parser')
seven_day = soup.find(id = "seven-day-forecast")
items = seven_day.find_all(class_="tombstone-container")
day = items[0]
period = day.find(class_="period-name").get_text()
short_desc = day.find(class_="short-desc").get_text()
temp = day.find(class_="temp").get_text()
image = day.find("img")
desc = image['title']
print ('\n',"Extracting information of 1st element of page", '\n')
print(period)
print(short_desc)
print(temp)
print (desc)


period = [p.get_text() for p in seven_day.select(".tombstone-container .period-name")]
short_desc = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temp = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
desc = [d["title"] for d in seven_day.select(".tombstone-container img")]
print ('\n',"Extracting all the information of the page",'\n')
print(period)
print(short_desc)
print(temp)
print(desc)


weather_forecast = pd.DataFrame({
        "period": period, 
        "short_desc": short_desc, 
        "temp": temp, 
        "desc":desc
    })
print ('\n',"Weather forecast in the table form by combining data with Pandas DataFrame",'\n')
print(weather_forecast)
temp_num = weather_forecast["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather_forecast["temp_num"] = temp_num.astype('int')
print ('\n',"Mean of the temperatures in a week",'\n')
print(weather_forecast["temp_num"].mean())
print ('\n'"Maximum temperature of the week",'\n')
print(weather_forecast["temp_num"].max())
print ('\n',"Min temperature of the week",'\n')
print(weather_forecast["temp_num"].min())
print('\n',"Sorting the temperature",'\n')
print(weather_forecast.sort(["temp_num","period"] , ascending=[True,True]))


print ('\n',"Select the rows that happen at night",'\n')
night = weather_forecast["temp"].str.contains("Low")
weather_forecast["night"] = night
print(weather_forecast[night])

print ('\n',"Select the rows that happen at noon",'\n')
noon = weather_forecast["temp"].str.contains("High")
weather_forecast["noon"] = noon
print(weather_forecast[noon])

weather_forecast.to_csv("weather.csv" , sep=',')

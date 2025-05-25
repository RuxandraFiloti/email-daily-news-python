import requests
from send_email import send_email

topic = "tesla"  #the topic of the news

#the api key is from websote newsapi.org
api_key = "50c5153425904f9bbbf0f372fe24c460"

#the url for the request
url = "https://newsapi.org/v2/everything?" \
f"q={topic}&from=2025-04-25&sortBy=publishedAt&" \
"apiKey=50c5153425904f9bbbf0f372fe24c460&" \
"language=en" #i added the language parameter to filter articles in English; for more parameters, 
#check the documentation from newsapi.org 
#another parameter is sortBy

#make a request
request = requests.get(url)

#get the dictionary of with data 
content = request.json() #json() method converts the response to a Python dictionary

body = ""
#access the articles and the description
for article in content["articles"][0:20]:  #get the first 20 articles
    if article["title"] and article["description"] is not None:
        body = "Subhect: Today's News:" + "\n" \
        + body + article["title"] + "\n" + \
        article["description"] + "\n" \
        + article["url"]+ 2*"\n"

body = body.encode("utf-8")  #encode the body to utf-8 format
#send the email
send_email(message=body)


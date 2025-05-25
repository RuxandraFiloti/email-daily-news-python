import requests
import streamlit as st

#prepare the api key and api url

api_key = "sjfFkjt4Ua9j2m8C3VGSbFFdXaFmvuP6P3pHNkVp"
api_url = "https://api.nasa.gov/planetary/apod?"f"api_key={api_key}"

#get the request data as a dictionary
response1 = requests.get(api_url)
data = response1.json()

#extract the image title, url and explanation
title = data["title"]
image_url = data["url"] 
explanation = data["explanation"]

#download the image
image_filepath = "nasa_image.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)



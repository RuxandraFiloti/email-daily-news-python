import requests
#this works for other types of files, not only images, you need to change the extension of the file and url

url = "https://ro.wikipedia.org/wiki/C%C3%A2ine#/media/Fi%C8%99ier:Montage_of_dogs.jpg" # URL of the image to download 

response = requests.get(url)

print(response.status_code)  # Check if the request was successful (200 OK)
response.content  # This contains the binary content of the response
with open("downloaded_image.jpg", "wb") as file:
    file.write(response.content)  # Write the binary content to a file
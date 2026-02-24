import requests
from dotenv import load_dotenv
import os

load_dotenv()

NASA_API = os.getenv("NASA_API")

url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API}"

response = requests.get(url)

data = response.json()

image_url = data.get("url")

image = requests.get(image_url, stream=True)

with open("nasa_image.jpg", "wb") as file:
    for chunk in image.iter_content(chunk_size=8192):
        file.write(chunk)


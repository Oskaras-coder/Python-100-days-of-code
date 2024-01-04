import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
all_movies = soup.find_all(name="h3")[::-1]
with open("movies.txt", "w", encoding='utf-8') as file:
    for movie in all_movies:
        movie_name = movie.getText()
        file.write(f"{movie_name}\n")


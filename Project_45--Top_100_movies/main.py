from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
movie_website = response.text

soup = BeautifulSoup(movie_website, "html.parser")

movies_list = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movies_list]

arranged_movie_titles = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in arranged_movie_titles:
        file.write(f"{movie}\n")

from bs4 import BeautifulSoup
import requests
WEBSITE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(WEBSITE_URL)

soup = BeautifulSoup(response.text, "html.parser")
movie_names = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movie_names = movie_names[::-1]
movie_names = "\n".join(movie_names)
with open("movies.txt", "w") as file:
    file.write(movie_names)
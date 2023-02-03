from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_input = input("Which year do you want to travel to? Type the date in this format YYY-MM-DD:")

URL = "https://www.billboard.com/charts/hot-100/" + user_input

response = requests.get(URL)
billboard_website = response.text

soup = BeautifulSoup(billboard_website, "html.parser")

songs_titles = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")


songs_list = [title.getText().strip() for title in songs_titles]
print(songs_list)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR_ID",
        client_secret="YOUR_SECRET_KEY",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

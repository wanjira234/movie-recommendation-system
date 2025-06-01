# omdb_utils.py
import requests
from urllib.parse import quote

def get_movie_details(title, api_key):
    # Encode the movie title to handle spaces and special characters
    encoded_title = quote(title)
    url = f"http://www.omdbapi.com/?t={encoded_title}&plot=full&apikey={api_key}"
    
    try:
        response = requests.get(url)
        res = response.json()
        
        if res.get("Response") == "True":
            plot = res.get("Plot", "Plot not available")
            poster = res.get("Poster", "No Poster Found")
            return plot, poster
        
        return "Plot not available", "No Poster Found"
    except:
        return "Error fetching movie details", "No Poster Found"
    
import requests
import os


api_key = os.environ.get('ressources/api.env')

def get_movie_poster_url(tmdb_id):
    base_url = 'https://api.themoviedb.org/3/movie/'
    endpoint = f'{tmdb_id}?api_key={api_key}'
    response = requests.get(base_url + endpoint)
    if response.status_code == 200:
        data = response.json()
        if 'poster_path' in data:
            poster_path = data['poster_path']
            return f'https://image.tmdb.org/t/p/w500/{poster_path}'
    return None

def get_movie_synopsis(tmdb_id):
    base_url = 'https://api.themoviedb.org/3/movie/'
    endpoint = f'{tmdb_id}?api_key={api_key}&language=fr-FR'
    response = requests.get(base_url + endpoint)
    if response.status_code == 200:
        data = response.json()
        if 'overview' in data:
            return data['overview']
    return None


import requests

# movie_id = 
url = 'https://api.themoviedb.org/3/movie/search/movies'
payload = {
    'api_key': '20e1d94831b618c7e8aa2b5edb1c27a0',
    'language': 'ko-Kr',
    # 'query': 검색어
}
# '?api_key=20e1d94831b618c7e8aa2b5edb1c27a0&language=en-US'
response = requests.get(url, params=payload)

print(type(response.json()))
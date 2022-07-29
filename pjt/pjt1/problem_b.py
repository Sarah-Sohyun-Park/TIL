import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    movie_in = dict()

    for k in movie:
        if k in keys:
            movie_in[k] = movie[k]


    movie_id = movie_in['genre_ids']
    # print(movie_id)
    genre_names = []

    for genre in genres:
        for m_id in movie_id:
            if genre['id'] == m_id:
                genre_names.append(genre['name'])

    del movie_in['genre_ids']
    movie_in['genre_names'] = genre_names

    return movie_in
              



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

   
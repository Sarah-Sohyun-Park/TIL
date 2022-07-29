import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.
    keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    movie_in = dict()
    for k in movie:
        if k in keys:
            movie_in[k] = movie[k]

    return dict(movie_in)
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))


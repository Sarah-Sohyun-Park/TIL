import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    id_list = []
    release_movies = []
    for movie in movies:
        max_id.append(movie['id'])

    for m_id in id_list:
        movies_sell = open(f'data/movies/{m_id}.json', encoding='UTF8')
        movies_newlist = json.load(movies_sell)
            if movies_newlist['release_date'][5:7] == '12':
                release_movies.append(movies['id'])

    max_sort_dict = sorted(max_dict.items(), key= lambda x: x[1], reverse = True)
    max_id = max_sort_dict[0][0]
    for movie in movies:
        if movie['id'] == max_id:
            max_title += movie['title']
        # if genre['id'] == m_id:
        #     genre_names.append(genre['name'])

    return max_title        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
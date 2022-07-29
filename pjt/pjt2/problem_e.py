import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다. 
    try: 
        url = 'https://api.themoviedb.org/3/search/movie'

        
        payload ={
            'api_key': '20e1d94831b618c7e8aa2b5edb1c27a0',
            'language': 'ko-Kr',
            'query': title,
            'page': '1',
            'include_adult': 'false',
        }
        
        response = requests.get(url, params=payload)
        search_mv = response.json()
        search_mv_r = search_mv['results']
        mv_id = search_mv_r[0]['id']

        movie_id = mv_id
        url3 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
        payload3 ={
            'api_key': '20e1d94831b618c7e8aa2b5edb1c27a0',
            'language': 'ko-Kr',
        }
        
        response3 = requests.get(url3, params=payload3)
        credit_d = response3.json()
        credit_cast = credit_d['cast']
        credit_crew = credit_d['crew']

        cc_data = {'cast': [], 'directing': []}
        for cast in credit_cast.value():
            if cast['cast_id'] < 10:
                cc_data['cast'].append(cast['original_name'])

        for crew in credit_crew:
            if crew['known_for_department'] == 'Directing':
                cc_data['crew'].append(crew['original_name'])

        return cc_data

    except:
        return 'None'



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

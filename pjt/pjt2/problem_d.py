import requests
from pprint import pprint


def recommendation(title):
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
        url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
        payload2 ={
            'api_key': '20e1d94831b618c7e8aa2b5edb1c27a0',
            'language': 'ko-Kr',
            'page': '1',
        }
        
        response2 = requests.get(url2, params=payload2)
        commend_mv = response2.json()
        command_r = commend_mv['results']
        new_list = []

        for c_mv in command_r:
            new_list.append(c_mv['title'])

        return new_list

    except:
        return None




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None

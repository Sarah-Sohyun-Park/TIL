import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    url = 'https://api.themoviedb.org/3/movie/popular'
    # ?api_key=20e1d94831b618c7e8aa2b5edb1c27a0&language=en-US&page=1


    payload ={
        'api_key': '20e1d94831b618c7e8aa2b5edb1c27a0',
        'language': 'ko-Kr',
        'page': '1'
    }
    response = requests.get(url, params=payload)

    pmv_page = response.json()
    length_pmw = len(pmv_page['results'])
    return length_pmw


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20

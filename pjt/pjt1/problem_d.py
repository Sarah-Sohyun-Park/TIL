import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.
    max_id = []
    max_dict = dict()
    max_title = ''
    for movie in movies:
        max_id.append(movie['id'])

    for m_id in max_id:
        movies_sell = open(f'data/movies/{m_id}.json', encoding='UTF8')
        movies_newlist = json.load(movies_sell)
        max_dict[m_id] = movies_newlist['revenue']

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
    max_revenue(movies_list)
    # print(max_revenue(movies_list))
    print(max_revenue(movies_list))
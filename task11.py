from pprint import pprint
from task9 import scrape_movie_json
from pprint import pprint

def analyse_movies_genre():
    movie_genre=scrape_movie_json()
    genre_dict={}
    for g in movie_genre:
        for h in g["genre"]:
            if h in genre_dict:
                genre_dict[h]+=1
            else:
                genre_dict[h]=1
    # pprint(genre_dict)
            

# analyse_movies_genre()

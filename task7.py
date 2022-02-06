from pprint import pprint
from task5 import get_movie_list_details

director_list=get_movie_list_details()

def analyse_movies_directors():
    director_dict={}
    for d in director_list:
        for e in d["director"]:
            if e in director_dict:
                director_dict[e]+=1
            else:
                director_dict[e]=1
    # pprint(director_dict)
            
# analyse_movies_directors()
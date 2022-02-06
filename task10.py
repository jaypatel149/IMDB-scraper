from pprint import pprint
from task9 import scrape_movie_json
from pprint import pprint


def analysis_language_and_directors():
    movie_json=scrape_movie_json()
    director_dict={}
    for j in movie_json:
        for dire in j["director"]:
            if dire not in director_dict:
                director_dict[dire]={}
            for lan in j["language"]:
                if lan not in director_dict[dire].keys():
                    director_dict[dire][lan]=1
                else:
                    director_dict[dire][lan]+=1
    # pprint(director_dict)

# analysis_language_and_directors()
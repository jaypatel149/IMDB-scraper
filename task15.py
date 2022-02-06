from task13 import movie_cast_movie_details
from pprint import pprint
import json


def analyse_actors():
    cast_dict={}
    data=movie_cast_movie_details()
    for c in data:
        for d in c["cast"]:
            if d['imdb_id'] not in cast_dict:
                cast_dict[d['imdb_id']]={}
                cast_dict[d['imdb_id']]['name'] = d['name']
                cast_dict[d['imdb_id']]['num_movie'] = 1
            else:
                cast_dict[d['imdb_id']]['num_movie'] += 1
    pprint(cast_dict)

analyse_actors()
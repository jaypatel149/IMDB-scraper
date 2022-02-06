import random,time
from task4 import scrape_movie_details
from os import path
import json 
from pprint import pprint


with open("all_movies.json","r")as var:
    url=json.load(var)
    var.close()


def scrape_movie_json():
    time.sleep(random.randint(3,5))
    main_list = []
    for j in url:
        url_name=j["url"]
        file_name="movies/"+url_name[27:36]+".json"
        if path.exists(file_name):
            all_movie = json.load(open(file_name))
        else:
            all_movie=scrape_movie_details(url_name)
            with open(file_name,"w+") as file:
                json.dump(all_movie,file,indent=6)
        main_list.append(all_movie)
    return main_list
            
# pprint(scrape_movie_json())

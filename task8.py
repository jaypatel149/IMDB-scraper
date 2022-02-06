from os import path
import json 
from task4 import scrape_movie_details
from pprint import pprint

with open("all_movies.json","r")as var:
    url=json.load(var)
    var.close()


def scrape_movie_json():
    for j in url[:10]:
        url_name=j["url"]
        file_name="movies/"+url_name[27:36]+".json"
        # all_movie=scrape_movie_details(url_name)
        # with open(file_name,"w+") as file:
        #     json.dump(all_movie,file,indent=6)
        

            
# scrape_movie_json()

from task4 import scrape_movie_details
import json
from pprint import pprint

with open("all_movies.json","r")as var:
    url=json.load(var)
    var.close()
def get_movie_list_details():
    mainlist = []
    for movie in url[:10]:
        mainlist.append(scrape_movie_details(movie['url']))
    return mainlist

# get_movie_list_details()
import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint
from os import path
from task4 import scrape_movie_details
from task12 import scrape_movie_cast

with open("all_movies.json","r")as var:
    url=json.load(var)
    var.close()
    
def movie_cast_movie_details():
    new_list=[]
    for u in url[:15]:
        url1=u["url"]
        movie_detail=scrape_movie_details(url1)
        link=url1+"fullcredits/?ref_=tt_cl_sm"
        cast=scrape_movie_cast(link)
        movie_detail["cast"]=cast
        new_list.append(movie_detail)
    
    return new_list

# movie_cast_movie_details()
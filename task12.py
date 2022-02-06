import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

with open("all_movies.json","r")as var:
    url=json.load(var)
    var.close()

def scrape_movie_cast(link):
    data=requests.get(link)
    soup=BeautifulSoup(data.text,"html.parser")
    table=soup.find("table",class_="cast_list")
    trs=table.find_all("tr")
    imdb_list=[]
    for t in trs:
        td=t.find("td",class_="")
        if td !=None:
            cast_dict={}
            name=td.find("a").text
            imdb_id=td.find("a")["href"][6:15]
            cast_dict["name"]=name.strip()
            cast_dict["imdb_id"]=imdb_id
            imdb_list.append(cast_dict)

    return imdb_list
    # print(imdb_list)
            

# scrape_movie_cast("https://www.imdb.com/title/tt8176054/fullcredits/?ref_=tt_cl_sm")
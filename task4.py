import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

# with open("all_movies.json","r")as var:
#     url=json.load(var)
#     var.close()


def scrape_movie_details(link):
    dict = {}
    movies_details=[]
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    name = soup.find("div", class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.text
    Director = soup.find("li", class_="ipc-metadata-list__item")
    d = Director.find_all("a")
    l = []
    for i in d:
        b = (i.text)
        l.append(b)
    country = soup.find("li", attrs={"data-testid": "title-details-origin"})
    count = country.find("a").text
    lol = []
    language = soup.find("li", attrs={"data-testid": "title-details-languages"})
    lan = language.find("a").text
    lol.append(lan)

    poster = soup.find("img", class_="ipc-image")["src"]
    Bio = soup.find("span", class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-sc-cum89p-0 kHlJyu").text

    rantime = soup.find("li", attrs={"data-testid": "title-techspec_runtime"})
    r = rantime.find("div", class_="ipc-metadata-list-item__content-container").text
    run=r.split(" ")
    if len(run)==4:
        minuts=int(run[0])*60+int(run[2])
    else:
        minuts=int(minuts[0])*60
   
    list1=[]
    ganre=soup.find("li",attrs={"data-testid":"storyline-genres"})
    g=ganre.find("a").text
    list1.append(g)
    
    dict["name"]=name
    dict["director"]=l
    dict["country"]=count
    dict["language"]=lol
    dict["poster_image_url"]=poster
    dict["bio"]=Bio
    dict["runtime"]=minutes
    dict["genre"]=list1
    movies_details.append(dict)
    
    return dict
scrape_movie_details("https://www.imdb.com/title/tt8176054/")

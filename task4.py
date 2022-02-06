import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

# with open("all_movies.json","r")as var:
#     url=json.load(var)
#     var.close()


def scrape_movie_details(link):
    dict = {}
    # movies_details=[]
    # for i in url[:10]:
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
    # print(Bio, "Bio hai")

    rantime = soup.find("li", attrs={"data-testid": "title-techspec_runtime"})
    ran1 = rantime.find("div", class_="ipc-metadata-list-item__content-container").text
    ran = ran1.replace(" hours", "").replace(" minutes", "").replace(" hour", "").replace(" minute", "").replace(" h", "").replace(" m", "")
    sp = ran.split(' ')
    t_minutes = 0
    if len(sp) == 2:
        t_minutes += int(sp[0])*60
        t_minutes += int(sp[1]) 
    elif len(sp) == 1:
        if "h" in ran1:
            t_minutes += int(sp[0])*60 
        else:  
            t_minutes += int(sp[0])
   
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
    dict["runtime"]=t_minutes
    dict["genre"]=list1

    # movies_details.append(dict)
    # file = open("movies.json", "r")
    # old_data = json.load(file)
    # old_data.append(dict)
    # file = open("movies.json", "w")
    # file.write(json.dumps(old_data, indent=6))
    # pprint(movies_details)
    return dict

# pprint(scrape_movie_details("https://www.imdb.com/title/tt8176054/"))

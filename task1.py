import requests,json
from bs4 import BeautifulSoup
from pprint import pprint

url="https://www.imdb.com/india/top-rated-indian-movies/"
data=requests.get(url)
soup=BeautifulSoup(data.text,"html.parser")



def scrape_top_list():
    movies_list=[]
    main_div=soup.find("tbody",class_="lister-list")
    Tr=main_div.findAll("tr")

    movie_position=[]
    movie_name=[]
    year_movie=[]
    rating_movie=[]
    url_movie=[]
    for i in Tr:
        dic={}

        position=i.find("td",class_="titleColumn").get_text().strip()
        rank=" "
        for j in position:
            if "." not in j:
                rank=rank+j
            else:
                break
            movie_position.append(rank)

        title=i.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)

        year=i.find("td",class_="titleColumn").span.get_text().strip("()")
        year_movie.append(year)

        rate=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        rating_movie.append(rate)


        link=i.find("td",class_="titleColumn").find("a").attrs['href']
        url="https://www.imdb.com"+link
        url_movie.append(url)
        
        dic["position"]=int(rank)
        dic["name"]=title
        dic["year"]=int(year)
        dic["raning"]=float(rate)
        dic["url"]=url
        movies_list.append(dic)
        # file=open("all_movies.json","w")
        # json.dump(movies_list,file,indent=4)
        # file.close()

        # pprint(movies_list) 

# scrape_top_list()

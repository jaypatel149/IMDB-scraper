import json
from pprint import pprint
from task4 import scrape_movie_details
from task12 import scrape_movie_cast


with open("all_movies.json","r")as var:
    url=json.load(var)
    var.close()

def analyse_co_actors():
    main_dict={}
    for u in url[:15]:
        url2=u["url"]
        movie_link=url2+"fullcredits/?ref_=tt_cl_sm"
        a=scrape_movie_cast(movie_link)
        for k in a[:5]:
            if k['imdb_id'] not in main_dict:
                main_dict[k['imdb_id']] = {"name": k['name'],'frequent_co_actors': []}
                fc = main_dict[k['imdb_id']]['frequent_co_actors']
                for k2 in a:
                    fc.append({'imdb_id': k2['imdb_id'], "name": k2['name'], "num_movies": 1})
            else:
                fc = main_dict[k['imdb_id']]['frequent_co_actors']
                for k2 in a:
                    for kf in fc:
                        if k2['imdb_id'] == kf['imdb_id']:
                            kf['num_movies']+=1
                            break
                    else:
                        fc.append({'imdb_id': k2['imdb_id'], "name": k2['name'], "num_movies": 1})
    # pprint(main_dict)        
        
        

# analyse_co_actors()
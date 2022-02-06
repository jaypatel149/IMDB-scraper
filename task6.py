from pprint import pprint
from task5 import get_movie_list_details

movie_list = get_movie_list_details()


def analyse_movies_language():
    language_dict={}
    for i in movie_list:
        for j in i["language"]:
            if j in language_dict:
                language_dict[j]+=1
            else:
                language_dict[j]=1


    # pprint(language_dict)

# analyse_movies_language()
# import json
# from pprint import pprint




# with open("all_movies.json","r")as file:
#     movies=json.load(file)
# pprint(movies)

# def group_by_year(movies):
#     dict1={}
#     for i in movies:
#         a=i["year"]
#         if a not in dict1:

#             dict1[a]=[]
#         else:
#             dict1[a].append(i)

#     return dict1

# pprint(group_by_year(movies))
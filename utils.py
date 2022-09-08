"""
UTILS 
- Helper functions to use for your recommender funcions, etc
- Data: import files/models here e.g.
    - movies: list of movie titles and assigned cluster
    - ratings
    - user_item_matrix
    - item-item matrix 
- Models:
    - nmf_model: trained sklearn NMF model
"""
import pandas as pd
import numpy as np
from thefuzz import process
import pickle


movies = pd.read_csv("./data/movies.csv", index_col=0) 

# 2. load trained NMF model
with open('./data/nmf_recommender.pkl', 'rb') as file:
    model = pickle.load(file)


def match_movie_title(input_title, movie_titles):
    """
    Matches inputed movie title to existing one in the list with fuzzywuzzy
    """
    matched_title = process.extractOne(input_title, movie_titles)[0]

    return matched_title




def lookup_movieId(movies, movieId):
    """
    Convert output of recommendation to movie title
    """
    # match movieId to title
    movies = movies.reset_index()
    boolean = movies["movieId"] == movieId
    movie_title = list(movies[boolean]["title"])[0]
    return movie_title



def lookup_movie_name(movies, user_movie_titles):
    """
    Convert output of recommendation to list of movie ids
    """
    # match title to movieId

 #   movie_titles = list(movies["title"])
 #   intended_movies = [match_movie_title(title, movie_titles) for title in user_movie_titles]
    
    movies = movies.reset_index()
 #   boolean = movies["title"].isin(intended_movies)
    boolean = movies["title"].isin(user_movie_titles)
    movie_id = list(movies[boolean]["movieId"])
    return movie_id

def print_movie_columns(movies):
    print("")
    print("******")
    print("")
    print("")
    print(movies.columns)
    print(movies.head(2))


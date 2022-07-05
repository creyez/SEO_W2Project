import requests
import random
import pandas as pd
import sqlalchemy as db

tmdbKey = ""
omdbKey = ""

def getGenre():


def getUserRating():


def getStreamingServices():



def getMovies(genre = None, userRating = None, streamingServices = None):
    if genre == None and userRating == None and streamingServices == None:
        url = "https://api.themoviedb.org/3/discover/movie?api_key=" + tmdbKey + \
              "&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"

        response = requests.get(url)
        response = response.json()
        totalPages = response['total_pages']

        if totalPages > 500:
            totalPages = 500

        randomPage = random.randint(1, totalPages)

        url = "https://api.themoviedb.org/3/discover/movie?api_key=" + tmdbKey + \
             "&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=" + str(randomPage)

    response = requests.get(url)
    response = response.json()

    return response

def displayMovie(data):
    response = requests.get(url)
    response = response.json()

def getStreamingServices(movieData):


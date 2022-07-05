import requests
import random
import pandas as pd
import sqlalchemy as db

tmdbKey = ""
omdbKey = ""

def getGenre():
    url = "https://api.themoviedb.org/3/genre/movie/list?api_key=" + tmdbKey + "&language=en-US"
    response = requests.get(url)
    response = response.json()

    genreList = [genre['name'] for genre in response['genres']]
    idList = [genre['id'] for genre in response['genres']]

    genreOrNo = input("Would you like to specify a genre for the movie suggestion? (yes or no): ")

    if genreOrNo.lower() == "yes":
        print("Here are the genres available:")
        print(genreList)

        userGenre = input("Enter a genre: ").lower().capitalize()

        while userGenre not in genreList:
            userGenre = input("Invalid input. Enter a genre listed above: ").lower().capitalize()

        return idList[genreList.index(userGenre)]

    elif genreOrNo.lower() == "no":
        return -1
    else:
        print("Invalid input. Type 'yes' or 'no'")
        getGenre()



def getUserRating():
    rating = input("Would you like to specify a minimum user rating? (yes or no): ")


# def getStreamingServices():



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

print(getGenre())

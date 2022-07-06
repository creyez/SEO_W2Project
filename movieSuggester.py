import requests
import random
import pandas as pd
import sqlalchemy as db

tmdbKey = "37909ab2a58f4d635646887a974c77a1"
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
        return ""
    else:
        print("Invalid input. Type 'yes' or 'no'")
        getGenre()


def getUserRating():
    ratingOrNO = input("Would you like to specify a minimum user rating? (yes or no): ")

    if ratingOrNO.lower() == "yes":
        print("User ratings range from 0 to 10. For reference, most popular movies have an average user rating "
              "between 6 and 8")

        while True:
            try:
                userRating = float(input("Enter a minimum user rating: "))
                while userRating < 0 or userRating > 10:
                    userRating = float(input("Invalid input. Enter an number between 0 and 10: "))
                break
            except:
                print("Error: input should be a number.", end=" ")

        return userRating

    elif ratingOrNO.lower() == "no":
        return ""
    else:
        print("Invalid input. Type 'yes' or 'no'")
        getUserRating()


def getStreamingServices():
    streamingServices = ["Netflix", "Amazon Prime Video", "Hulu", "Paramount Plus", "HBO max", "Peacock", "ShowMax",
                         "Apple Tv Plus", "Crunchyroll", "Disney Plus",
                         "HBO Go", "The Roku Channel", "Discovery Plus", "Showtime", "Apple iTunes", "Netflix Kids",
                         "Youtube Premium", "Google Play Movies"]

    idList = [8, 119, 15, 531, 384, 386, 55, 350, 283, 390, 31, 207, 510, 37, 2, 175, 188, 3]

    serviceOrNo = input("Would you like to specify a streaming service? (yes or no): ")

    if serviceOrNo.lower() == "yes":
        print("Here are the streaming services available:")
        print(streamingServices)

        userSS = input("Enter the streaming services you have (separate them with a space): ").strip().split(" ")
        userSS = [service.lower().capitalize() for service in userSS]

        validInput = True

        for service in userSS:
            if service not in streamingServices:
                validInput = False

        while validInput == False:
            validInput = True
            userSS = input("Invalid input. Enter any of the streaming services listed above: ").strip().split(" ")
            userSS = [service.lower().capitalize() for service in userSS]
            for service in userSS:
                if service not in streamingServices:
                    validInput = False

        return [idList[streamingServices.index(service)] for service in userSS]

    elif serviceOrNo.lower() == "no":
        return ""
    else:
        print("Invalid input. Type 'yes' or 'no'")
        getStreamingServices()


def getMovies(genre="", userRating="", streamingServices=""):
    if streamingServices != "":
        selectedSS = random.choice(streamingServices)
    else:
        selectedSS = ""

    url = "https://api.themoviedb.org/3/discover/movie?api_key=" + tmdbKey + "&language=en-US" \
                                                                             "&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&vote_count.gte=20&vote_average.gte" \
                                                                             "=" + str(
        userRating) + "&with_genres=" + str(genre) + "&with_watch_providers=" + str(selectedSS) + \
          "&watch_region=US"

    response = requests.get(url)
    response = response.json()
    totalPages = response['total_pages']

    if totalPages > 500:
        totalPages = 500

    randomPage = random.randint(1, totalPages)

    url = "https://api.themoviedb.org/3/discover/movie?api_key=" + tmdbKey + \
          "&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=" + str(randomPage) + \
          "&vote_count.gte=20&vote_average.gte=" + str(userRating) + "&with_genres=" + str(
        genre) + "&with_watch_providers=" + \
          str(selectedSS) + "&watch_region=US"

    response = requests.get(url)
    response = response.json()

    return response


def displayMovie(movie):
    url = 'http://www.omdbapi.com/?t=' + movie_name
    movie_name = movie.replace(" ", "+")

    response = requests.get(url)
    response = response.json()

    


def createDatabase(data):
    # Convert python dict into pandas data frame
    # convert pandas data frame to a sql dataframe 
    # query a result
    # display the result to the user 
    pass


movies = getMovies(getGenre(), getUserRating(), getStreamingServices())

movie_title = movies["results"][0]["title"]


print(movie_title.replace(" ", "+"))

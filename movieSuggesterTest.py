import unittest
from movieSuggester import getGenre, getUserRating, checkUserRating, getStreamingServices, getMovies, displayMovie

class TestFileName(unittest.TestCase):
    def test_getGenre(self):
        # Testing the APIs response to make sure its not invalid and to 
        # make sure the genreList and idList are not empty
        id_returned = getGenre()
        if type(id_returned) == list:
            self.assertNotEqual(len(id_returned), 0)

    def test_getUserRating(self):
        # Checking that getUserRating only returns a rating
        # between 0 and 10 and is a float
        rating = getUserRating()
        if rating != '':
            self.assertEqual(type(rating), float)
            self.asserTrue(0 <= rating <= 10)
         
    def test_getStreamingServices(self):
        # Checking that if the user decided to enter a streaming services 
        # the list being returned is not empty
        user_choice = getStreamingServices() 
        if type(user_choice) == list:
            self.assertNotEqual(len(user_choice), 0)

    def test_getMovies(self):
        # Testing the APIs response to make sure its a python dictionary
        response = getMovies(genre="", userRating="", streamingServices="")
        self.assertEqual(type(response), dict)
 
    def test_displayMovie(self):
        # Testing the APIs response to make sure its not invalid and to make sure the json 
        # response is a list of dictionaries
        pass



if __name__ == '__main__':
    unittest.main()
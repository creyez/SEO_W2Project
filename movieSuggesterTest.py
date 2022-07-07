import unittest
from movieSuggester import getGenre, getUserRating, getStreamingServices, getMovies, displayMovie

class TestFileName(unittest.TestCase):
    # def setUp(self):
    #     self.tmdbKey = "37909ab2a58f4d635646887a974c77a1"

    # def tearDown(self):
    #     self.tmdbKey = ''

    def test_getGenre(self):
        # Testing the APIs response to make sure its not invalid and to 
        # make sure the genreList and idList are not empty

        id_returned = getGenre()
        if type(id_returned) == list:
            self.assertNotEqual(len(id_returned), 0)

    def test_getUserRating(self):
        # Checking that an exception is raised if the user inputs a value 
        # that cannot be converted into a float

        # with self.assertRaises(ValueError) as exception_context:


        # self.assertRaises()
        pass


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
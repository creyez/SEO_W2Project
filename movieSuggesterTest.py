import unittest
import requests
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
            self.assertEqal(len(id_returned) > 0)

    def test_getUserRating(self):
        # Checking that an exception is raised if the user inputs a value 
        # that cannot be converted into a float

        with self.assertRaises(ValueError) as exception_context:


        self.assertRaises()


    def test_getStreamingServices(self):
        # Checking that if the user decided to enter a streaming services 
        # the list being returned is not empty

        user_choice = getStreamingServices() 
        if type(user_choice) == list:
            self.assertEqual(len(user_choice) > 0)


    # def test_getMovies(self):
    #     # Testing the APIs response to make sure its not invalid and to make sure the json 
    #     # response is a list of dictionaries
    #     fake_json = [{'some':'something'}]

    #     with patch('movieSuggester.getMovies') as mock_get:
    #         mock_get.return_value.status_code = 200
    #         mock_get.return_value.json().return_value = fake_json
    #         response = getMovies.get()

    #     self.assertEqal(response.status_code, 200)
    #     self.assertEqal(response.json(), fake_json)

        
    def test_displayMovie(self):
          # Testing the APIs response to make sure its not invalid and to make sure the json 
        # response is a list of dictionaries
        pass



if __name__ == '__main__':
    unittest.main()
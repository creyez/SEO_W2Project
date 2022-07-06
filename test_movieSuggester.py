import unittest
from unittest.mock import patch
from movieSuggester import getGenre, getUserRating, getStreamingServices, getMovies, displayMovie

class TestMovieSuggester(unittest.TestCase):
    def test_movie(self):
        fake_json = [{'':''}]

        with patch('movieSuggester.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

    def test_function2(self):
        pass

if __name__ == '__main__':
    unittest.main()
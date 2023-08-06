import unittest
import json

from theoneapi.client import Client
from theoneapi.query import Query


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.client = Client('ACCESS_TOKEN')
        self.query = Query()

    def test_get_one(self):
        expected = {"docs":[{"_id":"5cd95395de30eff6ebccde56","name":"The Lord of the Rings Series","runtimeInMinutes":558,"budgetInMillions":281,"boxOfficeRevenueInMillions":2917,"academyAwardNominations":30,"academyAwardWins":17,"rottenTomatoesScore":94}],"total":1,"limit":1000,"offset":0,"page":1,"pages":1}
        actual = json.loads(self.client.movie.get_one('5cd95395de30eff6ebccde56'))
        self.assertEqual(expected, actual, 'Incorrect record returned.')

    def test_get_all(self):
        expected = 8
        actual = len(json.loads(self.client.movie.get_all())['docs'])
        self.assertEqual(expected, actual, 'Incorrect number of records returned.')

    def test_get_all_limit(self):
        expected = 3
        self.query.paginate(limit=3)
        actual = len(json.loads(self.client.movie.get_all(self.query))['docs'])
        self.query.reset()
        self.assertEqual(expected, actual, 'Incorrect number of records returned.')

    def test_get_all_match(self):
        expected = {"docs":[{"_id":"5cd95395de30eff6ebccde5b","name":"The Two Towers","runtimeInMinutes":179,"budgetInMillions":94,"boxOfficeRevenueInMillions":926,"academyAwardNominations":6,"academyAwardWins":2,"rottenTomatoesScore":96}],"total":1,"limit":1000,"offset":0,"page":1,"pages":1}
        self.query.filter_match('name', 'The Two Towers')
        actual = json.loads(self.client.movie.get_all(self.query))
        self.query.reset()
        self.assertEqual(expected, actual, 'Incorrect record returned.')

    def test_get_all_quotes(self):
        expected = 9
        self.query.paginate(page=2)
        actual = len(json.loads(self.client.movie.get_all_quotes('5cd95395de30eff6ebccde5b', self.query))['docs'])
        self.query.reset()
        self.assertEqual(expected, actual, 'Incorrect number of records returned.')

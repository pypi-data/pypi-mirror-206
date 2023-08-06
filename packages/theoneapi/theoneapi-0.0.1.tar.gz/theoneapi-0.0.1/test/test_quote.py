import unittest
import json

from theoneapi.client import Client
from theoneapi.query import Query


class TestQuote(unittest.TestCase):
    def setUp(self):
        self.client = Client('ACCESS_TOKEN')
        self.query = Query()

    def test_get_one(self):
        expected = {"docs":[{"_id":"5cd96e05de30eff6ebcce92e","dialog":"Theoden's betrayed me! ABANDON YOUR POSTS! FLEE! FLEE FOR YOUR LIVES!","movie":"5cd95395de30eff6ebccde5d","character":"5cd99d4bde30eff6ebccfca1","id":"5cd96e05de30eff6ebcce92e"}],"total":1,"limit":1000,"offset":0,"page":1,"pages":1}
        actual = json.loads(self.client.quote.get_one('5cd96e05de30eff6ebcce92e'))
        self.assertEqual(expected, actual, 'Incorrect record returned.')

    def test_get_all(self):
        expected = 1000
        actual = len(json.loads(self.client.quote.get_all())['docs'])
        self.assertEqual(expected, actual, 'Incorrect number of records returned.')

    def test_get_all_limit(self):
        expected = 3
        self.query.paginate(limit=3)
        actual = len(json.loads(self.client.quote.get_all(self.query))['docs'])
        self.query.reset()
        self.assertEqual(expected, actual, 'Incorrect number of records returned.')

    def test_get_all_match(self):
        expected = 872
        self.query.filter_match('movie', '5cd95395de30eff6ebccde5d')
        actual = len(json.loads(self.client.quote.get_all(self.query))['docs'])
        self.query.reset()
        self.assertEqual(expected, actual, 'Incorrect record returned.')

    def test_get_all_from_movie(self):
        expected = 9
        self.query.paginate(page=2)
        actual = len(json.loads(self.client.quote.get_all_from_movie('5cd95395de30eff6ebccde5b', self.query))['docs'])
        self.query.reset()
        self.assertEqual(expected, actual, 'Incorrect number of records returned.')

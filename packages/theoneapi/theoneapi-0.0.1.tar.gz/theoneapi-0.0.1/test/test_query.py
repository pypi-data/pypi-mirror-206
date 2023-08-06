import unittest

from theoneapi.query import Query


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.query = Query()

    def test_paginate(self):
        expected = 'limit=3&page=1&offset=2'
        actual = self.query.paginate(offset=2, limit=3, page=1).get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_sort_asc(self):
        expected = 'sort=name:asc'
        actual = self.query.sort_asc('name').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_sort_desc(self):
        expected = 'sort=character:desc'
        actual = self.query.sort_desc('character').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_match(self):
        expected = 'name=The Two Towers'
        actual = self.query.filter_match('name', 'The Two Towers').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_not_match(self):
        expected = 'name!=Frodo'
        actual = self.query.filter_not_match('name', 'Frodo').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_include_string(self):
        expected = 'race=Hobbit,Human'
        actual = self.query.filter_include('race', 'Hobbit,Human').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_include_list(self):
        expected = 'race=Hobbit,Human'
        actual = self.query.filter_include('race', ['Hobbit', 'Human']).get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_exclude_string(self):
        expected = 'race!=Orc,Goblin'
        actual = self.query.filter_exclude('race', 'Orc,Goblin').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_exclude_list(self):
        expected = 'race!=Orc,Goblin'
        actual = self.query.filter_exclude('race', ['Orc', 'Goblin']).get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_exists(self):
        expected = 'name'
        actual = self.query.filter_exists('name').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_not_exists(self):
        expected = '!name'
        actual = self.query.filter_not_exists('name').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_regex(self):
        expected = 'name=/foot/i'
        actual = self.query.filter_regex('name', '/foot/i').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_not_regex(self):
        expected = 'name!=/foot/i'
        actual = self.query.filter_not_regex('name', '/foot/i').get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_less_than(self):
        expected = 'budgetInMillions<100'
        actual = self.query.filter_less_than('budgetInMillions', 100).get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_lt(self):
        expected = 'budgetInMillions<100'
        actual = self.query.filter_lt('budgetInMillions', 100).get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_greater_than(self):
        expected = 'academyAwardWins>0'
        actual = self.query.filter_greater_than('academyAwardWins', 0).get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_gt(self):
        expected = 'academyAwardWins>0'
        actual = self.query.filter_gt('academyAwardWins', 0).get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_greater_than_equal_to(self):
        expected = 'runtimeInMinutes>=160'
        actual = self.query.filter_greater_than_equal_to('runtimeInMinutes', 160).get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_filter_gte(self):
        expected = 'runtimeInMinutes>=160'
        actual = self.query.filter_gte('runtimeInMinutes', 160).get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

    def test_chained_filters(self):
        expected = 'budgetInMillions<100&academyAwardWins>0&runtimeInMinutes>=160'
        actual = self.query.\
            filter_lt('budgetInMillions', 100).\
            filter_gt('academyAwardWins', 0).\
            filter_gte('runtimeInMinutes', 160).\
            get_query_string()
        self.assertEqual(expected, actual, 'Incorrect query string returned.')

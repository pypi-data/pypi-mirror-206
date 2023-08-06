import requests

from theoneapi.query import Query
from theoneapi.entity.movie import Movie
from theoneapi.entity.quote import Quote


class Client():
    def __init__(self, access_token):
        self._access_token = access_token
        self._base_url = 'https://the-one-api.dev/v2'
        self._movie = None
        self._quote = None

    def request(self, method, path, query=None):
        headers = {'Authorization': f'Bearer {self._access_token}'}
        url = f'{self._base_url}/{path}'

        if type(query) == Query:
            qs = query.get_query_string()
            if len(qs):
                url += f'?{qs}'
            query.reset()

        if method == 'get':
            response = requests.get(url, headers=headers)
        else:
            raise ValueError(f'Invalid http method "{method}" provided.')

        if response.status_code != requests.codes.ok:
            raise ValueError('Invalid request. Please check your input.')

        return response.text

    @property
    def movie(self):
        if self._movie is None:
            self._movie = Movie(self)
        return self._movie

    @property
    def quote(self):
        if self._quote is None:
            self._quote = Quote(self)
        return self._quote

from theoneapi.entity import Entity


class Quote(Entity):
    def __init__(self, client):
        super().__init__(client, 'quote')

    def get_all_from_movie(self, movie_id, query=None):
        path = f'movie/{movie_id}/{self._name}'
        return self._client.request('get', path, query)

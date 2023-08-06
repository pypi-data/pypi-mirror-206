from theoneapi.entity import Entity


class Movie(Entity):
    def __init__(self, client):
        super().__init__(client, 'movie')

    def get_all_quotes(self, id, query=None):
        path = f'{self._name}/{id}/quote'
        return self._client.request('get', path, query)

class Entity():
    def __init__(
            self,
            client,
            name,
    ):
        self._client = client
        self._name = name

    def get_one(self, id):
        path = f'{self._name}/{id}'
        return self._client.request('get', path)

    def get_all(self, query=None):
        path = self._name
        return self._client.request('get', path, query)

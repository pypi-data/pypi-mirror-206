class Query():
    def __init__(self):
        self._reserved_keys = ['limit', 'page', 'offset', 'sort']
        self._params = None

    def _add_param(self, key, value=None):
        if self._params is None:
            self._params = {}
        self._params[key] = value

    def _validate_reserved_key(self, key):
        if key in self._reserved_keys:
            raise ValueError(f'Reserved keyword "{key}" provided.')

    def reset(self):
        self._params = None

    def get_params(self):
        return self._params

    def get_query_string(self):
        if self._params is None:
            return ''
        params = []
        for key, val in self._params.items():
            params.append(key if val is None else f'{key}={val}')
        return '&'.join(params)

    def paginate(self, limit=None, page=None, offset=None):
        if limit is not None:
            self._add_param('limit', limit)
        if page is not None:
            self._add_param('page', page)
        if offset is not None:
            self._add_param('offset', offset)
        return self

    def sort_asc(self, field):
        self._add_param('sort', f'{field}:asc')
        return self

    def sort_desc(self, field):
        self._add_param('sort', f'{field}:desc')
        return self

    def filter_match(self, field, value):
        self._validate_reserved_key(field)
        self._add_param(field, value)
        return self

    def filter_not_match(self, field, value):
        self._validate_reserved_key(field)
        self._add_param(f'{field}!', value)
        return self

    def filter_include(self, field, value):
        self._validate_reserved_key(field)
        if type(value) == list:
            value = ','.join(value)
        self._add_param(field, value)
        return self

    def filter_exclude(self, field, value):
        self._validate_reserved_key(field)
        if type(value) == list:
            value = ','.join(value)
        self._add_param(f'{field}!', value)
        return self

    def filter_exists(self, field):
        self._validate_reserved_key(field)
        self._add_param(field)
        return self

    def filter_not_exists(self, field):
        self._validate_reserved_key(field)
        self._add_param(f'!{field}')
        return self

    def filter_regex(self, field, value):
        self._validate_reserved_key(field)
        self._add_param(field, value)
        return self

    def filter_not_regex(self, field, value):
        self._validate_reserved_key(field)
        self._add_param(f'{field}!', value)
        return self

    def filter_less_than(self, a, b):
        self._validate_reserved_key(a)
        self._add_param(f'{a}<{b}')
        return self

    def filter_lt(self, a, b):
        return self.filter_less_than(a, b)

    def filter_greater_than(self, a, b):
        self._validate_reserved_key(a)
        self._add_param(f'{a}>{b}')
        return self

    def filter_gt(self, a, b):
        return self.filter_greater_than(a, b)

    def filter_greater_than_equal_to(self, a, b):
        self._validate_reserved_key(a)
        self._add_param(f'{a}>={b}')
        return self

    def filter_gte(self, a, b):
        return self.filter_greater_than_equal_to(a, b)

# raffy_kaloustian-SDK

This SDK provides (partial) access to [LibLab](https://liblab.com/)'s Lord of the Rings API - [The One API to rule them all](https://the-one-api.dev).

## Supported Python Version

This SDK supports Python 3.9 or higher.

## Installation

Install using pip from PyPi.

```shell
pip3 install theoneapi
```

## Example Usage

See examples.py.

```python
from theoneapi.client import Client
from theoneapi.query import Query

# sign up to get an access token: https://the-one-api.dev
client = Client('ACCESS_TOKEN')


'''
Movie Examples
'''

# get one movie (by id)
movie = client.movie.get_one('5cd95395de30eff6ebccde56')

# get all movies
movies = client.movie.get_all()

# get all movie quotes (by movie id)
# (see below for another way to get this as well)
movie_quotes_1 = client.movie.get_all_quotes('5cd95395de30eff6ebccde5b')


''' 
Quote Examples
'''

# get one quote (by id)
quote = client.quote.get_one('5cd96e05de30eff6ebcce92e')

# get all quotes
quotes = client.quote.get_all()

# get all movie quotes (by movie id)
# (see above for another way to get this as well)
movie_quotes_2 = client.quote.get_all_from_movie('5cd95395de30eff6ebccde5b')


'''
Query Option Examples
'''

query = Query()

# get paginated quotes
quotes_paginated = client.quote.get_all(
    query.paginate(offset=2, limit=3, page=1)
)

# get movies sorted ascending
movies_sorted = client.movie.get_all(
    query.sort_asc('name')
)

# get movies sorted ascending
movie_matched_name = client.movie.get_all(
    query.filter_match('name', 'The Two Towers')
)

# chaining query options
quotes_chained_query = client.quote.get_all(
    query.filter_match('movie', '5cd95395de30eff6ebccde5b').paginate(limit=5)
)
```

## Query Options

```python
from theoneapi.query import Query


query = Query()

# pagination
query.paginate(limit=limit, page=page, offset=offset)

# sorting
query.sort_asc(field)
query.sort_desc(field)

# filtering
query.filter_match(field, value)
query.filter_not_match(field, value)
query.filter_include(field, value)
query.filter_exclude(field, value)
query.filter_exists(field)
query.filter_not_exists(field)
query.filter_regex(field, value)
query.filter_not_regex(field, value)
query.filter_less_than(a, b)
query.filter_lt(a, b) # same as query.filter_less_than(a, b)
query.filter_greater_than(a, b)
query.filter_gt(a, b) # same as query.filter_greater_than(a, b)
query.filter_greater_than_equal_to(a, b)
query.filter_gte(a, b) # same as query.filter_greater_than_equal_to(a, b)
```
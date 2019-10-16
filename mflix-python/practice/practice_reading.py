from bson.json_util import dumps
from pymongo import MongoClient


if __name__ == "__main__":
    uri = 'mongodb+srv://m220student:m220password@mflix-vzr6e.mongodb.net/sample_mflix?retryWrites=true&w=majority'
    client = MongoClient(uri)
    mflix = client.sample_mflix

    movies = mflix.movies
    jp = movies.find({'cast': 'Joaquin Phoenix'}, {'_id': 0, 'title': 1, 'year': 1})
    print(dumps(jp, indent=2))


from pymongo import MongoClient
from pprint import pprint

# Set up database connection
uri = 'mongodb://admin:letmein@localhost:32768/?AuthSource=admin'
client = MongoClient(uri)
my_db = client["Netflix"]
rating_collection = my_db['Rating']

# Query 1: All documents in a collection in json format
# print('All documents in collection')
# for document in rating_collection.find():
#     pprint(document)

# Query 2: Embedded array data based on criteria
# print('Print embedded erray with condition')
# age_rating = input('Enter an age rating: ')
# criteria = input('Only show media released after this year: ')
# document = rating_collection.find_one({'Age_Rating': age_rating})
# for media in document['Media']:
#     if media['release_year'] >= int(criteria):
#         print(media)

# Query 3: Projection
# print('Projection')
# for doc in rating_collection.find({}, {'Age_Rating': 1, '_id': 0}):
#     print(doc)

# Query 4: Sorted output
# print('Sorted output')
# age_rating = input('Choose an age rating to sort by release year: ')
# document = rating_collection.find_one({'Age_Rating': age_rating})
# document['Media'].sort(key=lambda x: x['release_year'])
# for media in document['Media']:
#     print(media['title'], media['release_year'])

# Query 5: Aggregation Pipeline
# print('Aggregation Pipeline')
# pipeline = [
#     {"$unwind": "$Media"},
#     {"$group": {"_id": "$Media.release_year", "count": {"$sum": 1}}},
#     {"$sort":  {"count": -1}},
# ]
# pprint(list(rating_collection.aggregate(pipeline)))

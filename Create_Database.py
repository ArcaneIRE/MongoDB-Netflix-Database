import pandas as pd
import json
from pymongo import MongoClient
from pprint import pprint

# Clean data
df = pd.read_csv('./netflix_ratings.csv', encoding='latin-1')
# Replace spaces in column names
df.columns = list(map(lambda x: x.replace(" ", "_"), df.columns))
df = df.drop(columns=['user_rating_size'])
df = df.rename(columns={'rating': 'age_rating',
                        'rating_level': 'age_rating_description',
                        'rating_description': 'age_rating_score'})
# Fix datatypes
df['title'] = df['title'].astype("string")
df['age_rating'] = df['age_rating'].astype("string")
df['age_rating_description'] = df['age_rating_description'].astype(
    "string")
df = df.replace('NA', '')
df['user_rating_score'] = df['user_rating_score'].astype("float")

# Set up database connection
uri = 'mongodb://admin:letmein@localhost:32768/?AuthSource=admin'
client = MongoClient(uri)
my_db = client["Netflix"]
# Set up collection
validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['Age_Rating', 'Media'],
        'properties': {
            'Age_Rating': {
                'bsonType': 'string',
                'description': 'Required. Must be a string',
            },
            'Media': {
                'bsonType': 'array',
                'items': {
                    'bsonType': 'object',
                    'required': ['title'],
                    'properties': {
                        'title': {'bsonType': 'string'},
                        'age_rating_description': {'bsonType': ['string', 'null'], 'minimum': 0},
                        'age_rating_score': {'bsonType': 'int', 'minimum': 0},
                        'release_year': {'bsonType': 'int', 'minimum': 1500},
                        'user_rating_score': {'bsonType': 'double'},
                    }
                }
            }
        }
    }
}
my_db['Rating'].drop()
rating_collection = my_db.create_collection('Rating')
my_db.command({
    "collMod": "Rating",
    "validator": validator,
    "validationLevel": "moderate",
})

rating_df = df[['age_rating']].drop_duplicates()
for row in rating_df.itertuples():
    media = df[df.age_rating ==
               row.age_rating][['title', 'age_rating_description', 'age_rating_score', 'release_year', 'user_rating_score']]
    entries = json.dumps({'Age_Rating': row.age_rating,
                          'Media': media.to_dict('records')})
    rating_collection.insert_one(json.loads(entries))

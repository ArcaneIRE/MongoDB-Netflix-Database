from pymongo import MongoClient
from pprint import pprint

# Set up database connection
uri = 'mongodb://admin:letmein@localhost:32768/?AuthSource=admin'
client = MongoClient(uri)
my_db = client["Netflix"]
rating_collection = my_db['Rating']

# Insert Statement
# print('Insert Movie/Series into Category')
# age_rating = input('Enter the age rating category of this media: ')
# age_categories = []
# for document in rating_collection.find():
#     age_categories.append(document['Age_Rating'])
# if age_rating not in age_categories:
#     raise Exception('Age category does not exist')
# title = input('Enter the title of this media: ')
# age_rating_description = input(
#     'Enter the age rating description of this media: ')
# age_rating_score = int(input('Enter the age rating score of this media: '))
# release_year = int(input('Enter the release year of this media: '))
# user_rating_score = float(input('Enter the user rating score of this media: '))
# rating_collection.update_one(
#     {"Age_Rating": age_rating},
#     {"$push":
#      {"Media":
#       {
#           "title": title,
#           "age_rating_description": age_rating_description,
#           "age_rating_score": age_rating_score,
#           "release_year": release_year,
#           "user_rating_score": user_rating_score,
#       }
#       }
#      }
# )
# print('Success! Item Added')

# Update Statement
# print('Update Movie/Series Title')
# old_title = input('Enter the title of the media you wish to update: ')
# new_title = input('Enter the new title: ')
# for document in rating_collection.find():
#     for media in document['Media']:
#         if media['title'] == old_title:
#             update_document = (
#                 {"$set":
#                  {"Media.$.title": new_title}
#                  }
#             )
#             rating_collection.update_one(
#                 {"Media.title": old_title}, update_document)
#             print('Success! Item Updated')
# for document in rating_collection.find():
#     for media in document['Media']:
#         if media['title'] == new_title:
#             print('yep worked')

# Delete Statement
# title_to_delete = input('Enter a media title to delete: ')
# rating_collection.update_one(
#     {},
#     {"$pull":
#      {"Media":
#       {
#           "title": title_to_delete,
#       }
#       }
#      }
# )

# is_deleted = True
# for document in rating_collection.find():
#     for media in document['Media']:
#         if media['title'] == 'old people':
#             is_deleted = False
#             print('Error! Delete failed')
# if is_deleted:
#     print("Success! Item deleted")

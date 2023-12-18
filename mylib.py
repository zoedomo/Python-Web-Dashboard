# python lib code ....
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host, port, db, col):
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31499
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.collection.insert_one(data)  # data should be a dictionary
            return result.inserted_id  # Return the inserted ID or any other relevant information
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            cursor = self.collection.find(query)
            result_list = list(cursor)
            return result_list
        else:
            raise Exception("Query parameter cannot be None")
            
     # Create method to implemnt the U in CRUD
    def update(self, query, update_data):
        if query is not None:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        else:
            raise Exception("Query parameter cannot be None")
            
    # Create method to implemnt the D in CRUD
    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Query parameter cannot be None")

# Example usage:
if __name__ == "__main__":
    # Instantiate the AnimalShelter class
    animal_shelter = AnimalShelter()

    # Example: Create a document
    document_to_insert = {"name": "Fluffy", "type": "Cat", "age": 3}
    animal_shelter.create(document_to_insert)

    # Example: Read documents
    query_criteria = {"type": "Cat"}
    query_result = animal_shelter.read(query_criteria)
    print(f"Query Result: {query_result}")
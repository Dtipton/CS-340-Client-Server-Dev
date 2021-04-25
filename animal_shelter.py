
from pymongo import MongoClient
from bson.objectid import ObjectId
import json


# Our class definition that our script will call
class AnimalShelter(object):
    def __init__(self, username, password):
        # This initializes mongoclient to access the db.
        self.client = MongoClient('mongodb://%s:%s@localhost:45300/test?authSource=AAC'%(username, password))
        self.database = self.client['AAC']

    # Our C method.  Returns true/false as necessary.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    # Our R method.  Read based on any given parameter, returns the
    # data, or returns everything if no criteria is given
    def read(self, param):
        if param is not None:
            data = self.database.animals.find(param)
        else:
            data = self.database.animals.find({})
        return data

    # Our U method it updates records in the Animal Database	
    def update(self, query, record):

        #Check that the record exist
        if record is not None:
            # Updates the records and prints out the number updated.
            update_result = self.database.animals.update_many(query, record)
            result= "Documents updated: " + json.dumps(update_result.modified_count)
            return result

        else:
            raise Exception("Record not found")

     #Our D method it deletes records from the database.
    def delete(self, data):

        #Check that the record is in the database
        if data is not None:
            # delete the documents matching data criteria and print no. of documents deleted
            delete_result = self.database.animals.delete_many(data)
            result = "Documents deleted: "+ json.dumps(delete_result.deleted_count)
            return result

        else:
            raise Exception("No record provided.")
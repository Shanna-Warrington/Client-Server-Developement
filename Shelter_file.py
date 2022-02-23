from pymongo import MongoClient

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username=None, password=None):
        # Allows access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:37554' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:37554')
        self.database = self.client['AAC']

    def create(self, data):
        if data is not None:   # If there is any data
            self.database.animals.insert(data)
        else:  # If there is no data
            raise Exception("Nothing to save because data parameter is empty")

            
    def read(self, data):
        # If search is not none then this will return all the entries matching the criteria
        if data is not None:
            self.database.animals.find(data,{"_id":False})  # finds matching criteria
        else:
            self.database.animals.find({}, {'_id':False})  # no matching criteria, returns all entries
            
    
    def update(self, data, newData):
        #If data is not none, then it will update the data with new data
        if data is not None:
            self.database.animals.update_one(data, newData)
            return newData
        else:
        #Raises an exception if there is no data to update
            raise Exception('Nothing to update because data parameter is empty')
            
   
    def delete(self, remove):
        #If data is not empty it will delete it.
        if remove is not None:
            self.database.animals.delete_many(remove)
            return 'Document removed'
        else:
            raise Exception('Nothing to delete because data parameter is empty')
            
            
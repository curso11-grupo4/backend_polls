import json
import pymongo
import certifi
from typing import Generic, TypeVar, get_args

from bson import ObjectId

T = TypeVar('T')


class InterfaceRepository(Generic[T]):

    def __init__(self):
        # connection database
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(
            data_config.get("db-connection"),
            tlsCAFile=ca
        )
        self.data_base = client[data_config("db-name")]
        # collection name
        model_class = get_args(self.__orig_bases__[0])
        self.collection = model_class[0].__name__.lower()

    def load_file_config(self):
        with open("config.json", 'r') as config_file:
            data = json.load(config_file)
        return data

    def find_all(self) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find():
            document['_id'] = document['_id'].__str__()
            document = self.transform_obj_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def find_by_id(self, id_: str) -> T:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        # Document is not found, document = None
        document = current_collection.find_one({'_id': _id})
        document = self.get_values_db_ref(document)
        if document:
            document['_id'] = document['_id'].__str__()
        else:
            # document not found
            document = {}
        return document

    def save(self, item: T) -> dict:
        current_collection = self.data_base[self.collection]
        item = self.transform_refs(item)
        if hasattr(item, '_id') and item._id != "":
            # update
            id_ = item._id
            _id = ObjectId(id_)
            delattr(item, '_id')
            item_dict = item.__dict__
            update_item = {"$set", item_dict}
            current_collection.update_one({'_id': _id}, update_item)
        else:
            # insert
            _id = current_collection.insert_one(item.__dict__)
            id_ = _id.inserted_id.__str__()
        return self.find_by_id(id_)

    # TODO Verificar el tipo de dato a retornar
    def update(self, id_: str, item: T) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        item_dict = item.__dict__
        updated_item = {"$set": item_dict}
        result = current_collection.update_one({'_id': _id}, updated_item)
        return {"update_count": result.matched_count}


    def delete(self, id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        result = current_collection.delete_one({'_id': _id})
        return {"delete_count": result.deleted_count}

    def query(self, query: dict) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find(query):
            document['_id'] = document['_id'].__str__()
            document = self.transform_obj_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def query_aggregation(self, query: dict) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.aggregate(query):
            document['_id'] = document['_id'].__str__()
            document = self.transform_obj_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    # Sprint1
    def get_values_db_ref(self, document) -> T:
        pass

    def get_values_db_ref_from(self, document) -> list:
        pass

    def transform_obj_ids(self):
        pass

    def format_list(self):
        pass

    def transform_refs(self):
        pass

    def object_to_db_ref(self):
        pass



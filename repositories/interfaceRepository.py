import json
import pymongo
import certifi
from typing import Generic, TypeVar, get_args

from bson import ObjectId, DBRef

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
        self.data_base = client[data_config.get("db-name")]
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
        for key in document.keys():
            value = document.get(key)
            if isinstance(value, DBRef):
                collection_ref = self.data_base[value.collection]
                _id = ObjectId(value.id)
                document_ref = collection_ref.find_one({'_id': _id})
                document_ref['_id'] = document_ref['_id'].__str__()
                document[key] = document_ref
                document[key] = self.get_values_db_ref(document[key])
            elif isinstance(value, list) and len(list) > 0:
                document[key] = self.get_values_db_ref_from_list(value)
            elif isinstance(value, dict):
                document[key] = self.get_values_db_ref(value)
        return document

    def get_values_db_ref_from_list(self, list_: list) -> list:
        processed_list = []
        collection_ref = self.data_base[list_[0]._id.collection]
        for item in list:
            _id = ObjectId(item._id)
            document_ref =  collection_ref.find_one({'_id': _id})
            document_ref['_id'] = document_ref['_id'].__str__()
            processed_list.append(document_ref)
        return processed_list

    def transform_obj_ids(self, document: dict) -> dict:
        for key in document.key():
            value = document.get(key)
            if isinstance(value, ObjectId):
                document[key] = document[key].__str__()
            elif isinstance(value, list) and len(list) > 0:
                document[key] = self.format_list(value)
            elif isinstance(value, dict):
                document[key] = self.transform_obj_ids(value)
        return document

    def format_list(self, list_: list) -> list:
        processed_list = []
        for item in list_:
            if isinstance(item, ObjectId):
                temp = item.__str__()
                processed_list.append(temp)
        if len(processed_list) == 0:
            processed_list = list_
        return processed_list

    def transform_refs(self, item: T) -> T:
        item_dict = item.__dict__
        for key in item_dict.keys():
            if item_dict.get(key).__str__().count("object") == 1:
                object_ = self.object_to_db_ref(getattr(item, key))
                setattr(item, key, object_)
        return item

    def object_to_db_ref(self, object_ref) -> DBRef:
        collection_ref = object_ref.__class__.__name__.lower()
        return DBRef(collection_ref, ObjectId(object_ref._id))


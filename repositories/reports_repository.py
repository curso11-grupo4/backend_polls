
from repositories.interfaceRepository import InterfaceRepository
from models.vote import Vote


class ReportsRepository(InterfaceRepository[Vote]):

    def get_votes_by_table(self):
        query_group = {
            "$group": {
                "_id": "$table",
                "count": {"$sum": 1}
            }
        }
        query_lookup = {
            "$lookup": {
                "from": "table",
                "localField": "_id.$id",
                "foreignField": "_id",
                "as": "details"
            }
        }
        query_unwind = {
            "$unwind": "$details"
        }
        query_add_fields = {
            "$addFields": {
                    "number_of_personal_ids": "$details.number_personal_ids",
                    "table_number": "$details.table_number",
                    "_id": "$details._id"
            }
        }
        query_project = {
            "$project": {
                "number_of_personal_ids": 1,
                "table_number": 1,
                "count": 1
            }

        }
        pipeline = [query_group, query_lookup, query_unwind, query_add_fields, query_project]
        return self.query_aggregation(pipeline)

    def get_votes_by_candidate(self):
        query_group = {
            "$group": {
                "_id": "$candidate",
                "count": {"$sum": 1}
            }
        }
        query_lookup = {
            "$lookup": {
                "from": "candidate",
                "localField": "_id.$id",
                "foreignField": "_id",
                "as": "details"
            }
        }

        query_unwind = {
            "$unwind": "$details"
        }
        query_add_fields = {
            "$addFields": {
                "name": "$details.name",
                "lastname": "$details.lastname",
                "_id": "$details._id",
            }
        }
        query_project = {
            "$project": {
                "name": 1,
                "lastname": 1,
                "count": 1
            }

        }
        pipeline = [query_group, query_lookup, query_unwind, query_add_fields, query_project]
        return self.query_aggregation(pipeline)

    def get_votes_by_party(self):
        query_group = {
            "$group": {
                "_id": "$table",
                "count": {"$sum": 1}
            }
        }
        query_lookup = {
            "$lookup": {
                "from": "table",
                "localField": "_id.$id",
                "foreignField": "_id",
                "as": "details"
            }
        }
        query_lookup1 = {
            "$lookup": {
                "from": "party",
                "localField": "party.$id",
                "foreignField": "party",
                "as": "details"
            }
        }
        query_unwind = {
            "$unwind": "$details"
        }
        query_add_fields = {
            "$addFields": {
                "number_of_personal_ids": "$details.number_personal_ids",
                "table_number": "$details.table_number",
                "_id": "$details._id"
            }
        }
        query_project = {
            "$project": {
                "number_of_personal_ids": 1,
                "table_number": 1,
                "count": 1
            }

        }
        pipeline = [query_group, query_lookup, query_lookup1, query_unwind, query_add_fields, query_project]
        return self.query_aggregation(pipeline)

    def distribution_by_parties(self):
        pass


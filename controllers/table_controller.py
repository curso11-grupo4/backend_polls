from models.table import Table
from repositories.table_repository import TableRepository


class TableController:

    def __init__(self):
        print("Table controller ready...")
        self.table_repository = TableRepository()

    def index(self) -> list:
        """
        Get all tables with the number of them and amount of "cedula" on each table
        :return:
        """
        print("Get all tables")
        return self.table_repository.find_all()

    def show(self, table_number_: str):
        """
        Get one specific table knowing the number of it
        :param table_number_:
        :return:
        """
        print("Get table")
        return self.table_repository.find_by_id(table_number_)

    def create(self, table_: dict) -> dict:
        """
        Insert a new table
        :param table_: a dictionary carries the number of the table and amount of "cedula" on it
        :return:
        """
        print("Insert table")
        table = Table(table_)
        return self.table_repository.save(table)

    def update(self, table_number_: str, table_: dict) -> dict:
        """
        Update a specific table
        :param table_number_: number of the table
        :param table_:
        :return:
        """
        print("Update tables")
        table = Table(table_)
        return self.table_repository.update(table_number_, table)

    def delete(self, table_number_: str) -> dict:
        """
        Delete a specific table
        :param table_number_: number of the table
        :return:
        """
        print("Delete table " + table_number_)
        return self.table_repository.delete(table_number_)

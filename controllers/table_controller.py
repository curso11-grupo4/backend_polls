

class TableController:

    def __init__(self):
        print("Table controller ready...")

    def index(self) -> list:
        """
        Get all tables with the number of them and amount of "cedula" on each table
        :return:
        """
        print("Get all tables")

    def show(self, table_number: str) -> dict:
        """
        Get one specific table knowing the number of it
        :param table_number:
        :return:
        """
        print("Get table")

    def create(self, table: dict) -> dict:
        """
        Insert a new table
        :param table: a dictionary carries the number of the table and amount of "cedula" on it
        :return:
        """
        print("Insert table")

    def update(self, table_number: str, table: dict) -> dict:
        """
        Update a specific table
        :param table_number: number of the table
        :param table:
        :return:
        """
        print("Update tables")

    def delete(self, table_number: str) -> dict:
        """
        Delete a specific table
        :param table_number: number of the table
        :return:
        """
        print("Delete table")

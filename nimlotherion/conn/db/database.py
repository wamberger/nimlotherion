

__all__ = ['Database', 'DatabaseHolder']


from typing import Mapping
from nimlotherion.conn.db.layers import Add
from nimlotherion.conn.db.layers import Query
from nimlotherion.conn.db.layers import Update
from nimlotherion.conn.db.layers import Delete
from nimlotherion.utils.crypto import CryptoSafe


class Database(Add, Query, Update, Delete):
    """
    Represents a database connection and execution interface.

    This class inherits from :class:`DAO` (Data Access Object) and encapsulates
    the main methods for connecting to a database and executing database
    processes. It serves as an interface for interacting with the underlying
    database system. Users can use this class to establish connections to
    databases, execute queries, and perform database operations.

    The class provides essential functionality for managing database
    interactions, including methods for executing SQL queries, managing
    transactions, and handling database connections.

    Attributes:
        Inherits attributes from the :class:`DAO` class.
    """

    def __init__(self, conn: str) -> None:
        """
        Args:
            conn (str): Can be any, depends on the ORM.
        """
        self._conn: CryptoSafe = CryptoSafe(bytes(conn, 'utf-8'))
        super().__init__(conn)

    @property
    def conn(self) -> str:
        return self._conn.decrypt().decode('utf-8')


class DatabaseHolder:
    """A holder for multiple :class:`DatabaseManager` objects."""

    def __init__(self, creds: Mapping[str, str] = None) -> None:

        self.databases: dict[str, Database] = {}

        if creds:
            self.load_databases(creds)

    def add_database(self, db_name: str, conn: str) -> None:
        self.databases[db_name] = Database(conn)

    def load_databases(self, creds: Mapping[str, str]) -> None:
        """
        Load database configurations and
        create :class:`DatabaseManager` objects.

        This function initializes :class:`DatabaseManager` objects using the
        provided credentials from configurations as arguments.

        Args:
            creds (Mapping[str, str]): A dictionary containing database
                                   configuration information. The keys
                                   should correspond to database names,
                                   and the values should be connection
                                   strings for SQLAlchemy :class:`Engine`.
        """
        for db_name, conn in creds.items():
            if not conn:
                continue
            else:
                self.add_database(db_name, conn)

    def get_database(self, db_name: str) -> Database | None:
        """Retrieve a specific :class:`DatabaseManager` object
        corresponding to the provided database name.

        Args:
            db_name (str): The name of the database to retrieve.

        Returns:
            Database: The :class:`DatabaseManager` object
                      corresponding to the provided name
                      or None if does not exist.
        Raises:
            AttributeError: If the specified database name does not exist.
        """
        return self.databases.get(db_name, None)

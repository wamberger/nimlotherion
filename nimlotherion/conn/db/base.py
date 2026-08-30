

__all__ = ['Base']


from sqlalchemy import text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.engine import create_engine
from sqlalchemy.exc import SQLAlchemyError


class Base:
    """Base layer for the database processes"""

    def __init__(self, conn: str) -> None:
        try:
            self.engine: Engine = create_engine(
                conn, pool_pre_ping=True)
            self.session_factory: sessionmaker = sessionmaker(
                bind=self.engine)
            self.session: scoped_session = scoped_session(
                self.session_factory)
        except SQLAlchemyError as e:
            raise SQLAlchemyError(
                f'Cannot conn with database and create session: {e}') from e

    def ping_db(self) -> None:
        """Check database connection.

        Raises:
            DatabaseConnectionError: If cannot communicate with the database.
        """
        try:
            match self.engine.dialect.dialect_description:
                case 'oracle+oracledb':
                    with self.engine.connect() as connection:
                        connection.execute(text('SELECT 1 FROM DUAL'))
                case 'mssql+pyodbc':
                    with self.engine.connect() as connection:
                        connection.execute(text('SELECT @@VERSION'))
                case _:
                    with self.engine.connect() as connection:
                        connection.execute(text('SELECT 1'))
        except SQLAlchemyError as e:
            raise SQLAlchemyError(e) from e

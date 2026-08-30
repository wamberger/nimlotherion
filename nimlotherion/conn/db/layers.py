

__all__ = [
    'Add',
    'Query',
    'Update',
    'Delete'
    ]


from typing import Mapping
from typing import TypeVar
from typing import Any
from typing import Sequence

from sqlalchemy import select
from sqlalchemy import Sequence as Seq
from sqlalchemy.engine.row import Row
from sqlalchemy.engine.row import RowMapping
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import SQLAlchemyError

from nimlotherion.conn.db.query import QueryConstructor
from nimlotherion.conn.db.base import Base


type P_key = str | int | float
type _RowData = Row[Any] | RowMapping | Any

R = TypeVar("R", bound=_RowData)
M = TypeVar('M', bound=declarative_base)


class Add(Base):
    def insert(self, ins_obj: M) -> None:
        """
                Inserts a new record into the database
                if it doesn't already exist based on the primary key.

                Args:
                    model (_M): The SQLAlchemy model class.
                    ins_obj (_M): The object with record data
                                                      created from the SQLAlchemy
                                                      model class.
                    p_key (P): The primary key value for the record.

                Returns:
                    Tuple[bool, Union[Model, str]]:
                        - A tuple containing:
                            - True: If the record is inserted successfully.
                            - The inserted object (model instance).
                        - A tuple containing:
                            - False: If a record with the same
                                     primary key already exists.
                            - A string message indicating that
                              the record already exists.

                Raises:
                    DatabaseInsertError: If there is an error
                                                with the database insert.
        """
        try:
            self.session.add(ins_obj)
            self.session.commit()
            self.session.expunge_all()
            self.session.close()
        except SQLAlchemyError as e:
            self.session.rollback()
            self.session.close()
            raise SQLAlchemyError(e) from e

    def insert_with_seq(
            self, ins_obj: M, seq_col: str, seq_name: str) -> None:
        """
            Inserts a database record with a sequence-generated primary key.

            Args:
                model (_M): The SQLAlchemy model class.
                ins_obj (_M): The instance of the model to be inserted.
                p_key (P): The primary key value of the record to be checked.
                seq_col (str): The name of the sequence-generated column.
                seq_name (str): The name of the sequence.

            Returns:
                Tuple[bool, Union[_M, str]]: A tuple containing a boolean indicating
                                              whether the operation was successful
                                              and either the inserted object or
                                              a message indicating failure.

            Raises:
                DatabaseInsertError: If there is an error during the database
                                            insertion operation.
        """
        with self.session() as session:
            try:
                seq_nr = session.execute(Seq(seq_name))
                setattr(ins_obj, seq_col, seq_nr)
                session.add(ins_obj)
                session.commit()
                session.expunge_all()
            except SQLAlchemyError as e:
                session.rollback()
                raise SQLAlchemyError(e) from e


class Query[R, M](Base, QueryConstructor):
    def get_all(self, model: M) -> Sequence[R]:
        """Gets all records from the database.

        Args:
            model (_M): The SQLAlchemy model class.

        Returns:
            Optional[List[_M]]: A list containing records
                                from the database as instances
                                of the SQLAlchemy model class,
                                or None.

        Raises:
            DatabaseQueryError: If there is an error
                                       with the database query.
        """
        try:
            return self.session.scalars(select(model)).all()
        except SQLAlchemyError as e:
            raise SQLAlchemyError(e) from e

    def get_by_p_key(self, model: M, p_key: P_key) -> M | None:
        """Retrieves a record by its primary key from the database.

                Args:
                    model (_M): The SQLAlchemy model class.
                    p_key (P): The primary key of the record.

                Returns:
                    Optional[_M]: An instance of the SQLAlchemy
                                  model class representing the
                                  record, or None if no record
                                  is found.
                Raises:
                    DatabaseQueryError: If there is an error
                                               with the database query.
        """
        try:
            return self.session.get(model, p_key)
        except SQLAlchemyError as e:
            raise SQLAlchemyError(e) from e

    def get_by_custom_query(
            self,
            model: M,
            equal: Mapping[str, Any] = None,
            greater_than: Mapping[str, Any] = None,
            less_than: Mapping[str, Any] = None,
            not_equal: Mapping[str, Any] = None,
            greater_than_or_equal_to: Mapping[str, Any] = None,
            less_than_or_equal_to: Mapping[str, Any] = None,
            order_by: Sequence[str] = None) -> Sequence[R]:
        """
        Retrieves records where specified columns in database
        are greater than the provided values.

        Args:
            model (_M): The SQLAlchemy model class.
            columns (Dict[str, T): A dictionary where keys represent column names and
                                     values represent the values from the database.
            order_by (List[str], optional): A list of column names to order the
                                            results by. Default is None.

        Returns:
            Optional[Query]: An instance of the SQLAlchemy model
                                class representing the record, or None
                                if no record is found.

        Raises:
            DatabaseQueryError: If there is an error
                                       with the database query.
        """
        try:
            q = self.crt_custom_query(
                equal,
                greater_than,
                less_than,
                not_equal,
                greater_than_or_equal_to,
                less_than_or_equal_to,
                order_by)
            if not q:
                return []
            else:
                return eval(q)
        except SQLAlchemyError as e:
            raise SQLAlchemyError(e) from e


class Update(Base):

    def update(self) -> None:
        """
                Updates a database record with the provided data
                using primary key.

                Args:
                    model (_M): The SQLAlchemy model class representing
                                the database table.
                    p_key (P): The primary key value of the record to be updated.
                    upd_data (Dict[str, _V]): A dictionary containing the updated
                                              data for the record, where keys are
                                              column names and values are the
                                              updated values.
                Returns:
                    Tuple[bool, Union[_M, str]]: A tuple containing a boolean indicating
                                                 whether the operation was successful
                                                 and either the updated object or an
                                                 error message.
                Raises:
                    DatabaseUpdateError: If there is an error during the
                                                database update operation.
        """
        try:
            self.session.commit()
            self.session.expunge_all()
            self.session.close()
        except SQLAlchemyError as e:
            self.session.rollback()
            self.session.close()
            raise SQLAlchemyError(e) from e


class Delete(Base):

    def delete(self, del_obj: M) -> None:
        """Deletes a database record.
                Args:
                    del_obj (_M): The SQLAlchemy model instance to be deleted.
                Returns:
                    None
                Raises:
                    DatabaseDeleteError: If there is an error during
                                                the database deletion operation
        """
        try:
            self.session.delete(del_obj)
            self.session.commit()
            self.session.expunge_all()
            self.session.close()
        except SQLAlchemyError as e:
            self.session.rollback()
            self.session.close()
            raise SQLAlchemyError(e) from e

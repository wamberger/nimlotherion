

__all__ = ['QueryConstructor']


from typing import Mapping
from typing import Any
from typing import Sequence


class QueryConstructor:
    """
    The class QueryConstructor is designed to
    generate SQLAlchemy query code as a string
    for subsequent execution.
    """

    @staticmethod
    def _crt_param(
            col: Mapping[str, Any] | None, operator: str) -> str | None:
        """
        Constructs a parameterized WHERE clause string for SQLAlchemy queries.

        Args:
            col ([Dict[str, T]]): Columns that will be queried in the database.
                                  Keys represent column names from the database 
                                  and values represent the queried values:
                                  - Column name (str): The name of the 
                                                       database column.
                                  - value (T): The value to be compared
                                                with database value.
            operator (str): The comparison operator, 
                            one of ">", "<", "==", "<=", ">=", "!=".
        Returns:
            str: The constructed WHERE clause string.
        """
        if not col:
            return None
        stmt = ''
        for ind, (k, v) in enumerate(col.items(), 1):
            if isinstance(v, str):
                stmt += f"model"\
                    f".{k} {operator} '{v}'"
            else:
                stmt += f"model"\
                    f".{k} {operator} {v}"
            if ind < len(col):
                stmt += ', '
        return stmt

    @staticmethod
    def _add_order_by(order_by: Sequence[str] | None) -> str | None:
        """Constructs optional ordering.

        Args:
            order_by (List[str], optional): A list of column names by which 
                                            the query results should be ordered.
                                            Defaults to None.
        Returns:
            str: The constructed SQLAlchemy query string.
        """
        if not order_by:
            return None
        else:
            a = ''
            for i, o in enumerate(order_by):
                if isinstance(o, str):
                    a += f'model.{o}'
                if i < len(order_by):
                    a += ', '
            a = '.order_by(' + a + ')'
            return a

    @staticmethod
    def _crt_query(
            params: Sequence[str | None],
            order_by: str | None
            ) -> str | None:
        """
        Constructs an SQLAlchemy query string based on provided 
        data from parameter functions.

        Args:
            params (Callable[[Dict[str, T]], Union[str, List[str]]]):
                    A callable function that generates 
                    either an SQLAlchemy parameters string or 
                    a list of parameters strings based on 
                    the provided arguements.
            order_by (Callable[[List[str]], str]): 
                    A callable function that creates string
                    of ordering for SQLAlchemy session. Default is None.
        Returns:
            str: The constructed SQLAlchemy query string.
        """
        param: list = []
        for s in params:
            if s:
                param.append(s)
        else:
            new_query = ''
            for i, q in enumerate(param):
                new_query += q
                if i < len(param):
                    new_query += ', '
            p = ('self.session.scalars(select(model).'
                 'where(') + new_query + ')).all()'
            if order_by:
                p = p + order_by
            return p

    @classmethod
    def crt_custom_query(
            cls,
            equal: Mapping[str, Any] = None,
            greater_than: Mapping[str, Any] = None,
            less_than: Mapping[str, Any] = None,
            not_equal: Mapping[str, Any] = None,
            greater_than_or_equal_to: Mapping[str, Any] = None,
            less_than_or_equal_to: Mapping[str, Any] = None,
            order_by: Sequence[str] = None) -> str:

        return cls._crt_query([
            cls._crt_param(equal, '=='),
            cls._crt_param(not_equal, '!='),
            cls._crt_param(greater_than, '>'),
            cls._crt_param(less_than, '<'),
            cls._crt_param(greater_than_or_equal_to, '>='),
            cls._crt_param(less_than_or_equal_to, '<='),
            ],
            cls._add_order_by(order_by))
    
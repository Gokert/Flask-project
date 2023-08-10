from typing import Optional

from pymysql import connect
from pymysql.cursors import Cursor
from pymysql.connections import Connection
from pymysql.err import OperationalError


class DBContextManager:
    """A class for connecting to the database and executing sql queries."""

    def __init__(self, config: dict):
        """Initialization of the connection object."""

        self.config: dict = config
        self.conn: Optional[Connection] = None
        self.cursor: Optional[Cursor] = None

    def __enter__(self) -> Optional[Cursor]:
        """ Implements the logic of logging into the context manager."""

        try:
            self.conn = connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except OperationalError as err:
            if err.args[0] == 1045:
                print('Invalid login or password')
            elif err.args[0] == 1049:
                print('Check database name')
            else:
                print(err)
            return None

    def __exit__(self, exc_type, exc_val, exc_tr) -> bool:
        """Implements the logic of exiting the context manager to work with the database."""

        if exc_type:
            print(f"Error type: {exc_type.__name__}")
            print(f"DB error: {' '.join(exc_val.args)}")

        if self.conn and self.cursor:
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
            self.conn.close()
            self.cursor.close()
        return True

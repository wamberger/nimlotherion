
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from tests.test_conn.models.Users import Users

from tests.test_conn.models.Pers import Pers
from tests.test_conn.models.Email import Email


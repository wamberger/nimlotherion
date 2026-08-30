

from sqlalchemy import Column
from tests.test_conn.models import Base
from sqlalchemy.dialects.sqlite import INTEGER
from sqlalchemy.dialects.sqlite import TEXT
from sqlalchemy.dialects.sqlite import REAL
from sqlalchemy.dialects.sqlite import BLOB


class Users(Base):
    __tablename__ = 'users'


    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False, default=' ')
    email = Column(TEXT, nullable=True, default=None)
    age = Column(INTEGER, nullable=True, default=None)
    heigh = Column(REAL, nullable=True, default=None)
    data = Column(BLOB, nullable=True, default=None)



    def __post_init__(self):

        if self.id and not isinstance(self.id, int):
            try:
                self.id = int(self.id)
            except:
                raise SyntaxError(f'< {self.id} > is not integer')
        
        if self.name and not isinstance(self.name, str):
            try:
                self.name = str(self.name)
            except:
                raise SyntaxError(f'< {self.name} > is not string')
        
        if self.email and not isinstance(self.email, str):
            try:
                self.email = str(self.email)
            except:
                raise SyntaxError(f'< {self.email} > is not string')
        
        if self.age and not isinstance(self.age, int):
            try:
                self.age = int(self.age)
            except:
                raise SyntaxError(f'< {self.age} > is not integer')
        
        if self.heigh and not isinstance(self.heigh, float):
            try:
                self.heigh = float(self.heigh)
            except:
                raise SyntaxError(f'< {self.heigh} > is not float')
        
        if self.data and not isinstance(self.data, str):
            try:
                self.data = str(self.data)
            except:
                raise SyntaxError(f'< {self.data} > is not string')
        
    
    def __str__(self):

        return f'User(id={self.id},'\
			f'name={self.name},'\
			f'email={self.email},'\
			f'age={self.age},'\
			f'heigh={self.heigh},'\
			f'data={self.data})'


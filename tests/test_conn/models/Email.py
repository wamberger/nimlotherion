

from sqlalchemy import Column
from tests.test_conn.models import Base
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.dialects.oracle import VARCHAR
from sqlalchemy.orm import relationship


class Email(Base):
    __tablename__ = 'email'


    email = Column(VARCHAR(320), primary_key=True)
    text = Column(VARCHAR(70), nullable=False, default=' ')
    persnr = Column(NUMBER(11,0), nullable=False, default=0)
    exchange = Column(VARCHAR(1), nullable=False, default=' ')
    oof = Column(VARCHAR(1), nullable=False, default=' ')
    exchange_feier = Column(VARCHAR(1), nullable=False, default='N' )



    def __post_init__(self):

        if self.email and not isinstance(self.email, str):
            try:
                self.email = str(self.email)
            except:
                raise SyntaxError(f'< {self.email} > is not string')
        
        if self.text and not isinstance(self.text, str):
            try:
                self.text = str(self.text)
            except:
                raise SyntaxError(f'< {self.text} > is not string')
        
        if self.persnr and not isinstance(self.persnr, int):
            try:
                self.persnr = int(self.persnr)
            except:
                raise SyntaxError(f'< {self.persnr} > is not integer')
        
        if self.exchange and not isinstance(self.exchange, str):
            try:
                self.exchange = str(self.exchange)
            except:
                raise SyntaxError(f'< {self.exchange} > is not string')
        
        if self.oof and not isinstance(self.oof, str):
            try:
                self.oof = str(self.oof)
            except:
                raise SyntaxError(f'< {self.oof} > is not string')
        
        if self.exchange_feier and not isinstance(self.exchange_feier, str):
            try:
                self.exchange_feier = str(self.exchange_feier)
            except:
                raise SyntaxError(f'< {self.exchange_feier} > is not string')
        
    
    def __str__(self):

        return f'User(email={self.email},'\
			f'text={self.text},'\
			f'persnr={self.persnr},'\
			f'exchange={self.exchange},'\
			f'oof={self.oof},'\
			f'exchange_feier={self.exchange_feier})'


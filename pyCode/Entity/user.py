from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)
  nombreCompleto = Column('nombre_completo', String(100))
  nombreUsuario = Column('nombre_usuario', String(100))
  password = Column('pass', String(100))
  score = Column('score', Integer)

  
  def __repr__(self):
    return "<Entity('%d', '%s', '%s', '%s', '%d')>" % (self.id, self.nombreCompleto, self.nombreUsuario, self.password, self.score)
        
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trophy(Base):
  __tablename__ = 'trophy'
  id = Column(Integer, primary_key=True)
  name = Column('name', String)
  des = Column('des', String)
  image = Column('image', String)

  
  def __repr__(self):
  	return "<Entity('%d', '%s', '%s', '%s', '%d')>" % (self.id, self.nombreCompleto, self.nombreUsuario, self.password, self.score)
  
  def toDict(self, removeAtr = []):
    dictUser = vars(self)
    dictUser.pop('_sa_instance_state', None)
    dictUser.pop('image', None)
    print(dictUser)
    for i in removeAtr:
      dictUser.pop(i, None)
    return dictUser

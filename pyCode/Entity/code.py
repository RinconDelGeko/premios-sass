from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Code(Base):
  __tablename__ = 'code'
  id = Column(Integer, primary_key=True)
  userId = Column('user_id', String)
  submitDate = Column('submit_date', Date)
  des = Column('des', String)
 	codeSample = Column('code_sample', String)

  
  def __repr__(self):
  	return "<Entity('%d', '%s', '%s', '%s', '%d')>" % (self.id, self.nombreCompleto, self.nombreUsuario, self.password, self.score)
  
  def toDict(self, removeAtr = []):
    dictUser = vars(self)
    dictUser.pop('_sa_instance_state', None)
    print(dictUser)
    for i in removeAtr:
      dictUser.pop(i, None)
    return dictUser

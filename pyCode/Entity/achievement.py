from sqlalchemy import Column, Integer, String

class Archivement():
  __tablename__ = 'archivement'
  id = Column(Integer, primary_key=True)
  nombreCompleto = Column('nombre_completo', String)
  nombreUsuario = Column('nombre_usuario', String)
  password = Column('pass', String)
  score = Column('score', Integer)

  
  def __repr__(self):
  return "<Entity('%d', '%s', '%s', '%s', '%d')>" % (self.id, self.nombreCompleto, self.nombreUsuario, self.password, self.score)
  
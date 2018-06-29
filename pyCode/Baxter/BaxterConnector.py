import inspect
import bottle
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import ScopedSession

#Importaciones Propias
import baxterSession


# PluginError is defined to bottle >= 0.10
if not hasattr(bottle, 'PluginError'):
  class PluginError(bottle.BottleException):
    pass
  bottle.PluginError = PluginError


class BaxterConnector(object):

  name = 'baxter'
  api = 2
      
  def __init__(self, securityConfig = None):
    print("init")
    if securityConfig == None:
      self.useSecurity = False;
    else:
      self.useSecurity = True;
      print("Get Config")
      self.securityConfig = securityConfig
      self.createSession = sessionmaker()

  def setup(self, app):
    print("setup")
    for other in app.plugins:
      if isinstance(other, BaxterConnector):
        raise PluginError("Found another BaxterConnector.")
    self.sessionManager = baxterSession.BaxterSessionManager(self.securityConfig)
    self.sessionManager.start()
  def apply(self, callback, context):

    def wrapper(*args, **kwargs):
    
      keyword = self.securityConfig.dataSource.keyword[0]
      argsCallback = inspect.getargspec(context.callback)[0]
      usedb = False
      commit = self.securityConfig.dataSource.commit;
      engine = self.securityConfig.dataSource.engine[0];
      if keyword in argsCallback:
        kwargs[keyword] = session = self.createSession(bind=engine)
        usedb = True
        print('usedb')
      
      if self.useSecurity:
        self.sessionManager.processPermission()
        
      if usedb:
        try:
          rv = callback(*args, **kwargs)
          if commit:
            session.commit()
        except (SQLAlchemyError, bottle.HTTPError):
          session.rollback()
          raise
        except bottle.HTTPResponse:
          if commit:
            session.commit()
          raise
        finally:
          if isinstance(self.createSession, ScopedSession):
            self.createSession.remove()
          else:
              session.close()
      else:
        rv = callback(*args, **kwargs)
      
      return rv
    return wrapper
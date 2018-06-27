import inspect
import bottle

#Importaciones Propias
import BaxterSession


# PluginError is defined to bottle >= 0.10
if not hasattr(bottle, 'PluginError'):
    class PluginError(bottle.BottleException):
        pass
    bottle.PluginError = PluginError


class BaxterConnector(object):

    name = 'baxter'
	api = 2
		
    def __init__(self, securityConfig = None):
        
		if securityConfig == None:
			self.useSecurity = False;
		else:
			self.securityConfig = securityConfig
    
	def setup(self, app):
        for other in app.plugins:
            if isinstance(other, BaxterConnector):
				raise PluginError("Found another BaxterConnector.")
			else:
				if other.name == "sqlalchemy":
					print("Sql Alchemy Plugin installed")
					self.dataOrigin = other
		self.sessionManager = BaxterSession.BaxterSessionManager(securityConfig, self.dataOrigin)
		self.sessionManager.start()
    def apply(self, callback, context):

        def wrapper(*args, **kwargs):
				if self.useSecurity:
					self.sessionManager.checkSession()
				rv = callback(*args, **kwargs)
                
            return rv

        return wrapper


Plugin = BaxterConnector
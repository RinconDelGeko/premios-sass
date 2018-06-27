import applicationConfig
from bottle import request, redirect

class BaxterSessionManager():

	def __init__(self, configuration, dataOrigin = None):
		self.configuration = configuration
		self.

	def checkPermission(self, restFunction):
		
		appConfig = applicationConfig.baseConfiguration

		requestPath = request.path

		sessionId = request.get_cookie("sessionId", secret=appConfig.secretKey)

		if sessionId:
			
			usuarioActual = appConfig.usersDict[sessionId]
			
			if usuarioActual != None and usuarioActual.checkPermission(requestPath):
				#Puede usar la web
				return restFunction(*args, **kwargs):
				
			else:
				#Necesita iniciar sesion
				return '<p> Sin Acceso </p>'
		else:
			if userManager.unknownCheckPermission(requestPath):
				print("true")
			else:
				print("false")
				redirect("/login")

		return restFunction(*args, **kwargs)
		
	def start(self):
		
		
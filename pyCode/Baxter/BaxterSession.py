from bottle import request, redirect

class BaxterSessionManager():

  def __init__(self, configuration, dataOrigin = None):
    self.configuration = configuration

  def processPermission(self):
    requestPath = request.path
    print(requestPath)
    """
    sessionId = request.get_cookie("sessionId", secret=self.configuration.cookieKey)
    if sessionId:
      usuarioActual = appConfig.usersDict[sessionId]
			
      if usuarioActual != None and checkPermission(requestPath):
        #Puede usar la web
        return restFunction(*args, **kwargs)
				
      else:
        #Necesita iniciar sesion
        return '<p> Sin Acceso </p>'
    else:
      if unknownCheckPermission(requestPath):
        print("true")
      else:
        print("false")
        redirect("/login")
    return restFunction(*args, **kwargs)
    677"""
  def unknownCheckPermission(variable):
    return True
  def checkPermission(variable):
    return True

  def start(self):
    print("start")
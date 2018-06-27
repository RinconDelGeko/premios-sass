class BaxterSessionConfiguration():
	def __init__(self, loginOrigin, permissionOrigin = None, roleOrigin = None, loginJoin = "id", permissionJoin = "id", roleJoin = "id", cookieKey = None, sessionTime = 600, cacheTime = 600):
		self.loginOrigin = loginOrigin
		self.permissionOrigin = permissionOrigin
		self.roleOrigin = roleOrigin
		self.loginJoin = loginJoin
		self.permissionJoin = permissionJoin
		self.roleJoin = roleJoin
		self.cookieKey = cookieKey
		self.sessionTime = sessionTime
		self.cacheTime = cacheTime

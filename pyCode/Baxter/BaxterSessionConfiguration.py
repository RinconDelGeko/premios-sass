class BaxterSessionConfiguration():
	def __init__(self, dataSource = None, permissionOrigin = None, roleOrigin = None, loginJoin = "id", permissionJoin = "id", roleJoin = "id", cookieKey = None, sessionTime = 600, cacheTime = 600):
		self.dataSource = dataSource
		self.permissionOrigin = permissionOrigin
		self.roleOrigin = roleOrigin
		self.loginJoin = loginJoin
		self.permissionJoin = permissionJoin
		self.roleJoin = roleJoin
		self.cookieKey = cookieKey
		self.sessionTime = sessionTime
		self.cacheTime = cacheTime

class DataSource():
  def __init__(self, engine, keyword='db', commit=True):
    self.engine = engine,
    self.keyword = keyword,
    self.commit = commit
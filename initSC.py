from bottle import run, TEMPLATES, install
import sys

def main():
  TEMPLATES.clear()
  sys.path.append('./pyCode')
  sys.path.append('./pyCode/Entity')
  sys.path.append('./pyCode/EntityManager')
  sys.path.append('./pyCode/Baxter')

  pluginInstall()
  
  import routes
  run(host = '127.0.0.1', port = 8888, reloader=True)
  
  
def pluginInstall():
  from sqlalchemy import create_engine
  import baxterSessionConfiguration
  import baxterConnector
  import userManager
  engine = create_engine('sqlite:///./sqlite/premios-sass.db', echo=True)
  dataSource = baxterSessionConfiguration.DataSource(
    engine,
    keyword='db',
    commit=True
  )
  userManager = userManager.UserManager()
  configuration = baxterSessionConfiguration.BaxterSessionConfiguration(
    dataSource = dataSource,
    permissionOrigin = userManager,
    roleOrigin = None,
    loginJoin = "id",
    permissionJoin = None,
    roleJoin = None,
    cookieKey = "Hola",
    sessionTime = 600,
    cacheTime = 600
  )
  obj = baxterConnector.BaxterConnector(configuration)
  install(obj)
		
if __name__ == "__main__":
  main()

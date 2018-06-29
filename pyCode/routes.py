from bottle import get, template, redirect, route, static_file, install

import json

from user import User

def generateTemplate(returnTemplate):
  return template('./web-page/header') + template('./web-page/main-menu') + template(returnTemplate) + template('./web-page/footer')

@get('/')
def defaultPath():
  redirect('/dashboard')

#DASHBOARD

@get('/dashboard')
def main():
  return generateTemplate('./web-page/dashboard')

@get('/dashboard/table-get-last-trophy')
def tableGetLastTrophy():
	jsonResponse="""
	[{
		"name": "Nick",
		"trophy": "Perder a Kirby",
		"score": 123,
		"top": 3
		},{
		"name": "Calatrava",
		"trophy": "Todo",
		"score": 9000,
		"top": 1
		},{
		"name": "David",
		"trophy": "Error de importacion",
		"score": 111,
		"top": 2
		}]
	"""
	return jsonResponse
	
#Profile

@get('/profile/edit/<name>')
def editUser(name):
  return(generateTemplate('./web-page/profile-page-edit'))
  
@get('/profile/close')
def closeSession():
  return '<h1>Por Hacer</h1>'
  
@get('/profile/<name>')
def getUser(name):
  return(generateTemplate('./web-page/profile-page'))
  
  
#User
@get('/user')
def getUser():
  return(generateTemplate('./web-page/user'))

@get('/user/<name>')
def getUser(name):
  return(generateTemplate('./web-page/user-page'))
  
  
@get('/user/table-get-users')
def getUser(db):
  print("entra nates")
  test = db.query(User).all()
  print("Entra")
  dictfinal = dict()
  listJson = []
  for i in test:
    data = i.toDict()
    listJson.append(data)
    
  dictfinal['rows'] = listJson
  dictfinal['total'] = 4
  return dictfinal
  
@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root='./web-page')

@get('/prueba')
def testbd(db):
  entity = db.query(User).all()
  return print(entity)
  
  
from bottle import get, template, redirect


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
	
	#Perfil
	
@get('/profile/<name>')
def getUser(name):
	return(generateTemplate('./web-page/user-page'))
	

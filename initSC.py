from bottle import run, TEMPLATES
import sys


def main():
	TEMPLATES.clear()
	sys.path.append('./pyCode')
	import routes
	run(host = '127.0.0.1', port = 8888, reloader=True)
	
if __name__ == "__main__":
	main()


import cgi
import datetime
import webapp2

from google.appengine.ext import db

class Feed(db.Model):
	secret = db.StringProperty()
	author = db.UserProperty()
	content = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)
	
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('main page')

class Stream(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('stream api')

app = webapp2.WSGIApplication([
	('/api', MainPage),
	('/api/stream', Stream),
	('/', MainPage)
], debug=True)

import webapp2
import simplejson as json
from google.appengine.ext import db

class Feed(db.Model):
	stream = db.StringProperty()
	input = db.StringProperty(multiline=True)
	data = db.StringProperty(multiline=True)
	datetime = db.DateTimeProperty(auto_now_add=True)
	
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write('<h3>Nano Cloud Logger</h3>')

class StreamGet(webapp2.RequestHandler):
	def get(self):
		response = []		
		if self.request.get('limit') <> '':
			limit = 'limit ' + self.request.get('limit')
		else:
			limit = ''
		
		feed = db.GqlQuery('select * from Feed where stream=:1 order by datetime desc ' + limit, self.request.get('stream'))
		
		if self.request.get('lastid') <> '':
			for entry in feed:
				if int(self.request.get('lastid')) < entry.key().id():
					response.append({
						'id': entry.key().id(),
						'input': str(entry.input),
						'data': str(entry.data),
						'datetime': str(entry.datetime)
					})
		else:
			for entry in feed:
				response.append({
					'id': entry.key().id(),
					'input': str(entry.input),
					'data': str(entry.data),
					'datetime': str(entry.datetime)
				})
		
		if self.request.get('format') == 'csv':
			self.response.headers['Content-Type'] = 'plain/text'
			for item in response:
				self.response.out.write(str(item['id']) + ',')
				self.response.out.write(str(item['datetime']) + ',')
				self.response.out.write(str(item['input']) + ',')
				self.response.out.write(str(item['data']) + '\n')
		else:
			self.response.headers['Content-Type'] = 'application/json'
			self.response.out.write(json.dumps(response, separators=(',',':')))
	def post(self):
		self.error(405)
		self.response.out.write('405 Method Not Allowed')

class StreamSet(webapp2.RequestHandler):
	def get(self):
		self.error(405)
		self.response.out.write('405 Method Not Allowed')
	def post(self):
		for input in self.request.arguments():
			if (str(input) <> 'format' and str(input) <> 'stream'):
				feed = Feed()
				feed.stream = str(self.request.get('stream'))
				feed.data = self.request.get(input)
				feed.input = str(input)
				feed.put()
		
		if self.request.get('format') == 'csv':
			self.response.headers['Content-Type'] = 'plain/text'
			self.response.out.write('status: ok')
		else:
			self.response.headers['Content-Type'] = 'application/json'
			self.response.out.write(json.dumps({'status' : 'ok'}, separators=(',',':')))

app = webapp2.WSGIApplication([
	('/api', MainPage),
	('/api/get', StreamGet),
	('/api/set', StreamSet),
	('/', MainPage)
], debug=True)
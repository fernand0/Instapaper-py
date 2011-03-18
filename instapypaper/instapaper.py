import oauth2 as oauth
import urllib, urlparse
from dolt import Dolt
try:
	import json
except:
	import simplejson as json

class InstapaperAPI(Dolt):
	def __init__(self, consumer_key, secret, *args, **kwargs):
		super(InstapaperAPI, self).__init__(*args, **kwargs)
		self._api_url = 'https://www.instapaper.com/api/1'
		self._url_template = "%(domain)s/%(generated_url)s"
		self._headers = {}
		self._consumer = consumer_key
		self._secret = secret
	
	def __call__(self, *args, **kwargs):
	    self._attribute_stack += [str(a) for a in args]
	    self._params = kwargs
	    body = self._generate_body()
	    url = self.get_url()
	    if body == None:
	    	body =''
	    response, data = self._http.request(self.get_url(), self._method, body=body)
	    self._attribute_stack = []
	    return self._handle_response(response, data)

	def get_xauth_access_token(self, username, password):
		consumer = oauth.Consumer(self._consumer, self._secret)
		client = oauth.Client(consumer)
		url = self._api_url+'/oauth/access_token'
		
		resp, content = client.request(url, "POST",urllib.urlencode({
			'x_auth_mode': 'client_auth',
			'x_auth_username': username,
			'x_auth_password': password
			})
		)
		token = dict(urlparse.parse_qsl(content))
		
		token = oauth.Token(token['oauth_token'], token['oauth_token_secret'])
	
		self._http = oauth.Client(consumer, token)
		
	
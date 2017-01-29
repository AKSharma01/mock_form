from flask import session
from models import *

class FormActivity:
	"""docstring for RegForm"""
	def __init__(self, data ):
		self.data = data  			# This data is in dict format
		self.db = DBActivity()


	def register(self):
		self.db.insert_into_profile(self.data)
		# username = self.db.select_form_profile(self.data['email'])[0][1]
		self.db.close()
		# return username


	def logvalidate(self):
		verify = self.db.select_form_profile(self.data['email'])
		if self.data['password'] == verify[0][4]:
			session['userid'] = verify[0][0]
			session['username'] = verify[0][1]
			self.db.close()
			return True
		return False
	
	def create_slug(self):
		self.db.insert_into_slug(self.data)
		sulgid = self.db.select_form_slug(self.data['slug'])[0][0] ##it can have similar slugid 
		self.db.close()
		return sulgid

	def create_slug_version(self):
		self.db.insert_into_slug_version(self.data)
		slugversionid = self.db.select_form_slug_version(self.data['sulgid'],self.data['vesion'])[0][0] #it can have 
		self.db.close()
		return slugversionid
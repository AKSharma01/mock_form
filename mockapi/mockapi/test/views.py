from flask import Flask, render_template, session, redirect, request, jsonify
from flask.views import MethodView
from forms import FormActivity
import json, uuid, re

class Start(MethodView):
	def __init__(self):
		pass

	def get(self):
		return "welcome to the flask mockapi project"


class Log(MethodView):
	"""docstring for log"""
	def __init__(self):
		pass

	def get(self):
		if 'username' in session:
			return redirect('/mockapi')
		return "hello"

	def post(self):
		jsondata = request.get_json()
		reg = FormActivity(jsondata)
		if reg.logvalidate():
			return redirect('/mockapi')
		return redirect('/login')

class Logout(MethodView):
	"""docstring for Logout"""
	def __init__(self):
		pass

	def get(self):
		if 'username' in session:
			session.pop('username', None)
		return redirect('/login')


class Reg(MethodView):
	"""docstring for Reg"""
	def __init__(self):
		pass

	def get(self):
		return render_template('form/reg.html')

	def post(self):
		msg = ''
		jsondata = request.get_json()
		if re.search(r'\w+@sourceeasy.com',jsondata['email']):
			reg = FormActivity(jsondata)
			reg.register()
			return "You have been successfully registered"
		else :
			msg = "Mail domen should be of sourceeasy.com"
		return msg


class Dashboard(MethodView):
	"""docstring for Dashboard"""
	def __init__(self):
		pass

	def get(self):
		if 'username' in session:
			return "welcome to Dashboard Mr. {}".format(session['username'])
		return "Sorry Session has been expired or you has been logged out"


class CreateForm(MethodView):
	"""docstring for CreateForm"""
	def __init__(self):
		pass

	def post(self):
		if 'username' in session:
			jsondata = request.get_json()
			jsondata1 = {
				"userid" : session['userid'],
				"slug" : uuid.uuid1().bytes.encode('base64').rstrip('=\n').replace('/', '_'),
			}
			slugcreate = FormActivity(jsondata1)
			slugid = slugcreate.create_slug()
			jsondata2 = {
				"slugid" : slugid,
				"version" : jsondata['version'],
				"jsondata" : jsondata['jsondata']
			}
			slugversioncreate = FormActivity(jsondata2)
			versionid = slugversioncreate.create_slug_version()
			return "New slug is inserted into database with id = %s".format(str(versionid))
		return "Sorry Please login first"

class EditJson(MethodView):
	"""docstring for EditJson"""
	def __init__(self):
		pass

	def get(self, slug, version):
		pass

	def post(self, slug, version):
		pass

	def put(self):
		pass

class ViewJson(MethodView):
	"""docstring for ViewJson"""
	def __init__(self):
		pass

	def get(self,slug,version):
		pass

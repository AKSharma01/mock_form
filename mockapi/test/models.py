import sqlite3 as sql
import uuid
import os
from flask import g

class DBActivity:
	"""docstring for DBActivity"""
	def __init__(self):
		# get project folder
		x = os.getcwd()
		#get database folder
		print x
		#DATABASE = x+'/test/Database/database.db'
		DATABASE = '/tmp/database.db'
		db = getattr(g, '_database', None)
		if db is None:
			self.db = g._database = sql.connect(DATABASE) #create database.db in the folder if not exist
			self.cur = self.db.cursor()
			self.cur.execute("CREATE TABLE IF NOT EXISTS profile (id varchar primary key, username varchar, fullname varchar, email varchar, password varchar)")
			self.cur.execute("CREATE TABLE IF NOT EXISTS slug (id varchar primary key, userid varchar, slug varchar)")
			self.cur.execute("CREATE TABLE IF NOT EXISTS slug_version (id varchar primary key, slugid varchar, version varchar, jsondata JSON, date_time timestamp)")

		
	def insert_into_profile(self, data):
		self.cur.execute("INSERT INTO profile (id , username, fullname, email, password) VALUES (?,?,?,?,?)", (str(uuid.uuid4()), str(data['username']), str(data['fullname']), str(data['email']), str(data['password'])))
		self.db.commit()
	
	def insert_into_slug(self, data):
		self.cur.execute("INSERT INTO slug (id, userid, slug) VALUES (?,?,?)", (str(uuid.uuid4()), str(data['userid']), str(data['slug'])))
		self.db.commit()

	def insert_into_slug_version(self, data):
		self.cur.execute("INSERT INTO slug_version (id, slugid, version, jsondata) VALUES (?,?,?,?)",(str(uuid.uuid4()), str(data['slugid']), str(data['vesion']), data['jsondata']))
		self.db.commit()

	def select_form_profile(self, email):
		self.cur.execute("SELECT * from profile where email = ?",[email])
		return self.cur.fetchall()
	
	def select_form_slug(self, slug):
		self.cur.execute("SELECT * FROM slug WHERE slug = ?", [slug])
		return self.cur.fetchall()

	def select_form_slug_vesion(self, slugid, vesion):
		self.cur.execute("SELECT * FROM slug WHERE slugid = ? AND slug_version = ?", [slug,vesion])
		return self.cur.fetchall()
		
	# def select(self):
	# 		self.cur.execute("SELECT * from jsondb")
	# 		return self.cur.fetchall()

	# def selectByHash(self, hash):
	# 	self.cur.execute("SELECT * from jsondb where data = ?",[hash])
	# 	return self.cur.fetchall()

	def close(self):
		self.db.close()


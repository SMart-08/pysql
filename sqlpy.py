import mysql.connector as connector
class DBclass:
	def __init__(self):
		self.mydb = connector.connect(
 		host="localhost",
		user="root",
	  	password="dbms",
  		database="project")

	def exe(self,query):
		cur = self.mydb.cursor()
		cur.execute(query)
		return cur.fetchall()

	def create_table(self,table_deatils):
		result = self.exe('CREATE TABLE IF NOT EXISTS '+table_deatils+';')
		self.mydb.commit()
		return result

	def insert_row(self,name,bldgrp,phno):
		result = self.exe('INSERT INTO data(name,bldgrp,phno) values(\'{}\',\'{}\',\'{}\')'.format(name,bldgrp,phno))
		self.mydb.commit()
		return result

	def select_query(self,query):
		result = self.exe(query)
		for row in result:
			print(row)

	def select_all(self):
		result = self.exe('SELECT * FROM data')
		for row in result:
			print(row)

	def delete_id(self,userid):
		result = self.exe('DELETE FROM data WHERE userid={}'.format(userid))
		self.mydb.commit()
		return result

	def update_row(self,userid,new_name,new_bldgrp,new_phno):
		result = self.exe('UPDATE data SET name=\'{}\',bldgrp=\'{}\',phno=\'{}\'  where userid={}'.format(new_name,new_bldgrp,new_phno,userid))
		self.mydb.commit()
		return result
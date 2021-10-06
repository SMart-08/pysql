# pysql 

Overview: 
* I have designed and implemented a Database Accesing Applicaton Logic from scrach.
* It's a MINI Project which express how can we connect mysql database with python using python mysql connector module

Features:
* This application provide a non-tech user a friendly interface to access database without knowning any Query language or database fundamentals.
* Mysql query writting process has been automated with help of python code.
* Because application is developed on OOPs methodology, Code is easy to maintain and modify.

Futher Improvement Possibilities:
 As Query writting process has been automated, User is restricted to predefined set of commands.
 Requirements of additional features from User's side can be fulfilled by Developer in no time.
 As adding features is easy task because of Clean uderstandable Code & OOPs benefits.

System Requirements
pyhton3 installed with mysql-connector module (scr: https://pypi.org/project/mysql-connector-python/ )
mysql installed 
Database_details,user_id & password updated in pysql.py file.

Dive in technical !

mysql> USE project;
Database changed

mysql> SHOW TABLES;
+-------------------+
| Tables_in_project |
+-------------------+
| data              |
+-------------------+

mysql> DESCRIBE data;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| userid | int          | NO   | PRI | NULL    | auto_increment |
| name   | varchar(100) | YES  |     | NULL    |                |
| bldgrp | varchar(4)   | YES  |     | NULL    |                |
| phno   | varchar(12)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+


#Here "project" is our DB and "data" is table on which our python code runs And user don't need to learn only query language to access Database, this task has been automated by python code

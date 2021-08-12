from sqlpy import DBclass

def main():
	obj = DBclass()
	obj.create_table(' data( userid INT not null auto_increment, name VARCHAR(100), bldgrp VARCHAR(4), phno VARCHAR(12),primary key(userid) ) ')
	while 1:
		print('*'*20+'WELCOME'+'*'*20)
		ch = int(input('PRESS 1 - TO INSERT NEW ENTRY\nPRESS 2 - TO UPDATE ENTRY\nPRESS 3 - TO DELETE A ENTRY\nPRESS 4 - TO DISPLAY ALL\nPRESS 5 - TO DISPLAY WITH CONDITION\nPRESS 6 - TO EXIT\n'))

		if ch==1:
			name = str(input('NAME: '))
			bldgrp = str(input('BLOOD GROUP: '))
			phno = str(input('PHONE NO: '))
			obj.insert_row(name,bldgrp,phno)
			print('INSERTED in DB')

		elif ch==2:
			result = obj.exe('SELECT userid,name FROM data;')
			if result!=[]:
				print(result)
				userid = input('ENTER USER ID HERE: ')
				data = obj.exe('SELECT name,bldgrp,phno FROM data WHERE userid={}'.format(userid))
				name,bldgrp,phno = data[0]
				while 1:
					upch = int(input('\nPRESS - TO UPDATE\n1 - NAME\n2 - BLOOD GROUP\n3 - PHONE NO\n4 - NO MORE UPDATES\n'))
					print('\n')
					if upch==1:
						name=input('ENTER NEW NAME: ')
					elif upch==2:
						bldgrp=input('ENTER NEW BLOOD GROUP: ')
					elif upch==3:
						phno=input('ENTER NEW PHONE NO: ')
					elif upch==4:
						break;
					else:
						print('{} is INVALID choices\n TRY AGAIN'.format(upch))
				obj.update_row(userid,name,bldgrp,phno)
				print('UPDATED DB')
			else:
				print('EMPTY RESULT SET')

		elif ch==3:
			result = obj.exe('SELECT userid,name FROM data;')
			print(result)
			userid = input('ENTER USER ID HERE: ')
			obj.delete_id(userid)
			print('UPDATED DB')

		elif ch==4:
			obj.select_all()

		elif ch==5:
			conch = int(input('\nPRESS - TO CONDITION ON\n1 - NAME\n2 - BLOOD GROUP\n3 - PHONE NO\n'))
			if conch==1:
				result = obj.exe('SELECT DISTINCT name FROM data;')
				print(result)
				name = input('ENTER NAME HERE: ')
				result = obj.select_query('SELECT * FROM data WHERE name=\'{}\''.format(name))
				print(result)
			elif conch==2:
				result = obj.exe('SELECT DISTINCT bldgrp FROM data;')
				print(result)
				bldgrp = input('ENTER BLOOD HERE HERE: ')
				result = obj.select_query('SELECT * FROM data WHERE bldgrp=\'{}\' '.format(bldgrp))
				print(result)
			elif conch==3:
				result = obj.exe('SELECT DISTINCT phno FROM data;')
				print(result)
				phno = input('ENTER PHONE NO HERE: ')
				result = obj.select_query('SELECT * FROM data WHERE phno=\'{}\' '.format(phno))
				print(result)
			else:
				print('{} is INVALID choices\n TRY AGAIN'.format(conch))

		elif ch==6:
			break;
		
		else:
			print('{} is INVALID choices\n TRY AGAIN'.format(ch))

main()
import mysql.connector

dbconfig = {'host':'127.0.0.1', 'user':'vsearch', 'password':'vsearchpass', 'database':'vsearchlogdb',}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
"""zahardkodowana wartość"""
#_SQL = """insert into log (phrase, letters, ip, browser_string, results) values ('mierni', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""
"""wartosc pozwalająca na przekazanie parametrów pozniej"""
_SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""

#iso cursor.execute(_SQL)
cursor.execute(_SQL, ('mierni', 'aeiou', '127.0.0.1', 'Safari', 'set()'))

conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
	print(row)

cursor.close()

conn.close()

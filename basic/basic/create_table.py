import psycopg2
connection=psycopg2.connect(                         # open connection to postgres database
    host='localhost',
    database='postgres',
    user='postgres',
    password='12345678',
)

print("connection success")
cur=connection.cursor()                              # this is used to execute select statements
'''cur.execute("CREATE TABLE emp2(name TEXT,age INT)")
cur.execute("INSERT INTO emp2(name,age) VALUES  ('ram',22)")
connection.commit()'''                #commit current transaction
cur.execute("SELECT * FROM emp2")
rows=cur.fetchall()   # fetch all rows 
print(rows)
connection.close()   # close the connection 
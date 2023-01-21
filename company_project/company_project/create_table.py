import psycopg2
conn=psycopg2.connect(database="company",user='postgres',password='12345678') # connect to database
print("connected")
cur=conn.cursor()    # it is used to execute select statement
#cur.execute('CREATE TABLE company_info (id INT PRIMARY KEY NOT NULL, name TEXT NOT NULL, age INT NOT NULL, address CHAR(50),salary REAL)')
print("table created")
#conn.commit()    # commit the current transaction

#cur.execute("INSERT INTO company_info (id,name,age,address,salary)VALUES(1,'ram',23,'kolhapur',19000)")
'''cur.execute("INSERT INTO company_info (id,name,age,address,salary)VALUES(2,'raJ',25,'kagal',20000.00)")
cur.execute("INSERT INTO company_info (id,name,age,address,salary)VALUES(3,'sha',23,'kolhapur',23000)")
cur.execute("INSERT INTO company_info (id,name,age,address,salary)VALUES(4,'baban',23,'kagal',19000)")

conn.commit()    # commit the current transaction
print("data inserted")'''


'''cur.execute("SELECT * FROM company_info")
rows=cur.fetchall() # fetch all the rows 
print(rows)'''

'''cur.execute("UPDATE company_info set salary=25000 where id = 2")
conn.commit()'''

print("update data")

cur.execute("DELETE from company_info  where id = 2")
conn.commit()
print("delete data")

conn.close()

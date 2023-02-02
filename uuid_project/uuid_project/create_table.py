import psycopg2
import uuid 
uuid=uuid.uuid4()
con=psycopg2.connect(database='uuid_use',user='postgres',password='12345678',)
cur=con.cursor()

'''cur.execute('CREATE TABLE uuid_table (id uuid DEFAULT uuid_generate_v4(), PRIMARY KEY (id),name varchar(50),owner varchar(50), description varchar(50),scheduled_date Date,scheduled_timestamp timestamp, priority int)')
cur.execute("ALTER TABLE uuid_table ADD COLUMN created_timestamp timestamp, ADD COLUMN complete_timestamp timestamp")
con.commit()'''
#cur.execute("INSERT INTO uuid_table (name,owner,description,created_timestamp,scheduled_date,scheduled_timestamp,priority,complete_timestamp)VALUES('ram','rani','create table using uuid','2023-1-28','2023-1-28','2023-1-28', 3,'2023-2-1')")
cur.execute("INSERT INTO uuid_table (name,owner,description,created_timestamp,scheduled_date,scheduled_timestamp,priority,complete_timestamp)VALUES('raj','rani','create table using uuid','2023-1-29','2023-1-28','2023-1-28', 4,'2023-2-2')")
cur.execute("INSERT INTO uuid_table (name,owner,description,created_timestamp,scheduled_date,scheduled_timestamp,priority,complete_timestamp)VALUES('baban','rani','create table using uuid','2023-1-30','2023-1-29','2023-1-29', 2,'2023-2-1')")
cur.execute("INSERT INTO uuid_table (name,owner,description,created_timestamp,scheduled_date,scheduled_timestamp,priority,complete_timestamp)VALUES('rahul','rani','create table using uuid','2023-2-1','2023-1-29','2023-1-30', 1,'2023-2-1')")


con.commit()

#cur.execute("UPDATE uuid_table SET owner='sam' where (id='201464d9-fa8a-41fa-9c90-57940430269b')")
#con.commit()

#cur.execute("DELETE FROM uuid_table WHERE (id='12d870e8-42bb-4909-9eb6-efaaa5b1dc6e')")
#cur.execute("DELETE FROM uuid_table")
#con.commit()
'''
cur.execute("SELECT * FROM uuid_table")
rows=cur.fetchall()  # fetch all the rows 
for all in rows:
    print(all)

rows=cur.fetchone()  #fetch the one row
print(rows)'''
#rows=cur.fetchmany(2) # fetch many rows
#print(rows)



con.close()
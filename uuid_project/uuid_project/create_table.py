import psycopg2
import uuid 
uuid=uuid.uuid4()
con=psycopg2.connect(database='uuid_use',user='postgres',password='12345678',)
cur=con.cursor()

#cur.execute('CREATE TABLE uuid_table (id uuid DEFAULT uuid_generate_v4(), PRIMARY KEY (id),name varchar(50),owner varchar(50), description varchar(50),scheduled_date Date,scheduled_timestamp timestamp, priority int)')
#con.commit()
#cur.execute("INSERT INTO uuid_table (name,owner,description,scheduled_date,scheduled_timestamp,priority)VALUES('ram','rani','create table using uuid','2023-1-28','2023-1-28', 3)")
#con.commit()
cur.execute("SELECT * FROM uuid_table")
print('create table')


con.close()
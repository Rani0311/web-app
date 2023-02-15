import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask , request

CREATE_STUDENT_TABLE=("CREATE TABLE IF NOT EXISTS student(s_id PRIMARY KEY,s_name TEXT)")

INSERT_STUDENT_RETURN_ID="INSERT INTO student(s_name) VALUES (%s) RETRUNING s_id;"
load_dotenv()  # loading variable from .env file into environment



app=Flask(__name__)

url=os.environ.get("DATABASE_URL")
connection=psycopg2.connect(url)
@app.post("/api/student")    #endpoint to accept the data in using a decorator
def create_student():
    data= request.get.json()
    name=data['name']
    with connection:
        with connection.cursor() as cursor:
             cursor.execute(CREATE_STUDENT_TABLE)
             cursor.execute(INSERT_STUDENT_RETURN_ID,(name,))
             s_id= cursor.fetchone()[0]
    return {'s_id': s_id, 'message':f"sudent {name} created."},201
    

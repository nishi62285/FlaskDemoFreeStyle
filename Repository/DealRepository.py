from app import app
import pyodbc
from flask import current_app
a=current_app
conn = pyodbc.connect(current_app.config['DB_URL'])

#get deals
def get_deals(_id=None):
    result=[]
    cursor=conn.cursor()
    id=_id
    values=(id)
    sql="exec dbo.get_deals ?"
    c=cursor.execute(sql,(values))
    rc=cursor.fetchall()
    columns = [column[0] for column in c.description]
    for i in list(rc):
        result.append(dict(zip(columns,i)))
    return result




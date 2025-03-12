from sqlite3 import *
from sqlite3 import Error
from os import *


def create_connect(path:str):
    connection=None
    try:
        connection=connect(path)
        print("Ühendus on olemas!")
    except Error as e:
        print(f"Tekkis viga: {e}")
    return connection
def execute_query(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud või andmed on sisestatud")
    except Error as e:
        print(f"Tekkis viga: {e}")
def execute_read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Tekkis viga: {e}")
def execute_insert_query(connection,data):
    columns=columns_from_table(conn)
    like=mark=""
    n=len(columns)
    for c in columns:
        n-=1
        if n==0:
            like+=c
            mark+="?"
        else:
            like+=c+","
            mark+="?"+","
    query=f"INSERT INTO users({like}) VALUES({mark})"
    cursor=connection.cursor()
    cursor.execute(query,data)  
    connection.commit()
def columns_from_table(connection):
    filename=path.abspath(__file__)
    dbdir=filename.rstrip('Too_andmebaasiga.py')
    dbpath=path.join(dbdir,"data.db")
    conn=create_connect(dbpath)
    cursor=connection.cursor()
    cursor.execute("PRAGMA table_info('users')") #SELECT name FROM sqlite_master WHERE type='table';")
    column_names = [i[1] for i in cursor.fetchall()]
    return column_names
def execute_drop_table(connection, table):
    try:
        cursor=connection.cursor()
        cursor.execute(f"DROP TABLE IF NOT EXISTS {table}")
        connection.commit()
        print(f"Tabel {table} oli kustutatud")
    except Error as e :
        print(f"Tekkis viga: {e}")
        
        


create_gender_table="""
CREATE TABLE IF NOT EXISTS gender(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Nimetus TEXT NOT NULL)
"""
insert_gender="""
INSERT INTO 
gender(Nimetus) 
VALUES
('mees'),
('naine')"""
create_users_table2="""
CREATE TABLE IF NOT EXISTS users2(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Lname TEXT NOT NULL,
Age INTEGER NOT NULL,
GenderId INTEGER,
FOREIGN KEY (GenderId) REFERENCES gender (Id)
)
"""
insert_users2="""
INSERT INTO
users2(Name,Lname,Age,GenderId)
VALUES
('Mati','Tamm',50,1),
('Kati','Kask',54,2),
('Margus','Tamm',12,1),
('Anna','Kuusk',44,2)
"""

select_users2="SELECT * from users2"
select_users2_gender="""
SELECT 
users2.Name,
users2.Lname,
gender.Nimetus 
from users2 
INNER JOIN gender ON users2.GenderId=gender.Id"""
filename=path.abspath(__file__)
dbdir=filename.rstrip('Tund12(Sqlite3).py')
dbpath=path.join(dbdir,"data.db")
conn=create_connect(dbpath)
execute_query(conn,create_users_table2)
execute_query(conn,insert_users2)
execute_query(conn,create_gender_table)
execute_query(conn,insert_gender)
users=execute_read_query(conn,select_users2)
print("Kautajate tabel 1,2:")
for user in users:
    print(user)
users_genders=execute_read_query(conn,select_users2_gender)
print("Kautajate tabel mees, naine:")
for gender in users_genders:
    print(gender)

# users=execute_read_query(conn,select_users2)
# print("Kautajate tabel:")
# for user in users:
#     print(user)
# insert_user=(input("Eesnimi:"),input("Perenimi"),int(input("Vanus:")),int(input("Sugu:")))
# execute_insert_query(conn,insert_user)



import json
import sqlite3

con = sqlite3.connect('roster_db.sqlite')
cur = con.cursor()

# Database table setup
cur.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Course;
        DROP TABLE IF EXISTS Member;

        CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
        );

        CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
        );

        CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id, course_id)
        )
''')

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'roster_data_sample.json'
str_data = open(fname).read()
json_data = json.loads(str_data)
#print (json_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(name,))
    cur.execute('SELECT id FROM User WHERE name=?',(name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(title,))
    cur.execute('SELECT id FROM Course WHERE title=?',(title,))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)',(user_id,course_id,role))
    
    con.commit()

sqlsort = '''
SELECT User.name, Course.title, Member.role FROM User JOIN Member JOIN Course ON User.id=Member.user_id AND Member.course_id=Course.id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2'''

sqlhex = '''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X FROM User JOIN Member JOIN Course ON User.id=Member.user_id AND
Member.course_id=Course.id ORDER BY X LIMIT 1'''

for row in cur.execute(sqlsort):
    print(str(row[0]),str(row[1]),row[2])

for row in cur.execute(sqlhex):
    print(str(row[0]))

con.close()

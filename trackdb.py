import xml.etree.ElementTree as ET
import sqlite3

con = sqlite3.connect('track_db.sqlite')
cur = con.cursor()

cur.executescript('''
        DROP TABLE IF EXISTS Artist;
        DROP TABLE IF EXISTS Genre;
        DROP TABLE IF EXISTS Album;
        DROP TABLE IF EXISTS Track;

        CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
        );

        CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
        );
        
        CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
        );

        CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        length INTEGER, rating INTEGER, count INTEGER,
        genre_id INTEGER
        )
''')

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'Library.xml'

# create 'lookup' function
def lookup(d,key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

data = ET.parse(fname)
music = data.findall('dict/dict/dict')
print('Entries found:',len(music))

for entry in music:
    if lookup(entry,'Track ID') is None : continue

    track = lookup(entry,'Name')
    artist = lookup(entry,'Artist')
    album = lookup(entry,'Album')
    length = lookup(entry,'Total Time')
    rating = lookup(entry,'Rating')
    count = lookup(entry,'Play Count')
    genre = lookup(entry,'Genre')
    
    if track is None or artist is None or album is None or genre is None : continue

    #print(genre)

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)',(album,artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, length, rating, count, genre_id) 
    VALUES (?, ?, ?, ?, ?, ?)''',(track,album_id,length,rating,count,genre_id))

    con.commit()

sort_artists = '''
SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist 
ON Track.genre_id=Genre.id AND Track.album_id=Album.id AND Album.artist_id=Artist_id ORDER BY Artist.name LIMIT 3
'''

for row in cur.execute(sort_artists):
    print(str(row[0]),str(row[1]),str(row[2]),str(row[3]))

cur.close()

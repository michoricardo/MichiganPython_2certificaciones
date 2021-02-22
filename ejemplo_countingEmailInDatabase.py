import sqlite3 #importar la libreria para usar sqlite3 (bases de datos)

conn = sqlite3.connect('emaildb.sqlite') #nombre del archivo que se va a generar
cur = conn.cursor() #Allows Python code to execute PostgreSQL command in a database session

cur.execute('DROP TABLE IF EXISTS Counts') #ejecuta en lenguaje base de datos

cur.execute(''' 
CREATE TABLE Counts (email TEXT, count INTEGER)''') #ejecuta crear tabla con los campos de email y count del tipo TEXT 
#E INTEGER

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt' #Si el nombre del archivo es mbox-short.txt...
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue #si la linea no empieza con From: regresa al inicio, sino...
    pieces = line.split()
    email = pieces[1] #se obtiene el email
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) #contar de los que tengan el mail de eimail
    row = cur.fetchone() #fetchone hace el fetch de la consulta
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,)) #si esta vacio, entonces le pone los valores
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,)) #Sino, hace update
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' #hace print del email y cuenta de counts y los
#ordena por count, descendiente y con limite 10

for row in cur.execute(sqlstr): #hace print de cada uno de esos
    print(str(row[0]), row[1])

cur.close()
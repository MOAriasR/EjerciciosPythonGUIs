import sqlite3

cnn=sqlite3.connect('tiendita2.db')
micursor=cnn.cursor()
lista=[
    ('Raqueta Badmington',140.35,'Deportes'),
    ('Dardo',45.15,'Deportes'),
    ('Flecha',580,'Deportes')
]
#micursor.execute("insert into productos (nombre,precio,depto) values ('Snorkel',1680.00,'Deportes')")
micursor.executemany("insert into Productos (nombre,precio,depto) values (?,?,?)", lista)
cnn.commit()



micursor.close()
cnn.close() 
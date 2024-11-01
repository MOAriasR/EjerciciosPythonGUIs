import sqlite3
cnn=sqlite3.connect('tiendita2.db')
cursor=cnn.cursor()
#cursor.execute("Drop table Productos")
cursor.execute("create table Productos ('Nombre' varchar(80) not null, 'Precio' real not null, 'Depto' varchar(60) not null)")

cursor.close()
cnn.close()
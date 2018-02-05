import sqlite3
from tkinter import *

root = Tk()
root.title("Bar Borja - Menú")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="   Bar Borja   ", fg="darkblue", font=("Calibri",28,"bold italic")).pack()
Label(root, text="Menú del día", fg="blue", font=("Calibri",24,"bold italic")).pack()

Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

categorias = cursor.execute("SELECT * FROM categoria").fetchall()	
for categoria in categorias:
	Label(root, text=categoria[1], fg="black", font=("Arial",20,"bold italic")).pack()

	platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
	for plato in platos:
		Label(root, text=plato[1], fg="gray", font=("Verdana",15,"italic")).pack()

	Label(root, text="").pack()	

conexion.close()

Label(root, text="10.95€ (IVA incl.)", fg="darkgreen", font=("Arial",20,"bold italic")).pack(side="right")

root.mainloop()
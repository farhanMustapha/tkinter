from tkinter import *
import sqlite3 as db

def validate():
    vr_name=name.get()
    vr_imatriculation=imatriculation.get()
    
    conn=db.connect('Sample.db')
    print("Database created or connected successfully")
    cur=conn.cursor()
    req1="CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, namee TEXT NOT NULL, imatriculation TEXT NOT NULL)"
    cur.execute(req1)

    req2="INSERT INTO employee(namee,imatriculation) values (?,?)"
    cur.execute(req2,(vr_name,vr_imatriculation))
    conn.commit()
    conn.close()





root=Tk()


#ruls
#e=Entry(master,option ,.....)
Label(root,text="Name").grid(row=1,column=0)
Label(root,text="N° Immatriculation").grid(row=2,column=0)


name=Entry(root,width=40).grid(row=1,column=1)
imatriculation=Entry(root,width=40).grid(row=2,column=1)



Button(root,text="save",width=20,command=validate).grid(row=4,column=1)


root.mainloop()
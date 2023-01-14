#https://www.youtube.com/watch?v=clw6jvmAxjw
from tkinter import *

def validate():
    print(entryName.get(),entryEmail.get(),entryAge.get())
root=Tk()
root.geometry("600x400")
lblName=Label(root,text="Name :")
lblName.place(x=10,y=10)
entryName=Entry(root)
entryName.place(x=100,y=10,width=200)

lblEmail=Label(root,text="Email :")
lblEmail.place(x=10,y=40)
entryEmail=Entry(root)
entryEmail.place(x=100,y=40,width=200)

lblAge=Label(root,text="Age :")
lblAge.place(x=10,y=80)
entryAge=Entry(root)
entryAge.place(x=100,y=80,width=200)

valider=Button(text="valider",command=validate)
valider.place(x=100,y=120,width=200)
root.mainloop()
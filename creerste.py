from tkinter import *

app=Tk()
app.title("welcome")
app.geometry("600x500")

rs=Entry(app,width=40).pack()
ice=Entry(app,width=40).pack()
idf=Entry(app,width=40).pack()
typo=Entry(app,width=40).pack()
enrgistrer=Button(app,text="save").pack()

app.mainloop()
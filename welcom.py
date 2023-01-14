from tkinter import *

app=Tk()
app.title("welcome")
app.geometry("600x500")

count=0
def next():
    t=[2,5,9,7,6,3]
    for i in range(len(t)):
        if (i==i):
            print(t[i])
        
    

def ouvrirste():
    #========== label =============
    lbl_code=Label(text="code Ste").grid(row=0,column=0)
    #============ Entrys ==========
    code_ste=Entry().grid(row=0,column=1)

def creerste():
    #====== labels ================================
   lbl_nomSte=Label(text="raison social")
   lbl_nomSte.grid(row=0,column=0)
   lbl_activiteSte=Label(text="Activite ste ")
   lbl_activiteSte.grid(row=1,column=0)
   lbl_iceSte=Label(text="ICE")
   lbl_iceSte.grid(row=2,column=0)
   lbl_codeSte=Label(text="code Ste")
   lbl_codeSte.grid(row=3,column=0)

   #=============Entrys ============================
   nomSte= Entry()
   nomSte.grid(row=0,column=1)
   activiteSte=Entry()
   activiteSte.grid(row=1,column=1)
   iceSte=Entry()
   iceSte.grid(row=2,column=1)
   codeSte=Entry()
   codeSte.grid(row=3,column=1)
   btnCreate=Button(text="create",command=next)
   btnCreate.grid(row=4,column=1)
   
#===================== button =====================================
creer=Button(app,text="creer ste ou pp",command=creerste).grid(row=10,column=3)
ouvrir=Button(app,text="ouvrir ste ou pp",command=ouvrirste).grid(row=10,column=7)

app.mainloop()
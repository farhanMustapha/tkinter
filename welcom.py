from tkinter import *

app=Tk()
app.title("welcome")
app.geometry("600x500")

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
   nomSte= Entry().grid(row=0,column=1)
   activiteSte=Entry().grid(row=1,column=1)
   iceSte=Entry().grid(row=2,column=1)
   codeSte=Entry().grid(row=3,column=1)
   btnCreate=Button(text="create").grid(row=4,column=1)
   
#===================== button =====================================
creer=Button(app,text="creer ste ou pp",command=creerste).grid(row=10,column=3)
ouvrir=Button(app,text="ouvrir ste ou pp",command=ouvrirste).grid(row=10,column=7)

app.mainloop()
from tkinter import *

root=Tk()
mylist=["ahmed","ali","med"]
def newEploye():
    print("creer new")

def afficheAll():
    print(mylist)
item=""
def addEmploy(item):
    mylist.append(item)

item=Entry(root,width=40,textvariable=item).grid(row=9,column=3)
root.geometry('600x500')
save_button=Button(root,text="new employe",width=20,command=newEploye).grid(row=3,column=3)
show_button=Button(root,text="show all",width=20,command=afficheAll).grid(row=5,column=3)
add_button=Button(root,text="add",width=20,command=addEmploy).grid(row=7,column=3)





root.mainloop()

#https://www.youtube.com/watch?v=_Bt-P5xTFMs&t=658s
#https://www.youtube.com/watch?v=qP9-3LnMZsE&list=PLuXY3ddo_8nzUrgCyaX_WEIJljx_We-c1&index=2
#https://www.youtube.com/watch?v=9d5-Ti6onew
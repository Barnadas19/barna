# to do list in python 

import tkinter 

from tkinter import * 

root=Tk() 

root.title("To Do List") 

root.geometry("400x550+500+100") 

root.resizable(False,False) 

task_list=[] 

def addTask(): 

    task=task_entry.get() 

    task_entry.delete(0,END) 

    if task: 

        with open("tasklist.txt",'a') as taskfile: 

          taskfile.write(f"\n(task)") 

        task_list.append(task) 

        listbox.insert(END,task)  

def deleteTask(): 

    global task_list 

    task=str(listbox.get(ANCHOR)) 

    if task in task_list: 

        task_list.remove(task) 

        with open("tasklist.txt","w") as taskfile: 

          for task in task_list: 

                taskfile.write(task+"\n") 

        listbox.delete(ANCHOR) 

def openTaskFile(): 

    try: 

        global task_list 

        with open("tasklist.txt","r")as taskfile: 

            tasks= taskfile.readlines() 

        for task in tasks: 

          if task !='\n': 

             task_list.append(task) 

             listbox.insert(END,task) 

    except: 

     file=open('tasklist.txt','w') 

     file.close()

heading=Label(root,text="All TASK",font="arial 20 bold",fg="White",bg="light green") 

heading.place(x=130,y=20) 

frame=Frame(root,width=400,height=50,bg="White") 

frame.place(x=0,y=180) 

task=StringVar() 

task_entry=Entry(frame,width=18,font="Areal 20",bd=0,bg="sky blue") 

task_entry.place(x=10,y=7) 

task_entry.focus() 

button=Button(frame,text="ADD",font="Areal 20 bold",width=6,bg="orange",fg="grey",bd=0,command=addTask) 

button.place(x=300,y=0) 

frame1=Frame(root,bd=3,width=700,height=280,bg="yellow") 

frame1.pack(pady=(245,0)) 

listbox=Listbox(frame1,font=("areal",12),width=40,height=12,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff") 

listbox.pack(side=LEFT,fill=BOTH,padx=2) 

scrollbar=Scrollbar(frame1) 

scrollbar.pack(side=RIGHT,fill=BOTH) 

listbox.config(yscrollcommand=scrollbar.set) 

scrollbar.config(command=listbox.yview) 

openTaskFile() 

delete_button=Button(frame,text="DELETE",font="Areal 20 bold",width=6,bg="blue",fg="green",bd=0) 

Button(root,delete_button,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13) 

 

root.mainloop()

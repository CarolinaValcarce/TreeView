from tkinter import *
from tkinter import ttk

root=Tk()
root.title('Vista de tablas')
root.geometry('450x550')
root.config(bg='light slate grey')

Tree_frame=Frame(root)
Tree_frame.pack(pady=20)

Tree_Scroll=Scrollbar(Tree_frame)
Tree_Scroll.pack(side=RIGHT, fill=Y)

style=ttk.Style()
style.theme_use('clam')
style.configure('Treeview', background='silver', foreground='black', rowheigth=25, fieldbackground='silver')
style.map('Treeview', background=[('selected', 'light slate grey')])

mytree=ttk.Treeview(Tree_frame, yscrollcommand= Tree_Scroll.set)
mytree.pack()

Tree_Scroll.config(command=mytree.yview)
mytree.tag_configure('oddrow',background='#fedefb')
mytree.tag_configure('evenrow', background='#ffeaff')

mytree['columns']=('DNI', 'Nombre','Edad','Preferencia')

mytree.column ('#0', width=0, stretch=NO)
mytree.column ('#1',width=80, anchor=W)
mytree.column ('#2', width= 180, anchor=W)
mytree.column ('#3', width=40, anchor=CENTER)
mytree.column ('#4', width=100, anchor=W)

mytree.heading ('#0',text='')
mytree.heading ('#1', text='DNI', anchor=CENTER)
mytree.heading ('#2', text='Nombre', anchor=W)
mytree.heading ('#3', text='Edad', anchor=CENTER)
mytree.heading ('#4', text='Preferencia', anchor=W)

Data=[('12.788567-A', 'Pedro Gomez Saez', 43, 'Drama'),('12.965545-B','Ana Olmo Vazquez',24,'Ciencia Ficcion'),
      ('11.545767-S', 'Javier Velazquez Romero', 60, 'Comedia'),('11.999777-S', 'Marcos Garcia Garcia',33, 'Terror'),
      ('11.098878-A', 'Maria Perez Jimenez', 36, 'Accion'), ('19.555777-D', 'Antonio Gutierrez Olvido', 50, 'Drama'),
      ('12.788567-A', 'Pedro Gomez Saez', 43, 'Drama'),('12.965545-B','Ana Olmo Vazquez',24,'Ciencia Ficcion'),
      ('11.545767-S', 'Javier Velazquez Romero', 60, 'Comedia'),('11.999777-S', 'Marcos Garcia Garcia',33, 'Terror'),
      ('11.098878-A', 'Maria Perez Jimenez', 36, 'Accion'), ('19.555777-D', 'Antonio Gutierrez Olvido', 50, 'Drama') ]

count=0
for record in Data:
    if count%2==0: 
        mytree.insert(parent='', index=END, iid=count, text='', values=(record[0], record[1],record[2], record[3]),tags=('evenrow',))
    else:
        mytree.insert(parent='', index=END, iid=count, text='', values=(record[0], record[1],record[2], record[3]),tags=('oddrow',))
   
    count +=1

def save():
    global count
    if count%2==0: 
        mytree.insert(parent='', index=END, iid=count, text='', values=(DNI_e.get(), Name_e.get(), Age_e.get(), Preferences_e.get()),tags=('evenrow',))
    else:
        mytree.insert(parent='', index=END, iid=count, text='',values=(DNI_e.get(), Name_e.get(), Age_e.get(), Preferences_e.get()) ,tags=('oddrow',))

    DNI_e.delete(0, END)
    Name_e.delete(0, END)
    Age_e.delete(0, END)
    Preferences_e.delete(0, END)
    

def selected():
    
    records=mytree.item(mytree.selection(),'values')
    DNI_e.insert(0, records[0])
    Name_e.insert(0, records[1])
    Age_e.insert(0, records[2])
    Preferences_e.insert(0, records[3])
    
def update():
    
    mytree.item(mytree.selection(),values=(DNI_e.get(), Name_e.get(), Age_e.get(), Preferences_e.get()))
    
    DNI_e.delete(0, END)
    Name_e.delete(0, END)
    Age_e.delete(0, END)
    Preferences_e.delete(0, END)

def clear_one():
    mytree.delete(mytree.selection()[0])

def clear_many():
    for record in mytree.selection():
        mytree.delete(record)

def clear_all():
    for record in mytree.get_children():
        mytree.delete(record)

insertion_frame=Frame(root)
insertion_frame.pack(pady=10)

DNI_l=Label(insertion_frame, text='DNI: ').grid(row=0,column=0)
Name_l=Label(insertion_frame, text='Nombre: ').grid(row=0,column=1)
Age_l=Label(insertion_frame, text='Edad: ').grid(row=0,column=2)
Preferences_l=Label(insertion_frame, text='Preferencia: ').grid(row=0,column=3)

DNI_e=Entry(insertion_frame, width=15)
DNI_e.grid(row=1,column=0)
Name_e=Entry(insertion_frame, width=30)
Name_e.grid(row=1,column=1)
Age_e=Entry(insertion_frame, width=5)
Age_e.grid(row=1,column=2)
Preferences_e=Entry(insertion_frame, width=15)
Preferences_e.grid(row=1,column=3)

Button(root, text='Grabar registro', bd=5, command=save).pack()
Button(root, text='Seleccionar registro', bd=5, command=selected).pack()
Button(root, text='Actualizar registro', bd=5, command=update).pack()
Button (root, text='Borrar registro', bd=5, command=clear_one).pack()
Button (root, text='Borrar varios registros', bd=5, command=clear_many).pack()
Button (root, text= 'Borrar todos los registros', bd=5, command=clear_all).pack()



root.mainloop()

"""--------------CARLO ZAMBALDO---------------"""
"""---------LICEO GIROLAMO FRACASTORO---------"""
"""----CREATORE DI FILE (programma posti)-----"""
"""-------------------------------------------"""
"""------------VERSIONE 1.0.3 BETA------------"""
"""--------MODIFICATO IL 07 MARZO 2017--------"""
"""

"""

versione = "1.0.3 BETA"
datagg = "07 MAR 2017"

import __future__
import time

try:
    from tkinter import *
    import tkinter
    import tkinter.ttk as ttk
except ImportError:
    from Tkinter import *
    import Tkinter
    import ttk

##########################################################################

class creafile:

    def __init__(self):
        self.radice = Tk()
        self.radice.title("Crea file")
        self.radice.resizable(False, False)
        self.begin()

    def begin(self):
        self.menu = Frame(self.radice)
        
        Label(self.menu, text="Seleziona file:", fg = 'blue',font=('times', 16)).grid(row=0, column=0,stick = W)

        self.var = IntVar()
        self.c1 = Checkbutton(self.menu, text="NomiStudenti.txt", onvalue = 1, variable=self.var)
        self.c1.grid(row=1, column=0,stick = W)
        self.c2 = Checkbutton(self.menu, text="posti.txt", onvalue = 2, variable=self.var)
        self.c2.grid(row=2, column=0,stick = W)

        Label(self.menu, text="Classe (Classe+sezione):", fg = 'blue',font=('times', 16)).grid(row=3, column=0,stick = W)
        self.e2 = Entry(self.menu, width = 7, justify=CENTER)
        self.e2.grid(row=4, column=0, ipadx = 1)

        Button(self.menu, text = 'CREA', fg = 'blue', relief="groove", font=('times', 14), command = lambda: self.crea()).grid(row = 5, column = 0, stick = N)

        self.menu.pack()

    def crea(self):
        if (self.var.get()==1):
            self.dis=1
            self.NS(str(self.e2.get()))
        if (self.var.get()==2):
            exec(open("posti v.4 BETA.py").read(), globals())


    def NS(self, cl): #crea file nomi con lista: aggiungi studenti ad una lista poi premi crea e la crea con la sintassi
        self.menu.destroy()
        self.NSADD = Frame(self.radice)
        
        Label(self.NSADD, text="Nome: ", fg = 'black',font=('times', 16)).grid(row=0, column=0,stick = E)
        self.e1 = Entry(self.NSADD, textvariable=1)
        self.e1.grid(row=0, column=1, ipadx = 1)

        Button(self.NSADD, text = 'ADD', fg = 'blue', relief="groove", font=('times', 14),command = lambda: self.add(cl)).grid(row = 0, column = 3, stick = W)
        
        self.NSADD.pack()
        self.add(cl)

    def add(self, cl):
        try:
            self.agg.destroy()
        except:
            self.Lista=''
            print("Inizializzo")
        if(str(self.e1.get())!=''):
            self.Lista=self.Lista+str(self.e1.get())+"."
            print(self.Lista)
        self.e1.delete(0, last=1000)

        self.agg = Frame(self.radice)
              
        scrollbar = Scrollbar(self.agg)
        self.mylist = Listbox(self.agg, yscrollcommand = scrollbar.set)
        g = self.Lista.split(".")
        for i in range (0,len(g)-1):
            self.mylist.insert(i, str(i+1)+" - "+g[i])
            self.mylist.grid(row = 0, column = 1, stick = W)
        scrollbar.grid(row = 0, column = 2, sticky=N+S)
        scrollbar.config(command = self.mylist.yview)

        Button(self.agg, text = 'SICURA', fg = 'red', relief="groove", font=('times', 13),command = lambda: self.enable()).grid(row = 1, column = 0, stick = W)
        
        self.crea = Button(self.agg, state=DISABLED, text = 'CREA IL FILE', fg = 'blue', relief="groove", font=('times', 16),command = lambda: self.print(cl))
        self.crea.grid(row = 1, column = 1, stick = W)
        Button(self.agg, text = 'RESET', fg = 'red', relief="groove", font=('times', 14),command = lambda: self.inizialize(cl)).grid(row = 0, column = 3, stick = E)
        Button(self.agg, text = 'DEL', fg = 'red', relief="groove", font=('times', 15),command = lambda: self.delate(cl)).grid(row = 1, column = 3, stick = E)
        self.agg.pack()

    def enable (self):
        if self.dis==1:
            self.crea.config(state=NORMAL)
            self.dis=0
        else:
            self.crea.config(state=DISABLED)
            self.dis=1

    def delate(self, cl):
        print((self.mylist.curselection()))
        numero = self.Lista.split(".")
        print(self.Lista)
        print(str(numero[self.mylist.curselection()[0]]))
        numero.remove(str(numero[self.mylist.curselection()[0]]))
        print(numero)
        z=0
        self.Lista=''
        for k in range(0,len(numero)-1):
           try:
               self.Lista+=str(numero[z])+"."
               print(self.Lista)
           except IndexError:
               break
           z+=1
        self.add(cl)
    
    def inizialize(self, cl):
        self.Lista=''
        self.add(cl)
        
    def print(self, cl):
        out_file = open("NomiStudenti_"+cl+".txt","w")
        out_file.write(str(self.Lista))
        out_file.write("\n\n!- READ THE README.txt FILE BEFORE APPLYING CHANGES TO THIS FILE -!\n\n")
        out_file.write("Created on: "+time.strftime("%d/%m/%Y")+" at "+time.strftime("%H:%M:%S"))
        out_file.close()
    
    def M_loop(self):
        self.radice.mainloop()
        
###################################################################

if __name__ == '__main__':
    test = creafile()
    test.M_loop()

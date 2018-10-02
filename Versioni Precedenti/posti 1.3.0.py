"""--------------CARLO ZAMBALDO---------------"""
"""-----------PROGRAMMA-PER-I-POSTI-----------"""

import __future__
#import tkMessageBox
import random
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

##############################################################################################################

def INT():
    global e1, e2, e3, page
    page = Tk()
    page.title("Crea posti 1.3.0")

    Label(page, text="Numero studenti: ", fg = 'blue',font=('times', 16)).grid(row=0, column=0,stick = E)
    Label(page, text="Numero di banchi per fila: ", fg = 'blue',font=('times', 16)).grid(row=1, column=0,stick = E)
    Label(page, text="Numero di file: ", fg = 'blue',font=('times', 16)).grid(row=2, column=0,stick = E)

    e1 = Entry(page)
    e2 = Entry(page)
    e3 = Entry(page)

    e1.grid(row=0, column=1, ipadx = 1)
    e2.grid(row=1, column=1, ipadx = 1)
    e3.grid(row=2, column=1, ipadx = 1)

    pulsante_next = Button(page, text = 'NEXT', fg = 'black',font=('times', 16),command = avanti).grid(row = 3, column = 0, stick = W)
    Button(page, text = 'EXIT', fg = 'black',font=('times', 16),command = page.destroy).grid(row = 3, column = 1, stick = W)
    page.mainloop()

#########################################################################################################

def GUI():
    global pag
    pag = Tk()
    x=0
    y=0
    z=0
    if (f*bpf < alunni):
        """tkMessageBox.showerror("ERROR","!-BANCHI INSUFFICIENTI PER "+str(alunni)+" ALUNNI-!")"""
        Label(pag, text="!-BANCHI INSUFFICIENTI PER "+str(alunni)+" ALUNNI-!", fg = 'red', font=('times', 30)).grid(row=0, column=0)
    else:
        for x in range(0,f):
            for y in range(0,bpf):
                try:
                    Label(pag, text=((numero[z])+"  "), fg = 'black', font=('times', 50, 'italic')).grid(row=x, column=y)
                except IndexError:
                    break
                z+=1

    Button(pag, text = 'EXIT', fg = 'red',font=('times', 13),command = pag.destroy).grid(row = x+1, column = y, stick = W)
    Button(pag, text = 'BACK', fg = 'blue',font=('times', 13),command = indietro).grid(row = x+1, column = y+1, stick = W)
    pag.mainloop()

###############################################################################################################

def indietro():
    pag.destroy()
    INT()

###############################################################################################################

def avanti():
    global numero, alunni, bpf, f
    try:
        alunni = int(e1.get())
        f = int(e3.get())
        bpf = int(e2.get())

        print("studenti inseriti: ",alunni)
        print("banchi per fila inseriti: ",bpf)
        print("file inserite: ",f)

    except ValueError:
        print("ValueError: inserire i dati in tutti i campi.")
        alunni = 0
        f = 0
        bpf = 0


    posto = ''
    numero = ''

    for i in range(1,alunni):
        numero = numero+str(i)+'.'

    numero = numero+str(alunni)
    numero = numero.split('.')
    random.shuffle(numero)

    page.destroy()
    GUI()

#####################################################################################################################

INT()

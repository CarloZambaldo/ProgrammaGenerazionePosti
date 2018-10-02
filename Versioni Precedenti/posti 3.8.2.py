"""--------------CARLO ZAMBALDO---------------"""
"""---------LICEO GIROLAMO FRACASTORO---------"""
"""-----------PROGRAMMA PER I POSTI-----------"""
"""-------------------------------------------"""
"""--------------VERSIONE 3.8.2---------------"""
"""------MODIFICATO IL 16 FEBBRAIO 2017-------"""
"""

Programma che crea a random i posti,
   input necessari: - Numero studenti
                    - Banchi per fila
                    - Numero di file
                    
    funzioni aggiuntive: - Crea un documento .txt per salvare una disposizione
                         - Legge il documento creato (ne ridisegna la disposizione)
                         - Bottone info per conoscere la versione, data aggiornamento e mail del programmatore
                         - Converte i numeri identificativi con il nome degli studenti
                         - Decidere quante volte mescolare a random (Inutile, ma fa scena ahah)

 !-Nota Bene-!
   Il file txt creato con la versione precedente viene letto normalmente anche da questa versione.

"""

versione = "3.8.2"
datagg = "16 FEB 2017"

import __future__
import time

import random
try:
    from tkinter import *
    import tkinter
    import tkinter.ttk as ttk
except ImportError:
    from Tkinter import *
    import Tkinter
    import ttk

##########################################################################

class posti:

    def __init__(self):
        self.radice = Tk()
        self.radice.title("Crea posti "+versione)
        self.radice.resizable(False, False)
        self.begin()

    def begin(self):
        self.menu = Frame(self.radice)

        Label(self.menu, text="Numero studenti: ", fg = 'blue',font=('times', 16)).grid(row=0, column=0,stick = E)
        Label(self.menu, text="Numero di banchi per fila: ", fg = 'blue',font=('times', 16)).grid(row=1, column=0,stick = E)
        Label(self.menu, text="Numero di file: ", fg = 'blue',font=('times', 16)).grid(row=2, column=0,stick = E)
        Label(self.menu, text="File posti.txt gia' creato?", fg = 'green',font=('times', 16)).grid(row=3, column=0,stick = E)
        Label(self.menu, text="Quanto mescolo?", fg = 'black',font=('times', 16)).grid(row=4, column=0,stick = E)

        self.e1 = Entry(self.menu)
        self.e2 = Entry(self.menu)
        self.e3 = Entry(self.menu)
        self.e1.grid(row=0, column=1, ipadx = 1)
        self.e2.grid(row=1, column=1, ipadx = 1)
        self.e3.grid(row=2, column=1, ipadx = 1)

        Button(self.menu, text = 'OPEN FILE', fg = 'black', relief="groove",font=('times', 14),command = lambda: self.aprifile()).grid(row = 3, column = 1, stick = W)
        Button(self.menu, text = 'NEXT', fg = 'black', relief="groove",font=('times', 16, "bold"),command = lambda: self.avanti()).grid(row = 5, column = 0, stick = W)
        Button(self.menu, text = 'INFO', fg = 'blue', relief="groove", font=('times', 14, "bold"),command = lambda: self.info()).grid(row = 5, column = 1, stick = W)
        Button(self.menu, text = 'EXIT', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.radice.destroy()).grid(row = 5, column = 2, stick = W)

        self.scale = Scale(self.menu, from_=0, to=10, orient=HORIZONTAL)
        self.scale.set(5)
        self.scale.grid(row=4, column=1, ipadx = 30, stick = W)

#####################

        filemenu = Menu(self.menu, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as...")
        filemenu.add_command(label="Close")

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.radice.quit)
        



##############################
        
        self.menu.pack()
    
    def avanti(self):
        try: 
            self.inff.destroy()
        except:
            pass
        try:
            alunni = int(self.e1.get())
            f = int(self.e3.get())
            bpf = int(self.e2.get())
            val = int(self.scale.get())
            print("Studenti inseriti: ",alunni)
            print("Banchi per fila inseriti: ",bpf)
            print("File inserite: ",f)

            if(alunni>50):
                self.exeeded()
            elif (f*bpf < alunni):
                self.insuff(alunni)
            else:
                self.algo(alunni, f, bpf, val)

        except ValueError:
            print("ValueError: inserire i dati in tutti i campi.")
            alunni = 0
            f = 0
            bpf = 0

    def exeeded(self):
        self.exeed = Tk()
        self.exeed.title("Errore 01")
        self.exeed.resizable(False, False)
        Label(self.exeed, text="Troppi studenti per essere visualizzati.", fg = 'red', font=('times', 30)).grid(row=0, column=0)

    def insuff(self, alunni):
        self.ins = Tk()
        self.ins.title("Errore 02")
        self.ins.resizable(False, False)
        Label(self.ins, text="!-BANCHI INSUFFICIENTI PER "+str(alunni)+" ALUNNI-!", fg = 'red', font=('times', 30)).grid(row=0, column=0)
        print("Banchi insufficienti.\nIl numero dei banchi e' dato dal prodotto delle file con i banchi per fila.")

    def algo(self, alunni, f, bpf, val):
        self.menu.destroy() 
        numero = list(range(1,alunni+1))
        for ciao in range(1,val):
            random.shuffle(numero)
        self.GUI(alunni, f, bpf, numero)
      
    def GUI(self, alunni, f, bpf, numero):
        self.pag = Frame(self.radice)
        self.radice.title("Crea posti (v."+versione+")")
        k=0
        u=0
        z=0
        try:
            (int(numero[0]))
            car=50
        except:
            car=25

        for k in range(0,f):
            for u in range(0,bpf):
                try:
                    Label(self.pag, text=(str(numero[z])+"  "), fg = 'black', font=('times', car, 'italic')).grid(row=k, column=u)
                except IndexError:
                    break
                z+=1
        Label(self.pag, text=("PROF"), fg = 'black', font=('times', 15, 'italic')).grid(row=k+1, column=int(bpf/2))
            
        Button(self.pag, text = 'BACK', fg = 'blue', relief="groove", font=('times', 16, "bold"),command = lambda: self.indietro()).grid(row = k+2, column = 0, stick = W)
        Button(self.pag, text = 'CREA .txt', fg = 'green', relief="groove", font=('times', 16, "bold"),command = lambda: self.sicurezza(f, bpf, numero)).grid(row = k+2, column = 1, stick = W) 
        Button(self.pag, text = 'RESET', fg = 'blue', relief="groove", font=('times', 16, "bold"),command = lambda: self.reset(alunni, f, bpf)).grid(row = k+2, column = 2, stick = W)
        Button(self.pag, text = 'NUaNO', fg = 'blue', relief="groove", font=('times', 16, "bold"),command = lambda: self.changeToN(numero, alunni, f, bpf)).grid(row = k+2, column =3, stick = W)
        Button(self.pag, text = 'EXIT', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.radice.destroy()).grid(row = k+2, column = 4, stick = W)
        self.pag.pack()

    def changeToN(self, numero, alunni, f, bpf):
        try:
            self.sicu.destroy()
            filenomi = open("NomiStudenti.txt","r")
            nommi = filenomi.readline()
            sostituta = numero
            nomivari = nommi.split(".")
            provv = numero
            for vari in range(0,len(sostituta)):
                try:
                    val = int(provv[vari])
                    numero[vari] = nomivari[val-1]
                except IndexError:
                    break
            filenomi.close()
        except:
            print("Impossibile convertire con i nomi degli studenti!\nAssicurarsi che il file NomiStudenti.txt sia scritto correttamente.")
        self.pag.destroy()
        self.GUI(alunni, f, bpf, numero)

    def sicurezza(self, f, bpf, numero):
        self.sicu = Frame(self.radice)

        Label(self.sicu, text="Nome utente: ", fg = 'blue',font=('times', 16)).grid(row=0, column=0,stick = E)
        Label(self.sicu, text="Password: ", fg = 'blue',font=('times', 16)).grid(row=1, column=0,stick = E)
      
        self.nome = Entry(self.sicu)
        self.passw = Entry(self.sicu, show="*")
        self.nome.grid(row=0, column=1, ipadx = 1)
        self.passw.grid(row=1, column=1, ipadx = 1)
     
        Button(self.sicu, text = 'CREA', fg = 'green', relief="groove",font=('times', 16, "bold"),command = lambda: self.nuofile(f, bpf, numero)).grid(row = 4, column = 0, stick = W)
        Button(self.sicu, text = 'CANCEL', fg = 'red', relief="groove", font=('times', 14, "bold"),command = lambda: self.sicu.destroy()).grid(row = 4, column = 1, stick = W)

        self.menu.destroy()
        self.sicu.pack()
    
    def nuofile(self, f, bpf, numero):
        NU = str(self.nome.get())
        PSW = str(self.passw.get())
        if ((PSW=="confermo")or(PSW=="ok")):
            try:
                out_file = open("posti.txt","w")
                k=0
                u=0
                z=0
                for k in range(0,f):
                    for u in range(0,bpf):
                       try:
                           out_file.write((str(numero[z]))+".")
                       except IndexError:
                           break
                       z+=1
                out_file.write(str(f)+"."+str(bpf))
                out_file.write("\n\n-! DO NOT CHANGE THIS FILE !-\n\n")
                out_file.write("Created on: "+time.strftime("%d/%m/%Y")+" at "+time.strftime("%H:%M:%S")+" by "+NU)
                out_file.close()
                print("Salvata la disposizione come posti.txt")
            except:
                print("Impossibile creare il file.")
            self.sicu.destroy()
    
    def aprifile(self):
        try:
            self.menu.destroy()
        except:
            pass
        print("Aprendo il file...")
        try:
            in_file = open("posti.txt","r")
            text = in_file.readline()
            numero = text.split(".")
            alunni = (len(numero))-2
            f = int(numero[alunni])
            bpf = int(numero[alunni+1])
            numero = numero[:alunni]
            self.menu.destroy()
            try: 
                self.inff.destroy()
            except:
                pass
            self.GUI(alunni, f, bpf, numero)
            print("Apertura avvenuta con successo!")
        except:
            print("Impossibile aprire il file.")

    def indietro(self):
        try:
            self.sicu.destroy()
        except:
            pass
        self.pag.destroy()
        self.begin()

    def reset(self, alunni, f, bpf):
        self.pag.destroy()
        try:
            self.sicu.destroy()
        except:
            pass
        val=100
        self.algo(alunni, f, bpf, val)

    def info(self):
        self.inff = Tk()
        self.inff.title("INFO v."+versione)
        self.inff.resizable(False, False)
        self.informa = Frame(self.inff)
        Label(self.informa, text="Versione: ", fg = 'blue',font=('times', 16)).grid(row=1, column=0,stick = E)
        Label(self.informa, text=versione, fg = 'black',font=('times', 16)).grid(row=1, column=1,stick = W)
        Label(self.informa, text="Data aggiornamento: ", fg = 'blue',font=('times', 16)).grid(row=2, column=0,stick = E)
        Label(self.informa, text=datagg, fg = 'black',font=('times', 16)).grid(row=2, column=1,stick = W)
        Label(self.informa, text="Mail sviluppatore: ", fg = 'blue',font=('times', 16)).grid(row=3, column=0,stick = E)
        Label(self.informa, text="carlo.zambaldo@gmail.com", fg = 'black',font=('times', 16)).grid(row=3, column=1,stick = W)
        self.informa.pack()

    def M_loop(self):
        self.radice.mainloop()

"""
    def Wait(self):
        self.aspe = Frame(self.radice)
        Label(self.aspe, text="Please wait...", fg = 'white',font=('times', 18)).grid(row=0, column=0,stick = W)
"""

###################################################################

if __name__ == '__main__':
    test = posti()
    test.M_loop()

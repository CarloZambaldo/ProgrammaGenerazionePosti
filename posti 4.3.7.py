"""--------------CARLO ZAMBALDO---------------"""
"""---------LICEO GIROLAMO FRACASTORO---------"""
"""-----------PROGRAMMA PER I POSTI-----------"""
"""-------------------------------------------"""
"""---------------VERSIONE 4.3.7--------------"""
"""--------MODIFICATO IL 13 MARZO 2017--------"""
"""

Programma che crea a random i posti,
   input necessari: - Numero studenti
                    - Banchi per fila
                    - Numero di file
                    
   funzioni aggiuntive: - Crea un documento .txt per salvare una disposizione
                        - Legge il documento creato (ne ridisegna la disposizione)
                        - Bottone info per conoscere la versione, data aggiornamento e mail del programmatore
                        - Converte i numeri identificativi con il nome degli studenti
                        - Decidere quante volte mescolare a random (da 0 a 10)
                        - Mostra una finestra di avviso come gestione ad errori
                 (BETA) - Possibilita' di aggiungere una condizione (es. studente1 non puo' essere vicino a studente2)
   		        - Le finestre degli errori si chiudono automaticamente
			- Possibilita' di inserire la classe per leggere il file NomiStudenti.txt corretto (Leggi README.txt per maggiori info)
                        
"""

versione = "4.3.7"
datagg = "13 MAR 2017"

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

        # RICHIESTA DATI FONDAMENTALI
        Label(self.menu, text="Numero studenti: ", fg = 'blue',font=('times', 16)).grid(row=0, column=0,stick = E)
        Label(self.menu, text="Numero di banchi per fila: ", fg = 'blue',font=('times', 16)).grid(row=1, column=0,stick = E)
        Label(self.menu, text="Numero di file: ", fg = 'blue',font=('times', 16)).grid(row=2, column=0,stick = E)
        self.e1 = Entry(self.menu, textvariable=5, width = 10, justify=CENTER)
        self.e2 = Entry(self.menu, textvariable=2, width = 10, justify=CENTER)
        self.e3 = Entry(self.menu, textvariable=3, width = 10, justify=CENTER)
        self.e1.grid(row=0, column=1, ipadx = 1, stick = W)
        self.e2.grid(row=1, column=1, ipadx = 1, stick = W)
        self.e3.grid(row=2, column=1, ipadx = 1, stick = W)

        # CONDIZIONE DI DISPOSIZIONE
        self.e = 1
        self.CHKEN = Checkbutton(self.menu, text='Enable',  fg = 'black',font=('times', 15), variable=self.e, command= lambda: self.enab())
        self.CHKEN.grid(row=5, column=0,stick = E)
        self.Condizione = Button(self.menu, text = 'Condizione', state=DISABLED, fg = 'black', relief="groove",font=('times', 15),command = lambda: self.ADV())
        self.Condizione.grid(row = 5, column = 1)
        
        # FILE GIA' CREATO
        Label(self.menu, text="File posti.txt gia' creato?", fg = 'green',font=('times', 16)).grid(row=4, column=0,stick = E)
        Button(self.menu, text = 'OPEN FILE', fg = 'black', relief="groove",font=('times', 14),command = lambda: self.aprifile()).grid(row = 4, column = 1, stick = W)

        # BOTTONI FONDO
        Button(self.menu, text = 'GENERA', fg = 'blue', relief="groove",font=('times', 17, "bold"),command = lambda: self.avanti()).grid(row = 6, column = 0)
        Button(self.menu, text = 'HELP', fg = 'black', relief="groove", font=('times', 14),command = lambda: self.info()).grid(row = 6, column = 1)

        # OPZIONE QUANTO MESCOLA
        Label(self.menu, text="Quanto mescolo?", fg = 'black',font=('times', 16)).grid(row=3, column=0,stick = E+S)
        self.scale = Scale(self.menu, from_=0, to=10, orient=HORIZONTAL, length = 30)
        self.scale.set(5)
        self.scale.grid(row=3, column=1, ipadx = 30, stick = W)

        self.menu.pack()

    def enab(self):
        if(self.e==1):
            self.Condizione.config(state=NORMAL)
            self.e=0
        else:
            self.Condizione.config(state=DISABLED)
            self.e=1
            try:
                self.ADVANCED.destroy()
            except:
                pass
    
    def ADV(self):
        try:
            self.ADVANCED.destroy()
        except:
            pass
        self.ADVANCED = Frame(self.radice)
        Label(self.ADVANCED, text="Condizione:", fg = 'black',font=('times', 16)).grid(row=0, column=0,stick = E)
        self.A1 = Entry(self.ADVANCED, textvariable=4, width = 10, justify=CENTER)
        self.A1.grid(row=0, column=1, ipadx = 1)
        Button(self.ADVANCED, text = 'CANCEL', fg = 'red', relief="groove",font=('times', 13, "bold"),command = lambda: self.chiudoADV()).grid(row = 0, column = 2, stick = W)
        self.ADVANCED.pack()

    def chiudoADV(self):
        self.ADVANCED.destroy()
        self.e=0
        self.Condizione.config(state=DISABLED)
        
    def avanti(self):
        self.trytoclose()
        try:
            alunni = int(self.e1.get())
            f = int(self.e3.get())
            bpf = int(self.e2.get())
            val = int(self.scale.get())

            if(alunni>50):
                self.exeeded()
            elif (f*bpf < alunni):
                self.insuff(alunni)
            else:
                self.CHKEN.deselect()
                self.algo(alunni, f, bpf, val)
        except ValueError:
            self.ValueERR()
            alunni = 0
            f = 0
            bpf = 0

### ERRORI

    def exeeded(self):
        try:
            self.exeed.destroy()
        except:
            pass
        self.exeed = Tk()
        self.exeed.title("Errore 01")
        self.exeed.resizable(False, False)
        Label(self.exeed, text="Troppi studenti per essere visualizzati.", fg = 'red', font=('times', 30)).grid(row=0, column=0)
        Button(self.exeed, text = 'OK', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.exeed.destroy()).grid(row = 1, column = 0, stick = W)
        self.exeed.update()
        self.exeed.after(3600, lambda: self.exeed.destroy())

    def insuff(self, alunni):
        try:
            self.ins.destroy()
        except:
            pass
        self.ins = Tk()
        self.ins.title("Errore 02")
        self.ins.resizable(False, False)
        Label(self.ins, text="Banchi insufficienti per "+str(alunni)+" alunni.", fg = 'red', font=('times', 30)).grid(row=0, column=0)
        Button(self.ins, text = 'OK', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.ins.destroy()).grid(row = 1, column = 0, stick = W)
        self.ins.update()
        self.ins.after(3600, lambda: self.ins.destroy())
        
    def ValueERR(self):
        try:
            self.VE.destroy()
        except:
            pass
        self.VE = Tk()
        self.VE.title("Errore 03")
        self.VE.resizable(False, False)
        Label(self.VE, text="Inserire i dati in tutti i campi.", fg = 'red', font=('times', 30)).grid(row=0, column=0)
        Button(self.VE, text = 'OK', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.VE.destroy()).grid(row = 1, column = 0, stick = W)
        self.VE.update()
        self.VE.after(3600, lambda: self.VE.destroy())
        
        
    def NOaNUERR(self):
        try:
            self.NUE.destroy()
        except:
            pass
        self.NUE = Tk()
        self.NUE.title("Errore 04")
        self.NUE.resizable(False, False)
        Label(self.NUE, text="Errore durante la traduzione.", fg = 'red', font=('times', 30)).grid(row=0, column=0)
        Button(self.NUE, text = 'OK', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.NUE.destroy()).grid(row = 1, column = 1, stick = W)
        Button(self.NUE, text = 'Controlla file NomiStudenti.txt', fg = 'blue', relief="groove",font=('times', 16, "bold"),command = lambda: self.OpenAll()).grid(row = 1, column = 0, stick = W)
        self.NUE.update()
        self.NUE.after(3600, lambda: self.NUE.destroy())
        
    def IMPCRE(self):
        try:
            self.IC.destroy()
        except:
            pass
        self.IC = Tk()
        self.IC.title("Errore 05")
        self.IC.resizable(False, False)
        Label(self.IC, text="Errore durante la creazione del file.", fg = 'red', font=('times', 30)).grid(row=0, column=0)
        Button(self.IC, text = 'OK', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.IC.destroy()).grid(row = 1, column = 1, stick = W)  
        self.IC.update()
        self.IC.after(3600, lambda: self.IC.destroy())
        
    def IMPAPR(self):
        try:
            self.IA.destroy()
        except:
            pass
        self.IA = Tk()
        self.IA.title("Errore 06")
        self.IA.resizable(False, False)
        Label(self.IA, text="Errore durante l'apertura del file.", fg = 'red', font=('times', 30)).grid(row=0, column=0)
        Button(self.IA, text = 'OK', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.IA.destroy()).grid(row = 1, column = 1, stick = W)  
        self.IA.update()
        self.IA.after(3600, lambda: self.IA.destroy())
        self.begin()

    def CREAVV(self, NU):
        try:
            self.CREATA.destroy()
        except:
            pass
        self.CREATA = Tk()
        self.CREATA.title("Creato posti.txt")
        self.CREATA.resizable(False, False)
        Label(self.CREATA, text="File posti.txt creato con successo", fg = 'green', font=('times', 25)).grid(row=0, column=0)
        Label(self.CREATA, text="By: "+NU+", on: "+time.strftime("%d/%m/%Y")+", at "+time.strftime("%H:%M:%S"), fg = 'black', font=('times', 18)).grid(row=1, column=0)
        Button(self.CREATA, text = 'OK', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.CREATA.destroy()).grid(row = 2, column = 1, stick = W)  
        self.CREATA.update()
        self.CREATA.after(10000, lambda: self.CREATA.destroy())

    def PSERR(self):
        try:
            self.PASS.destroy()
        except:
            pass
        self.PASS = Tk()
        self.PASS.title("Errore 07")
        self.PASS.resizable(False, False)
        Label(self.PASS, text="Password errata", fg = 'black', font=('times', 30)).grid(row=0, column=0)
        Button(self.PASS, text = 'OK', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: self.PASS.destroy()).grid(row = 0, column = 1, stick = W)  
        self.PASS.update()
        self.PASS.after(1000, lambda: self.PASS.destroy())
        
#######
    ##### ALGORITMO DELLA DISPOSOIZIONE RANDOM
        
    def algo(self, alunni, f, bpf, val):
        self.menu.destroy()
        try:
            cond1=str(self.A1.get())
            CO = cond1.split(".")
        except:
            pass
        numero = list(range(1,alunni+1))
        for ciao in range(0,val):
            random.shuffle(numero)
            try: ### CONDIZIONI DISPOSIZIONE
                for chk in range(0,alunni):
                    CO0=int(CO[0])
                    CO1=int(CO[1])
                    while((int(numero[chk])==CO0)and((int(numero[chk+1])==CO1)or(int(numero[chk-1])==CO1)))or((int(numero[chk])==CO1)and((int(numero[chk+1])==CO0)or(int(numero[chk-1])==CO0))):
                        random.shuffle(numero)
            except:
                pass
        try:
            self.ADVANCED.destroy()
        except:
            pass
        self.GUI(alunni, f, bpf, numero)

##########
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
            car=22
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
        Button(self.pag, text = 'NUaNO', fg = 'blue', relief="groove", font=('times', 16, "bold"),command = lambda: self.CLASSE(numero, alunni, f, bpf)).grid(row = k+2, column =3, stick = W)
        Button(self.pag, text = 'EXIT', fg = 'red', relief="groove",font=('times', 16, "bold"),command = lambda: quit()).grid(row = k+2, column = 4, stick = W)
        self.pag.pack()

    def CLASSE (self, numero, alunni, f, bpf):
        try:
            self.filenomi = open("NomiStudenti.txt","r")
            self.pross(numero, alunni, f, bpf)
        except:
            self.ok = Frame(self.radice)
            self.radice.title("Crea posti (v."+versione+")")

            Label(self.ok, text="Classe: ", fg = 'blue',font=('times', 16)).grid(row=0, column=0,stick = E)

            self.es = Entry(self.ok, width = 7, justify=CENTER)
            self.es.grid(row=0, column=1, ipadx = 1)
            
            Button(self.ok, text = 'Continua', fg = 'blue', relief="groove", font=('times', 16, "bold"),command = lambda: self.pross(numero, alunni, f, bpf)).grid(row = 1, column = 1, stick = W)
            self.ok.pack()
        
    def pross(self, numero, alunni, f, bpf):
        try:
            self.filenomi = open("NomiStudenti_"+str(self.es.get())+".txt","r")
        except:
            pass
        self.changeToN(numero, alunni, f, bpf)
         
    def changeToN(self, numero, alunni, f, bpf):
        self.trytoclose()
        try:
            nommi = self.filenomi.readline()
            nomivari = nommi.split(".")
            provv = numero
            for vari in range(0,len(provv)):
                try:
                    val = int(provv[vari])
                    numero[vari] = nomivari[val-1]
                except IndexError:
                    break
            self.filenomi.close()
        except:
            self.NOaNUERR()
        self.pag.destroy()
        self.GUI(alunni, f, bpf, numero)

##### CREAZIONE DI UN NUOVO FILE

    def sicurezza(self, f, bpf, numero):
        self.trytoclose()
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
                self.CREAVV(NU)
            except:
                self.IMPCRE()
            self.sicu.destroy()
        else:
            self.PSERR()

########## APERTURA DI UN FILE GIA' CREATO
    
    def aprifile(self):
        try:
            self.ADVANCED.destroy()
        except:
            pass
        try:
            self.CHKEN.deselect()
            in_file = open("posti.txt","r")
            text = in_file.readline()
            numero = text.split(".")
            alunni = (len(numero))-2
            f = int(numero[alunni])
            bpf = int(numero[alunni+1])
            numero = numero[:alunni]
            self.trytoclose()
            self.menu.destroy()
            self.GUI(alunni, f, bpf, numero)
        except:
            self.IMPAPR()

###########

    def indietro(self):
        self.trytoclose()
        self.pag.destroy()
        self.begin()

    def reset(self, alunni, f, bpf):
        self.pag.destroy()
        try:
            self.sicu.destroy()
        except:
            pass
        val=5
        self.algo(alunni, f, bpf, val)

    def info(self):
        self.trytoclose()
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
        Label(self.informa, text="ReadMe file: ", fg = 'blue',font=('times', 16)).grid(row=4, column=0,stick = E)
        Button(self.informa, text = 'ReadMe.txt', fg = 'black', relief="groove", font=('times', 16, "bold"), command = lambda: self.readme()).grid(row = 4, column = 1, stick = W)
        Label(self.informa, text="Files (debug): ", fg = 'blue',font=('times', 16)).grid(row=5, column=0,stick = E)
        Button(self.informa, text = 'Open all', fg = 'black', relief="groove", font=('times', 16, "bold"), command = lambda: self.OpenAll()).grid(row = 5, column = 1, stick = W)
        self.informa.pack()

    def readme(self):
        self.trytoclose()
        self.RM = Tk()
        self.RM.title("ReadMe v."+versione)
        self.RM.resizable(False, False)
        self.ReadMee = Frame(self.RM)
        try:
            ReadMe = open("README.txt","r")
            testo = ReadMe.read()
            ReadMe.close()
            Label(self.ReadMee, text=str(testo), fg = 'black',font=('times', 15)).grid(row=0, column=0,stick = E)
        except:
            Label(self.ReadMee, text="File inesistente.", fg = 'red',font=('times', 30)).grid(row=0, column=0,stick = E)
        self.ReadMee.pack()
            

    def OpenAll(self):
        self.trytoclose()
        self.OA = Tk()
        self.OA.title("All Files")
        self.OA.resizable(False, False)

        self.Studenti = Frame(self.OA)
        Label(self.Studenti, text="File NomiStudenti.txt:", fg = 'Red',font=('times', 16)).grid(row=0, column=0,stick = N)
        try:
            Nomi = open("NomiStudenti.txt","r")
            StudentiText = Nomi.read()
            Nomi.close()
            text1 = Text(self.Studenti, height=10)
            text1.insert(INSERT,str(StudentiText))
            text1.grid(row=1, column=0,stick = E)
        except:
            Label(self.Studenti, text="File inesistente.", fg = 'black',font=('times', 15)).grid(row=1, column=0,stick = N)
            #try:
            #    Button(self.Studenti, text = 'Crea File', fg = 'blue', relief="groove", font=('times', 15, "bold"), command = lambda: exec(open("CreaFile.py").read(), globals())).grid(row=2, column =0, stick = N)
            #except:
            #    pass
        self.Studenti.pack()
        
        self.Disposizione = Frame(self.OA)
        Label(self.Disposizione, text="File posti.txt:", fg = 'Red',font=('times', 16)).grid(row=0, column=0,stick = N)
        try:
            Posti = open("posti.txt","r")
            PostiText = Posti.read()
            Posti.close()
            text2 = Text(self.Disposizione, height=10)
            text2.insert(INSERT,str(PostiText))
            text2.grid(row=1, column=0,stick = E)
        except:
            Label(self.Disposizione, text="File inesistente.", fg = 'black',font=('times', 15)).grid(row=1, column=0,stick = N)
        self.Disposizione.pack()
        
        self.CloseAll = Frame(self.OA)
        Button(self.CloseAll, text = 'Close All', fg = 'blue', relief="groove", font=('times', 16, "bold"), command = lambda: self.trytoclose()).grid(row =0, column =0, stick = N)
        self.CloseAll.pack()
            
    def M_loop(self):
        self.radice.mainloop()

    def trytoclose(self):
        try: 
            self.CloseAll.destroy()
            self.OA.destroy()
        except:
            pass
        try: 
            self.inff.destroy()
        except:
            pass
        try:
            self.sicu.destroy()
        except:
            pass
        try:
            self.exeed.destroy()
        except:
            pass
        try:
            self.ins.destroy()
        except:
            pass
        try:
            self.VE.destroy()
        except:
            pass
        try:
            self.NUE.destroy()
        except:
            pass
        try:
            self.IC.destroy()
        except:
            pass
        try:
            self.IA.destroy()
        except:
            pass
        try:
            self.CREATA.destroy()
        except:
            pass
        try:
            self.ReadMee.destroy()
        except:
            pass
        try:
            self.Disposizione.destroy()
        except:
            pass
        try:
            self.Studenti.destroy()
        except:
            pass
        try:
            self.ok.destroy()
        except:
            pass
###################################################################

if __name__ == '__main__':
    test = posti()
    test.M_loop()

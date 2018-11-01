# ProgrammaGenerazionePosti

PROGRAMMA POSTI v.4.3.1 - By Carlo Zambaldo (mail: carlo.zambaldo@gmail.com)
Liceo Girolamo Fracastoro, Verona


### Descrizione generale del programma ###
Programma che genera a random la disposizione dei posti in una classe.
input necessari:
	- Numero studenti
	- Banchi per fila
	- Numero di file

funzioni aggiuntive:
 - Crea un documento .txt per salvare una disposizione
 - Legge il documento creato (ne ridisegna la disposizione)
 - Bottone Help per conoscere la versione, data aggiornamento e mail del programmatore
 - Inoltre il bottone Help consente di leggere i file , e il presente file README.txt
 - Converte i numeri identificativi con il nome degli studenti utilizzando il file NomiStudenti.txt
 - Decidere quante volte mescolare a random (da 0 a 10)
 - Mostra una finestra di avviso come gestione ad errori
 - (BETA) Possibilita' di aggiungere una condizione (es. studente1 non puo' essere vicino a studente2)
 - Le finestre degli errori si chiudono automaticamente
 - Possibilita' di inserire la classe per leggere il file NomiStudenti.txt corretto


### Istruzioni per la configurazione ###


### Guida all'installazione ###
Scaricare il file posti.py, (NOTA: e' necessario aver scaricato python v.3, anche se funziona anche con la v.2), eseguire dunque il file posti.py.

### Un elenco dei file contenuti nel pacchetto ###


### Informazioni riguardo al tipo di licenza e il copyright ###
Il programma è OpenSource. Modifiche e correzioni di bugs sono ben accette.

### Contatti del distributore e del programmatore ###
Carlo Zambaldo (carlo.zambaldo@gmail.com)

### Eventuali bug (conosciuti) ###
Nessun bug noto, in caso si riscontrasse qualsiasi malfunzionamento pregasi segnalare al programmatore.

### Risoluzione di problemi ###


### Ringraziamenti ###


### Un changelog ###


[*** ] Questa funzione, essendo BETA, non funziona del tutto, tuttavia riduce le possibilita' che due studenti siano vicini
      ATTENZIONE! - La sintassi della condizione DEVE essere StudenteA.StudenteB e non piu' di due studenti

[****] ATTENZIONE! - Il file NomiStudenti.txt viene ancora letto dal programma, in caso contrario viene richiesto l'inserimento
	             della classe di appartenenza (es. 3CS), il nuovo file degli studenti ha il nome NomiStudenti_*CLASSE*.txt
	             dove *CLASSE* e' la classe di appartenenza


Sintassi dei file:

[* ] File posti.txt 
Non cambiare il file! Salva la disposizione con la sintassi: n1.n2.n3...nm.*NumeroFile*.*BanchiPerFila*
Dove n1, n2, n3, ..., nm sono i numeri corrispondenti agli studenti o i loro nomi.
Sapendo ora la sintassi del file e' possibile scambiare due studenti (scambiando semplicemente i rispettivi numeri/nomi)
e salvando il file (N.B. NON CAMBIARE IL NOME DEL FILE!)

[**] File NomiStudenti.txt e NomiStudenti_*CLASSE*.txt
Scrivere il file con la sintassi: Studente1.Studente2.StudenteN. Dove Studente1 e' il primo in ordine alfabetico e via di seguito.
N.B. Notare il punto dopo StudenteN: e' necessario al fine di una corretta visualizzazione in seguito alla traduzione dai numeri
Inoltre, e' stato creato un programma (CreaFile.py) con il compito di agevolare la scrittura dei file-database del presente programma

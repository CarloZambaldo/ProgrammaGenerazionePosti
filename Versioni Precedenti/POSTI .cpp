/*
--	  PROGRAMMA POSTI	  --
--   by Carlo Zambaldo	  --
-- 						  --
--	  versione 1.0.0		  --
--						  --
--	ultimo aggiornamento	  --
--  		07 OTT 2017		  --
--						  --
--    VERSIONE IN C++	  --
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <fstream>
#include <iostream>
using namespace std;

int main(){
	int n,nf,nbf,mesc=10;
	srand(time(NULL));

	//richiedo l'inserimento dei dati
	cout<<"Numero di studenti: ";
	cin>>n;
	do{
		cout<<"Numero di file: ";
		cin>>nf;
		cout<<"Numero di banchi in una fila: ";
		cin>>nbf;
		if(nf*nbf<n) cout<<"I banchi non sono sufficienti per "<<n<<" alunni."<<endl;
	}while(nf*nbf<n);
	cout<<"Mescolo [numero da 0 a 100]: ";
	cin>>mesc;

	int v[n];
	for(int i=0; i<n; i++) v[i]=i+1; // creo il vettore v degli studenti
	cout<<"Studenti: ";
	for(int i=0; i<n; i++){
		cout<<v[i]<<"-";
	}
	cout<<endl;

	for(mesc*=10;mesc>=0;mesc--){
		int a,b;
		a=rand()%n;
		b=rand()%n;
		if(a!=b){
			v[a]+=v[b];
			v[b]=v[a]-v[b];
			v[a]-=v[b];
		}else{
			mesc++;
		}
	}
	cout<<"Mescolati: ";
	for(int i=0; i<n; i++){
		cout<<v[i]<<"-";
	}

	cout<<"\nI nuovi posti sono: \n";
	int stud=0;
	for(int c=0; c<=nf; c++){
		for(int k=0; k<=nbf; k++){
			for(int i=1; i<=k; i++){
				cout<<v[stud]<<"\t";
				stud++;
				if(stud>n)
					break;
			}
			if(stud>n)
				break;
		}
		if(stud>n){
			cout<<"\n CATTEDRA";
			break;
		}
		cout<<endl;
	}
	cout<<endl<<endl;
	//system("PAUSE");
	return 0;
}



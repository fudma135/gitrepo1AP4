/*
 * zasieg.cpp
 * 
 
 */
// zasieg globalny
//zmienna globalna
//zasieg lokalny
//zmienna lokalna
//void drukuj(){;}
//int sumuj(){return a;}
//int sumuj (int a, int b) {return suma;}//przekazanie przez wartosci
//void oblicz(int&liczba){liczba =5;} //przekazanie przez referencje


#include <iostream>
using namespace std;
int suma = 0;
void drukuj(int liczba) {
    cout<<suma<<endl;
    liczba+= 7;
    //cout<<&liczba<<endl;
    cout<<liczba<<endl;
}
void drukuj2(int&liczba){
    cout<<suma<<endl;
    liczba += 7;
    cout<<&liczba <<endl;
    cout<<liczba<<endl;
}

int main(int argc, char **argv)
{
	int suma = 5;
    int liczba =3;
    suma+=10;
    cout<<suma<<endl;
    cout<<liczba<<endl;
    cout<<&liczba<<endl;
    drukuj(liczba);
    drukuj2(liczba);
    cout<<liczba<<endl;
	return 0;
}


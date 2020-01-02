/*
 * kalkulator.cpp
 * 
 
 */


#include <iostream>
using namespace std;
void sumuj() {
    int a, b;
    cout<<"podaj dwie liczby:"<<endl;
    cin>>a>>b;
    cout<<"Suma:"<<a+b<<endl;
    }
    void odejmij() {
        int a, b;
    cout<<"podaj dwie liczby:"<<endl;
    cin>>a>>b;
    cout<<"Różnica:"<<a-b<<endl;
        }
        void mnożenie()
int main(int argc, char **argv)
{
	char operacja;
    cout <<"Jakie działanie chcesz wykonać(+,-,*,/)?"<<endl;
    cin>>operacja;
    switch(operacja) {
        case'+':
            sumuj();
        break; 
        case '-':
        odejmij();
        break;
        default:
            cout <<"Nie rozumiem"<< endl;
        break;
        }
	return 0;
}


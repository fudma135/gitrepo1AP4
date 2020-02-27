/*
 * silnia.cxx
 *
 */


#include <iostream>
using namespace ;
long silnia_it(int n){
    long s=1;
    for(int i=2; i<=n;i++){
        s*=i;
    }
    return s;
}
long silnia_re(int n){
    if(n==0)
    return 1;
    else
    return silnia_re(n-1) *n;
int main(int argc, char **argv)
{
	int n;
    cout<<"Podaj liczbe:"<<endl;
    cin>>n;
    cout<<n<<"!="<<silnia_it(n);
	return 0;
}


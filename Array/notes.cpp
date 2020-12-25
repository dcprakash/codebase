#include <iostream>

struct calc{
    int buy;
    int sell;
};


void stockBuySell(int a[], int n){
    int i=0;
    int x=0;
    calc sol[n/2-1];
    while(i<n-1){
        while(i<n-1 && a[i]>=a[i+1]){
            i++;
        }
        sol[x].buy=i++;
        
        while(i<n-1 && a[i]>=a[i-1]){
            i++;
        }
        sol[x].sell=i-1;
        x++;
    }
    if(x==0){
        std::cout << "No profit" << std::endl;
    }
    else {
        for(int i=0;i<x;i++){
            std::cout << sol[i].buy << sol[i].sell << std::endl;
        }
    }
}


int main()
{
	std::cout << "Hello from AWS Cloud9!" << std::endl;
	int a[]={100, 180, 260, 310, 40, 535, 695};
	int n=sizeof(a)/sizeof(a[0]);
	stockBuySell(a,n);
}
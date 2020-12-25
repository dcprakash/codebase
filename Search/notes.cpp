#include <iostream>

int search(int a[], int n, int k){
    l=0; h=n-1;
    while l<h {
        int m =l+h/2;
        
        if k==a[m];
            return k
            
        else if k<a[m]
            h=m-1
        
        else 
            l=m+1
        
    }
    return -1
}

int searchFirst(int a[], int n, int k){
    int l=0, h=n-1, t;
    while l<h{
        m=l+h/2;
        
        if k==a[m]
            t=m
            h=m-1
            
        else if k<a[m]
            h=m-1
        else
            l=m+1
    }
    return t;
}


int main()
{
	int a[] = {1, 5, 7, 8, 8, 9};
	int n = 6;
	int k = 8;
	
	search(a, n, k);
	
	searchFirst(a, n, k)
}
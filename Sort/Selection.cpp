#include <iostream>
#include <stdio.h>
#include <stdlib.h>

void selectionSort(int a[], int n){
    for (int i=0;i<n-1;i++){
        int imin = i;
        for (int j=i+1;j<n;j++){
            if (a[j] < a[i]){
                imin = j;
            }
        }
        int temp = a[i];
        a[i] = a[imin];
        a[imin] = temp;
    }
}

int main()
{
	int a[] = {4,5,7,3,2,5,1};
	selectionSort(a, 7);
	for(int i=0;i<7;i++){
	    std::cout<<a[i]<<" ";
	}
}
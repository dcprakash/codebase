#include <iostream>

void selectSort(int a[], int n){
    for(int i=0; i<n; i++){
        int min = i;
        for(int j=i+1;j<n;j++){
            if a[j] < a[min]{
                min = j;
            }
        }
        int t = a[i];
        a[i] = a[min];
        a[min] = t;
    }
}


void merge(int a[], int l, int m, int r){
    int n1 = m-l+1;
    int n2 = r-m;
    
    int l[n1], r[n2];
    
    for(int i=0; i<n1; i++)
        l[i]=a[l+i]
    for(int j=0; j<n2;j++)
        r[j]=a[m+j+1]
    
    int i, j=0;
    int k=1;
    
    while i<n1 && j<n2 {
        if l[i]<r[j]{
            a[k]=a[i]
            i++
            k++
        }
        else{
            a[k]=a[j]
            j++
            k++
        }
    }
    
    while i<n1 {
        a[k]=l[i];
        i++
        k++
    }
    
    while j<n2 {
        a[k]=r[j]
        j++
        k++
    }
}

void mergeSort(int a[], int l, int r){
    m=(l+r-1)/2;
    mergeSort(a,l,m);
    mergeSort(a,m+1,r);
    merge(a,l,m,r);
}

int main()
{
	int a[] = {3, 5, 6, 1, 4};
	selectSort(a, 5);
	mergeSort(a, 0, len(a)-1);
}
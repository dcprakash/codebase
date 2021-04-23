#include <iostream>
#include <stdio.h>
#include <stdlib.h>

class MergeSorting {
public:
    void mergeSort(int a[], int n);
    void Mergeit(int a[], int l[], int r[], int LC, int RC);
};
void MergeSorting::mergeSort(int a[], int n)
{
    if (n < 2)
        return;
    int mid = n / 2;
    int l[4], r[4];
    for (int i = 0; i < mid; i++)
        l[i] = a[i];
    for (int j = mid; j < n - mid; j++)
        r[j] = a[j];
    mergeSort(l, mid);
    mergeSort(r, n - mid);
    Mergeit(a, l, r, mid, n - mid);
}

void MergeSorting::Mergeit(int a[], int l[], int r[], int LC, int RC)
{
    int i, j, k;
    i = 0;
    j = 0;
    k = 0;
    while (i < LC && j < RC) {
        if (l[i] < r[i])
            a[k++] = l[i++];
        else
            a[k++] = r[j++];
    }
    while (i < LC)
        a[k++] = l[i++];
    while (j < RC)
        a[k++] = r[j++];
}

int main()
{
    std::cout << "Merge Sort" << std::endl;
    int a[] = { 8, 7, 6, 5, 4, 3, 2, 1 };
    MergeSorting m;
    m.mergeSort(a, 8);
    //std::cout <<a << std::endl;
    for (int i = 0; i < 8; i++) {
        std::cout << a[i] << std::endl;
    }
    return 0;
}
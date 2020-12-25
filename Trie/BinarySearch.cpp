#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int anyOccurance(int a[], int n, int x) {
    int low =0, high = n-1;
    while (low <= high) {
        int mid = (low+high)/2;
        if (a[mid] == x ){
            return mid;
        }
        else if (x<a[mid]) high = mid-1;
        else low = mid+1;
    }
    return -1;
}

int firstOccurance(int a[], int n, int x) {
    int low =0, high = n-1, results=-1;
    while (low <= high) {
        int mid = (low+high)/2;
        if (a[mid] == x ){
            results = mid;
            high = mid-1;
        }
        else if (x<a[mid]) high = mid-1;
        else low = mid+1;
    }
    return results;
}

int lastOccurance(int a[], int n, int x) {
    int low =0, high = n-1, results=-1;
    while (low <= high) {
        int mid = (low+high)/2;
        if (a[mid] == x ){
            results = mid;
            low = mid+1;
        }
        else if (x<a[mid]) high = mid-1;
        else low = mid+1;
    }
    return results;
}

int main()
{
	std::cout << "Binary Search!" << std::endl;
	int a[] = {1,2,6,2,3,4,5,8};
	//int result = anyOccurance(a,8,5);
	//int result = firstOccurance(a,8,2);
	int result = lastOccurance(a,8,2);
	if (result == -1){
		std::cout << "No Match Found" << std::endl;
	}
	else{
	    std::cout << "Match Found at position  ";
	    std::cout << result ;
	}
	
}

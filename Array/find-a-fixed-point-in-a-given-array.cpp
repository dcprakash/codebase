// C++ program to check fixed point 
// in an array using binary search 
// https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/
// Fixed Point in an array is an index i such that arr[i] is equal to i. 
// Note that integers in array can be negative.
/*
  Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3 
  
  low=0, high=n-1
  while(low<high){
  	mid=(l+h)/2;
  	if x==a[mid]
  		return mid;
  	else if x<a[mid]
  		high = mid-1;
  	else
  		low = mid+1;
  }
  
  
*/
#include <bits/stdc++.h> 
using namespace std; 

int binarySearch(int arr[], int low, int high) 
{ 
	if(high >= low) 
	{ 
		int mid = (low + high)/2; /*low + (high - low)/2;*/
		if(mid == arr[mid]) 
			return mid; 
		if(mid > arr[mid]) 
			return binarySearch(arr, (mid + 1), high); 
		else
			return binarySearch(arr, low, (mid -1)); 
	} 

	/* Return -1 if there is no Fixed Point */
	return -1; 
} 

/* Driver code */
int main() 
{ 
	int arr[10] = {-10, -1, 0, 3, 10, 11, 30, 50, 100}; 
	int n = sizeof(arr)/sizeof(arr[0]); 
	cout<<"Fixed Point is "<< binarySearch(arr, 0, n-1); 
	return 0; 
} 

/*
int linearSearch(int arr[], int n)  
{  
    int i;  
    for(i = 0; i < n; i++)  
    {  
        if(arr[i] == i)  
            return i;  
    }  
  
    return -1;  
}  
*/

// C++ implementation to find the index of first 
// '1' in a sorted array of 0's and 1's 
// https://www.geeksforgeeks.org/find-index-first-1-sorted-array-0s-1s/
// find index of first 1 in sorted 0's and 1's array
#include <bits/stdc++.h> 
using namespace std; 

// function to find the index of first '1' 
// binary search technique is applied 
int indexOfFirstOne(int arr[], int low, int high) 
{ 
	while (low <= high) { 
		int mid = (low + high) / 2; 

		// if true, then 'mid' is the index of first '1' 
		if (arr[mid] == 1 && (mid == 0 || arr[mid - 1] == 0)) 
			return mid; 

		// first '1' lies to the left of 'mid' 
		else if (arr[mid] == 1) 
			high = mid - 1; 

		// first '1' lies to the right of 'mid' 
		else
			low = mid + 1; 
	} 

	// 1's are not present in the array 
	return -1; 
} 

// Driver program to test above 
int main() 
{ 
	int arr[] = { 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 }; 
	int n = sizeof(arr) / sizeof(arr[0]); 
	cout << indexOfFirstOne(arr, 0, n - 1); 
	return 0; 
} 

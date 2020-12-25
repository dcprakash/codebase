// https://www.geeksforgeeks.org/find-minimum-difference-pair/
// C++ program to find minimum difference between 
// any pair in an unsorted array 
/*
Given an unsorted array, find the minimum difference between any pair in given array.

Input  : {1, 5, 3, 19, 18, 25};
Output : 1
Minimum difference is between 18 and 19
*/
#include <bits/stdc++.h> 
using namespace std; 

// Returns minimum difference between any pair 
int findMinDiff(int arr[], int n) 
{ 
// Sort array in non-decreasing order 
sort(arr, arr+n); 

// Initialize difference as infinite 
int diff = INT_MAX; 

// Find the min diff by comparing adjacent 
// pairs in sorted array 
for (int i=0; i<n-1; i++) 
	if (arr[i+1] - arr[i] < diff) 
		diff = arr[i+1] - arr[i]; 

// Return min diff 
return diff; 
} 

// Driver code 
int main() 
{ 
int arr[] = {1, 5, 3, 19, 18, 25}; 
int n = sizeof(arr)/sizeof(arr[0]); 
cout << "Minimum difference is " << findMinDiff(arr, n); 
return 0; 
} 


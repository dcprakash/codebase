// C++ program to find type of array, ascending 
// descending, clockwise rotated or anti-clockwise 
// rotated. 
// https://www.geeksforgeeks.org/type-array-maximum-element/
// increasing or Ascending and rotated
// decreasing or Descending and rotated
// We have to return max element

#include<bits/stdc++.h> 
using namespace std; 

// Function to find the type of an array 
// and maximum element in it. 
void findType(int arr[] , int n) 
{ 
	int i = 0; 

	// Check if the array is in ascending order 
	while (i < n-1 && arr[i] <= arr[i+1]) 
		i++; 

	// If i reaches to last index that means 
	// all elements are in increasing order 
	if (i == n-1) 
	{ 
		cout << "Ascending with maximum element = "
			<< arr[n-1]<<endl ; 
		return ; 
	} 

	// If first element is greater than next one 
	if (i == 0) 
	{ 
		while (i < n-1 && arr[i] >= arr[i+1]) 
			i++; 

		// If i reaches to last index 
		if (i == n - 1) 
		{ 
			cout << "Descending with maximum element = "
				<< arr[0] << endl; 
			return ; 
		} 

		// If the whole array is not in decreasing order 
		// that means it is first decreasing then 
		// increasing, i.e., descending rotated, so 
		// its maximum element will be the point breaking 
		// the order i.e. i so, max will be i+1 
		if (arr[0] < arr[i+1]) 
		{ 
			cout << "Descending rotated with maximum element = "
				<< max(arr[0], arr[i+1]) << endl; 
			return ; 
		} 
		else
		{ 
			cout << "Ascending rotated with maximum element = "
				<< max(arr[0], arr[i+1]) << endl; 
			return ; 
		} 
	} 

	// If whole array is not increasing that means at some 
	// point it is decreasing, which makes it ascending rotated 
	// with max element as the decreasing point 
	if (i < n -1 && arr[0] > arr[i+1]) 
	{ 
		cout << "Ascending rotated with maximum element = "
			<< max(arr[i], arr[0]) << endl; 
		return; 
	} 

	cout << "Descending rotated with maximum element "
		<< max(arr[i],arr[0]) << endl; 
} 

// Driver code 
int main() 
{ 
	int arr1[] = { 4, 6, 1, 3}; // Ascending rotated 
	int n = sizeof (arr1) / sizeof (arr1[0]); 
	findType(arr1, n); 

	int arr2[] = { 2, 1, 7, 5, 4, 3}; // Descending rotated 
	n = sizeof(arr2) / sizeof (arr2[0]); 
	findType(arr2, n); 

	int arr3[] = { 1, 2, 3, 4, 5, 8}; // Ascending 
	n = sizeof(arr3) / sizeof (arr3[0]); 
	findType(arr3, n); 

	int arr4[] = { 9, 5, 4, 3, 2, 1}; // Descending 
	n = sizeof(arr4) / sizeof (arr4[0]); 
	findType(arr4, n); 

	return 0; 
} 

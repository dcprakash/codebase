// C++ implementation to find unique digit 
// numbers in a range 
// https://www.geeksforgeeks.org/numbers-unique-distinct-digits/
// numbers having unique digits or distinct digits
#include<bits/stdc++.h> 
using namespace std; 

// Function to print unique digit numbers 
// in range from l to r. 
void printUnique(int l, int r) 
{ 
	// Start traversing the numbers 
	for (int i=l ; i<=r ; i++) 
	{ 
		int num = i; 
		bool visited[10] = {false}; 

		// Find digits and maintain its hash 
		while (num) 
		{ 
			// if a digit occcurs more than 1 time 
			// then break 
			if (visited[num % 10]) 
				break; 

			visited[num%10] = true; 

			num = num/10; 
		} 

		// num will be 0 only when above loop 
		// doesn't get break that means the 
		// number is unique so print it. 
		if (num == 0) 
			cout << i << " "; 
	} 
} 

// Driver code 
int main() 
{ 
	int l = 10, r = 13; 
	printUnique(l, r); 
	return 0; 
} 

// C++ implementation to check whether every 
// digit in the binary representation of the 
// given number is set or not 
// https://www.geeksforgeeks.org/check-bits-number-set/
// & is AND operator
// 7>> becomes 3 because 111 >> 11
// check if bit is set
#include <bits/stdc++.h> 
using namespace std; 
  
// function to check if all the bits are set 
// or not in the binary representation of 'n' 
string areAllBitsSet(int n) 
{ 
    // all bits are not set 
    if (n == 0) 
        return "No"; 
  
    // loop till n becomes '0' 
    while (n > 0) 
    { 
        int temp1= n & 1;
        cout << temp1<< std::endl;
    
        int temp2= n >> 1;
        cout << temp2<< std::endl;
        cout << "------"<< std::endl;
    
        // if the last bit is not set 
        if ((n & 1) == 0) 
            return "No"; 
  
        // right shift 'n' by 1 
        n = n >> 1; 
    } 
  
    // all bits are set 
    return "Yes"; 
} 
  
// Driver program to test above 
int main() 
{ 
    int n = 7; 
    cout << areAllBitsSet(n); 
    return 0; 
}

/*
7
111
  1
---
  1
3

3
  11
   1
----
   1
1

1
   1
   1
----
   1
0
*/
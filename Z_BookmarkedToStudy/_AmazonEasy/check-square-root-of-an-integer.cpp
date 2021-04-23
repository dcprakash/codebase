// A C++ program to find floor(sqrt(x) 
#include<bits/stdc++.h> 
using namespace std; 
  
// Returns floor of square root of x 
// https://www.geeksforgeeks.org/square-root-of-an-integer/
// square root of an integer
int floorSqrt(int x) 
{ 
    // Base cases 
    if (x == 0 || x == 1) 
    return x; 
  
    // Staring from 1, try all numbers until 
    // i*i is greater than or equal to x. 
    int i = 1, result = 1; 
    while (result <= x) 
    { 
      i++; 
      result = i * i; 
    } 
    return i - 1; 
} 
  
// Driver program 
int main() 
{ 
    int x = 11; 
    cout << floorSqrt(x) << endl; 
    return 0; 
} 
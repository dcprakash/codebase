// Count number of bits to be flipped 
// to convert A into B 
// https://www.geeksforgeeks.org/count-number-of-bits-to-be-flipped-to-convert-a-to-b/
/*
10^1-9^1=1

16 8 4 2 1
0  1 0 1 0=10
1  0 1 0 0=20
1  1 1 1 0=30

0&1=0
1&1=1
1&1=1
1&1=1
1&1=1

01111
*/
#include <iostream> 
using namespace std; 
  
// Function that count set bits 
int countSetBits(int n) 
{ 
    int count = 0; 
    while (n) 
    {   
        int t2=n & 1;
        cout << t2;
        count += n & 1; 
        n >>= 1; 
    } 
    cout<< endl;
    return count; 
} 
  
// Function that return count of 
// flipped number 
int FlippedCount(int a, int b) 
{ 
    // Return count of set bits in 
    // a XOR b 
    int t1=a^b;
    cout << t1 << endl;
    return countSetBits(a^b); 
} 
  
// Driver code 
int main() 
{ 
    int a = 10; 
    int b = 20; 
    cout << FlippedCount(a, b)<<endl; 
    return 0; 
} 
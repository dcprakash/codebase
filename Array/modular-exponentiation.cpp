/*
https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/

Given three numbers x, y and p, compute (xy) % p.
Input:  x = 2, y = 3, p = 5
Output: 3
Explanation: 2^3 % 5 = 8 % 5 = 3.


*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	t=1;
	while(t--)
	{
	    int a,b,c;
	    // cin>>a>>b>>c;
	    a=2;b=4;c=5;
	    int res=1;
	    while(b>0)
	    {
	        res=(res*a);
	        b--;
	    }
	    res=res%c;
	    std::cout << res << std::endl;
	    //cout<<res<<endl;
	}
	return 0;
}
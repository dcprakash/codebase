#include <iostream>

int main()
{
	n="26";
	r="";
	while n>0{
	    r=n%26;
	    if r==0{
	        r+='z'
	        n=n/26-1;
	    }
	    else {
	        n=n/26;
	        r=(r-1)+'A'
	    }
	}
	reverse(r.begin(), r.end())
	
}
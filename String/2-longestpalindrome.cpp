
//abbaab abaa
// https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
// start at first ix char (1), check if first-1 and first is same charcter, if not move to second ix char (2)
// if same char, then low-- and high++; repeath looop

//maxLen is 1 to start with; start = 0; low=i-1; high=i
//check if low>=0 and high<n and str[low]==str[high]
//if high-low+1 > maxLen ; start=low and maxLen = high-low+1

#include<iostream>
#include<string>
using namespace std;

void longestpalindrome(string str)
{
    int maxlength = 1;
    int start = 0;
    
    int low,high;
    int n = str.length();
    for(int i=1; i<n; i++)
    {
        //even length string 
        // low = i-1;
        // high = i;
        
        // while(low >= 0 && high <n && str[low] == str[high])
        // {
        //     if(high - low + 1 > maxlength)
        //     {
        //         start = low;
        //         maxlength = high-low+1;
        //     }
        //     low--;high++;
        //     std::cout << low << high << std::endl;
        // }
        
        // //odd length string
        low = i-1;
        high = i+1;
        
        while(low >= 0 && high <n && str[low] == str[high])
        {
            if(high - low + 1 > maxlength)
            {
                start = low;
                maxlength = high-low+1;
            }
            low--;high++;
        }
    }
    for(int i=start; i<start+maxlength;i++)
        cout<<str[i];
    cout<<endl;
}
int main()
 {
	//code
	int t;
	std::cout << "Enter Number of Test Cases" << std::endl;
	cin>>t;
	
	while(t>0)
	{
	    std::cout << "Enter input string" << std::endl;
	    cin>>ws;
	    //std::cout << ws << std::endl;
	    string str;
	    getline(cin,str);
	    std::cout << str << std::endl;
	    longestpalindrome(str);
	    t--;
	}
	return 0;
}
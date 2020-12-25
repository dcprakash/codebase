#include <iostream>
using namespace std;
bool isVowel(char c)
{
    if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
        return true;
    return false;
}
int main() {
	//code
	int t;
	cin>>t;
	while(t--)
	{
	    string s;
	    cin>>s;
	    string tmp;
	    for(int i=0;i<s.size();i++)
	    {
	        if(isVowel(s[i]))
	        tmp+=s[i];
	    }
	    int k=tmp.size()-1;
	    for(int i=0;i<s.size();i++)
	    {
	        if(isVowel(s[i]))
	        {
	            cout<<tmp[k];
	            k--;
	        }
	        else
	            cout<<s[i];
	    }
	    cout<<"\n";
	}
	return 0;
}
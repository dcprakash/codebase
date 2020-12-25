#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
 {
	//code
	int t;cin>>t;
	while(t--){
	    string s;cin>>s;
	    vector<string> r;
	    sort(s.begin(),s.end());
	    
	    r.push_back(s);
	    //cout<<s<<" ";
	    //string temp=s,k;
	    while(next_permutation(s.begin(),s.end())){
	       r.push_back(s);
	    }
	    //sort(r.begin(),r.end());
	    for(int i=0;i<r.size();i++) 
		cout<<r[i]<<" ";
	    cout<<endl;
	}
	return 0;
}
//Not for now

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	//code
	int t;
	cin>>t;
	while(t--)
	{
	    string s;
	    cin>>s;
	    int k;
	    cin>>k;
	    priority_queue<int> pq;
	    map<char,int> mp;
	    for(int i=0;i<s.length();i++)
	    {
	        mp[s[i]]++;
	    }
	    for(auto it=mp.begin();it!=mp.end();it++)
	    {
	    	//std::cout << "it" << it << std::endl;
	        pq.push(it->second);
	        std::cout << "it->second : " << it->second << std::endl;
	    }
	    while(k && !pq.empty())
	    {
	        int tp=pq.top();
	        tp--;
	        pq.pop();
	        if(tp>=1)
	        {
	            pq.push(tp);
	        }
	        k--;
	    }
	    int sum=0;
	    while(pq.empty()==false)
	    {
	        sum+=(pq.top()*pq.top());
	       // cout<<pq.top()<<" ";
	        pq.pop();
	    }
	    cout<<sum<<endl;
	}
	return 0;
}
//stack st; string s; int i, l, 
//push to stack (i-low words from low)
//print top and pop

#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
 {
	//code
	int t;cin>>t;
	//string test; cin>>test;
	//std::cout << test[0] << " " << test[1] << " " << test[2] << " " <<  test[5] <<std::endl;
	while(t--){
	    string s;cin>>s;
	    string k;
	    stack<string>st;
	    int i=0,l=0,h=0;
	    while(s[i]!='\0'){
	        
	        if(s[i]=='.') {
	           
	            k=s.substr(l,i-l);
	            cout<<i << " " <<l << " " << h <<endl ;
	            l=i+1;
	            cout<<i << " " <<l << " " << h << endl;
	            std::cout << k << std::endl;
	            st.push(k);
	            st.push(".");
	        }
	        i++;
	    }
	    std::cout << "..." << std::endl;
	    std::cout << l << std::endl;
	    st.push(s.substr(l));
	    while(!st.empty()){
	        cout<<st.top();
	        st.pop();
	    }
	    cout<<endl;
	}
	return 0;
}
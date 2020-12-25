#include<iostream>
using namespace std;
int main()
 {
	//code
	int t,n;
	cin>>t;
	while(t--){
	    cin>>n;
	    int a[n],res,freq[1001]={0};
	    for(int i=0;i<n-1;i++){
	       cin>>a[i];
	       freq[a[i]]=1;
	    }
	    for(int i=1;i<=n;i++){
	    	std::cout << freq[i] << std::endl;
	        if(freq[i]==0){
	            res=i;
	            break;
	       }
	    }
	    cout<<res<<endl;
	}
	return 0;
}
//https://practice.geeksforgeeks.org/problems/transform-string5648/1
// min steps required to transfom one string to another

#include<iostream>
#include<math.h>
using namespace std;
int main(){
	int t;cin>>t;
	string str,str1;
	while(t--){
	cin>>str>>str1;
		// int a[26]={0};
		// for(int i=0;i<str.size();i++)
		// 	a[str[i]-'a']++;
		// 	std::cout << str << std::endl;
		// for(int i=0;i<str1.size();i++)
		// 	a[str1[i]-'a']--;
        int c=0,res=0; 
		// for(int i=0;i<26;i++){
		//     if(a[i]!=0){
		//         c=1;
		//         break;
		//     }
		// }
		//  if(c==0)
	 	 for(int i=str.size()-1,j=str.size()-1;i>=0;){
			while(i>=0 && str[i]!=str1[j]){
				res++;
				i--;
			}
			if(i>=0){
				i--;
				j--;
			}
		 }
        if(c==0)
		 cout<<res<<endl;
		 else cout<<-1<<endl;
	}
	return 0;
}
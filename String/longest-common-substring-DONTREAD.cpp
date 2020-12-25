//https://www.geeksforgeeks.org/longest-common-substring-dp-29/

//   x y a b c 
// a 0 0 1 0 0 //res=1
// b 0 0 0 2 0 //res=2
// c 0 0 0 0 3 //res=3
// x 1 0 0 0 0 //res=3
// y 0 2 0 0 0 //res=3


#include <bits/stdc++.h>
using namespace std;
int subs(string a,string b,int n,int m){
    int arr[n+1][m+1];

    int result = 0;
    for(int i=0;i<=n;i++){
        for(int j=0;j<=m;j++){
            if((i==0 || j==0)){
                arr[i][j] = 0;
            }
            else if(a[i-1] == b[j-1]){
                std::cout << "a[i-1]"<<a[i-1]<< std::endl;
                std::cout << "b[j-1]"<<b[j-1]<< std::endl;
                std::cout<<"arr[i-1][j-1]"<<arr[i-1][j-1]<<std::endl;
                arr[i][j] = arr[i-1][j-1] + 1;
                result = max(result,arr[i][j]);
            }
            else arr[i][j] = 0;
        }
    }
 
    
    return result;
}
int main() {
	int t;
	cin >>t ;
	while(t--){
	    int n,m;
	    cin >> n >> m;
	    string s1,s2;
	    cin >> s1 >> s2;
	    int len;
	    len = subs(s1,s2,n,m);
	    cout << len << endl;
	}
}
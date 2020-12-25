//************
//not now
#include <iostream>
using namespace std;

void findMajor(int a[], int n){
    int maj_idx = 0;
    int count = 1;
    for(auto i =1; i<n; i++){
        if (a[maj_idx]==a[i]){
            count++;
        } else {
            count--;
        }
        if(count==0){
            maj_idx = i;
            count = 1;
        }
    }
    cout << "maj_idx " << maj_idx <<endl;
    cout << "count " << count <<endl;
    int maj_num=0;
    for(auto i =0; i<n; i++){
        if(a[i]==a[maj_idx]) maj_num++;
    }
    cout << "maj_num " << maj_num <<endl;
    if (maj_num>n/2)
        cout << a[maj_idx] <<endl;
    else
        cout << "NO Majority Element" << endl;
}

int main() {
	//code
	int numT;
    cin >> numT;
    while(numT--){
        int numbers;
        cin >> numbers;
        int a[numbers];
        for(auto i=0; i<numbers; i++){
            cin >> a[i];
        }
        findMajor(a, numbers);
    }
	return 0;
}
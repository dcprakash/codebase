#include<iostream>
#include<stdio.h>

#include<bits/stdc++.h>
using namespace std;

void find_ele(int arr[],int n, int k)
{
    sort(arr,arr+n);

    int start=0,last=n;
    int sum=0;
    while(start<last)
    {
        sum=arr[start]+arr[last];
        if(sum == k)
        {
            cout<<"Yes"<<endl;
            //cout<<sum<<endl;
            return;
        }

        else if(sum<k)
            start++;
        else
            last--;
    }

    cout<<"No"<<endl;
    return;
}

int main()
{
    int t;

	cin>>t;

	for(int p=1; p<=t; p++)
	{
	    int arr[200];
	    int n;
        cin>>n;

        int k;
        cin>>k;

        for(int i=0;i<n;i++)
            cin>>arr[i];

        find_ele(arr,n,k);
	}

    return 0;
}

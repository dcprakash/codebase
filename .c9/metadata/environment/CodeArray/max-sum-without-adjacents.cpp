{"filter":false,"title":"max-sum-without-adjacents.cpp","tooltip":"/CodeArray/max-sum-without-adjacents.cpp","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":34,"column":2},"end":{"row":34,"column":2},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"ed4c6387680343c11e309ee8f5a3f795c4dc2ae4","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":36,"column":1},"action":"remove","lines":["#include <bits/stdc++.h>","using namespace std;","// https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/","int maxSum(int arr[],int n)","{","    ","    int inc,exc,temp;","    inc=arr[0];","    exc=0;","    cout<< \"    inc:\"<< inc << \"    exc:\"<< exc <<endl;","    for(int i=1;i<n;i++)","    {","        temp=inc;","        inc=max(inc,exc+arr[i]);","        exc=temp;","        cout<<\"i:\"<< i << \"   temp:\" << temp << \"    inc:\"<< inc << \"    exc:\"<< exc <<endl;","    }","    ","    return inc;","}","","int main()","{","    int t,n;","    cin>>t;","    while(t--)","    {","        cin>>n;","        int arr[n];","        for(int i=0;i<n;i++)","        {","            cin>>arr[i];","        }","        ","        cout<<maxSum(arr,n)<<endl;","    }","}"],"id":4},{"start":{"row":0,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["#include<stdio.h> ","  ","/*Function to return max sum such that no two elements "," are adjacent */","int FindMaxSum(int arr[], int n) ","{ ","  int incl = arr[0]; ","  int excl = 0; ","  int excl_new; ","  int i; ","  ","  for (i = 1; i < n; i++) ","  { ","     /* current max excluding i */","     excl_new = (incl > excl)? incl: excl; ","  ","     /* current max including i */","     incl = excl + arr[i]; ","     excl = excl_new; ","  } ","  ","   /* return max of incl and excl */","   return ((incl > excl)? incl : excl); ","} ","  ","/* Driver program to test above function */","int main() ","{ ","  int arr[] = {5, 5, 10, 100, 10, 5}; ","  int n = sizeof(arr) / sizeof(arr[0]); ","  printf(\"%d n\", FindMaxSum(arr, n)); ","  return 0; ","} "]}],[{"start":{"row":3,"column":14},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":4,"column":1},"end":{"row":4,"column":82},"action":"insert","lines":["https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/"],"id":6}],[{"start":{"row":4,"column":82},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":[" "]}]]},"timestamp":1562212473810}
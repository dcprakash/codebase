{"filter":false,"title":"array-rotation.cpp","tooltip":"/articles/array-rotation.cpp","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["#include <iostream>","","int main()","{","\tstd::cout << \"Hello from AWS Cloud9!\" << std::endl;","}"],"id":1},{"start":{"row":0,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["// C++ program to rotate an array by ","// d elements ","#include <bits/stdc++.h> ","using namespace std; ","  ","/*Function to left Rotate arr[] of  ","  size n by 1*/","void leftRotatebyOne(int arr[], int n) ","{ ","    int temp = arr[0], i; ","    for (i = 0; i < n - 1; i++) ","        arr[i] = arr[i + 1]; ","  ","    arr[i] = temp; ","} ","  ","/*Function to left rotate arr[] of size n by d*/","void leftRotate(int arr[], int d, int n) ","{ ","    for (int i = 0; i < d; i++) ","        leftRotatebyOne(arr, n); ","} ","  ","/* utility function to print an array */","void printArray(int arr[], int n) ","{ ","    for (int i = 0; i < n; i++) ","        cout << arr[i] << \" \"; ","} ","  ","/* Driver program to test above functions */","int main() ","{ ","    int arr[] = { 1, 2, 3, 4, 5, 6, 7 }; ","    int n = sizeof(arr) / sizeof(arr[0]); ","  ","    // Function calling ","    leftRotate(arr, 2, n); ","    printArray(arr, n); ","  ","    return 0; ","} "]}],[{"start":{"row":1,"column":14},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["/"],"id":3}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["/"],"id":4}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":[" "],"id":5}],[{"start":{"row":2,"column":3},"end":{"row":2,"column":48},"action":"insert","lines":["https://www.geeksforgeeks.org/array-rotation/"],"id":6}],[{"start":{"row":2,"column":48},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":7}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":3,"column":0},"end":{"row":3,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"dcdd37355c98aa5ce4aef2fe1f8f23997ffbc7d5","timestamp":1562622486147}
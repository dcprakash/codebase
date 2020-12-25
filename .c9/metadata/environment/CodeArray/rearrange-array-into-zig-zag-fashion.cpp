{"filter":false,"title":"rearrange-array-into-zig-zag-fashion.cpp","tooltip":"/CodeArray/rearrange-array-into-zig-zag-fashion.cpp","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":68},"end":{"row":1,"column":68},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":20,"state":"start","mode":"ace/mode/c_cpp"}},"hash":"ca4bfcb09e575e1b68ff141d735617f110494e0d","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":0,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["#include <iostream>","","int main()","{","\tstd::cout << \"Hello from AWS Cloud9!\" << std::endl;","}"],"id":1},{"start":{"row":0,"column":0},"end":{"row":42,"column":0},"action":"insert","lines":["// C++ program to sort an array in Zig-Zag form ","#include <iostream> ","using namespace std; ","","// Program for zig-zag conversion of array ","void zigZag(int arr[], int n) ","{ ","\t// Flag true indicates relation \"<\" is expected, ","\t// else \">\" is expected. The first expected relation ","\t// is \"<\" ","\tbool flag = true; ","","\tfor (int i=0; i<=n-2; i++) ","\t{ ","\t\tif (flag) /* \"<\" relation expected */","\t\t{ ","\t\t\t/* If we have a situation like A > B > C, ","\t\t\twe get A > B < C by swapping B and C */","\t\t\tif (arr[i] > arr[i+1]) ","\t\t\t\tswap(arr[i], arr[i+1]); ","\t\t} ","\t\telse /* \">\" relation expected */","\t\t{ ","\t\t\t/* If we have a situation like A < B < C, ","\t\t\twe get A < C > B by swapping B and C */","\t\t\tif (arr[i] < arr[i+1]) ","\t\t\t\tswap(arr[i], arr[i+1]); ","\t\t} ","\t\tflag = !flag; /* flip flag */","\t} ","} ","","// Driver program ","int main() ","{ ","\tint arr[] = {4, 3, 7, 8, 6, 2, 1}; ","\tint n = sizeof(arr)/sizeof(arr[0]); ","\tzigZag(arr, n); ","\tfor (int i=0; i<n; i++) ","\t\tcout << arr[i] << \" \"; ","\treturn 0; ","} ",""]}],[{"start":{"row":0,"column":48},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["/"],"id":3}],[{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["/"],"id":4}],[{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":[" "],"id":5}],[{"start":{"row":1,"column":3},"end":{"row":1,"column":68},"action":"insert","lines":["https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/"],"id":6}]]},"timestamp":1563214788343}
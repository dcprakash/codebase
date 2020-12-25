{"filter":false,"title":"converting-decimal-roman-numerals.cpp","tooltip":"/AmazonEasy/converting-decimal-roman-numerals.cpp","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":6},"end":{"row":21,"column":6},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"e6dead70e0e87c395b76d7bf036bc05995066959","undoManager":{"mark":35,"position":35,"stack":[[{"start":{"row":0,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["#include <iostream>","","int main()","{","\tstd::cout << \"Hello from AWS Cloud9!\" << std::endl;","}"],"id":1},{"start":{"row":0,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["// C++ Program to convert decimal number to ","// roman numerals ","#include <bits/stdc++.h> ","using namespace std; ","","// Function to convert decimal to Roman Numerals ","int printRoman(int number) ","{ ","\tint num[] = {1,4,5,9,10,40,50,90,100,400,500,900,1000}; ","\tstring sym[] = {\"I\",\"IV\",\"V\",\"IX\",\"X\",\"XL\",\"L\",\"XC\",\"C\",\"CD\",\"D\",\"CM\",\"M\"}; ","\tint i=12; ","\twhile(number>0) ","\t{ ","\tint div = number/num[i]; ","\tnumber = number%num[i]; ","\twhile(div--) ","\t{ ","\t\tcout<<sym[i]; ","\t} ","\ti--; ","\t} ","} ","","//Driver program ","int main() ","{ ","\tint number = 3549; ","","\tprintRoman(number); ","","\treturn 0; ","} ",""]}],[{"start":{"row":1,"column":18},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["/"],"id":3}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["/"],"id":4}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":[" "],"id":5}],[{"start":{"row":2,"column":3},"end":{"row":2,"column":101},"action":"insert","lines":["https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/"],"id":6}],[{"start":{"row":2,"column":101},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["/"],"id":8}],[{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["/"],"id":9}],[{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":[" "],"id":10}],[{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["d"],"id":11}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["e"],"id":12}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["c"],"id":13}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["i"],"id":14}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["m"],"id":15}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["a"],"id":16}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["l"],"id":17}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["s"],"id":18}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":[" "],"id":19}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["t"],"id":20}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["o"],"id":21}],[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":[" "],"id":22}],[{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["r"],"id":23}],[{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["o"],"id":24}],[{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["m"],"id":25}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["a"],"id":26}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["n"],"id":27}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":[" "],"id":28}],[{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["n"],"id":29}],[{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["u"],"id":30}],[{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["m"],"id":31}],[{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["e"],"id":32}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["r"],"id":33}],[{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["a"],"id":34}],[{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["l"],"id":35}],[{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["s"],"id":36}]]},"timestamp":1563293358735}
{"filter":false,"title":"key-pair-count-the-triplets.cpp","tooltip":"/CodeArray/key-pair-count-the-triplets.cpp","undoManager":{"mark":76,"position":76,"stack":[[{"start":{"row":0,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["#include <iostream>","","int main()","{","\tstd::cout << \"Hello from AWS Cloud9!\" << std::endl;","}"],"id":1},{"start":{"row":0,"column":0},"end":{"row":43,"column":1},"action":"insert","lines":["using namespace std;","int main()","{","\tint t;","\tcin>>t;","\twhile(t--)","\t{","\t\tint n;","\t\tcin>>n;","\t\tint c=0;","\t\tint a[n];","\t\tfor(int i=0;i<n;i++)","\t\t{","\t\t\tcin>>a[i];","\t\t}","\t\tsort(a,a+n);","\t\tfor(int i=n-1;i>0;i--)","\t\t{","\t\t\tint l=0,h=i-1;","\t\t\twhile(l<h&&l<i&&h>0)","\t\t\t{","\t\t\t\tif(a[l]+a[h]==a[i])","\t\t\t\t{","\t\t\t\t\tc++;","\t\t\t\t\tl++;","\t\t\t\t\th--;","//\t\t\t\t\tbreak;","\t\t\t\t}","\t\t\t\telse if(a[l]+a[h]<a[i])","\t\t\t\t{","\t\t\t\t\tl++;","\t\t\t\t}","\t\t\t\telse","\t\t\t\t{","\t\t\t\t\th--;","\t\t\t\t}","\t\t\t}","\t\t}","\t\tif(c!=0)","\t\t\tcout<<c<<endl;","\t\telse","\t\t\tcout<<\"-1\"<<endl;","\t}","}"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":20},"action":"remove","lines":["using namespace std;"],"id":2},{"start":{"row":0,"column":0},"end":{"row":4,"column":20},"action":"insert","lines":["#include<iostream>","#include<stdio.h>","","#include<bits/stdc++.h>","using namespace std;"]}],[{"start":{"row":4,"column":20},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["/"],"id":5}],[{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["*"],"id":6}],[{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["*"],"id":7}],[{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["/"],"id":8}],[{"start":{"row":6,"column":2},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":7,"column":0},"end":{"row":17,"column":6},"action":"insert","lines":["sor(a, a+n)","for i=0 to n"," s=0, end=n-1"," while(s<e)","  s=a[s]+a[e]","  if s==a[i]","   print a[i]=a[s]+a[e]","  else if s<a[i]","   s++","  else","   e--"],"id":11}],[{"start":{"row":18,"column":2},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":12}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":13}],[{"start":{"row":6,"column":2},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":14}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["c"],"id":15}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":["a"],"id":16}],[{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["n"],"id":17}],[{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":[" "],"id":18}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["a"],"id":19}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["l"],"id":20}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["s"],"id":21}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["o"],"id":22}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":[" "],"id":23}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["d"],"id":24}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["o"],"id":25}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":[" "],"id":26}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["b"],"id":27}],[{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["w"],"id":28}],[{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["l"],"id":29}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["o"],"id":30}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["e"],"id":31}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"remove","lines":["e"],"id":32}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"remove","lines":["o"],"id":33}],[{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"remove","lines":["l"],"id":34}],[{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"remove","lines":["w"],"id":35}],[{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["e"],"id":36}],[{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["l"],"id":37}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["o"],"id":38}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["w"],"id":39}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":[","],"id":40}],[{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":[" "],"id":41}],[{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["m"],"id":42}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["o"],"id":43}],[{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["d"],"id":44}],[{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["i"],"id":45}],[{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["f"],"id":46}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["u"],"id":47}],[{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["c"],"id":48}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["a"],"id":49}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"remove","lines":["a"],"id":50}],[{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"remove","lines":["c"],"id":51}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"remove","lines":["u"],"id":52}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["i"],"id":53}],[{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["c"],"id":54}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["a"],"id":55}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["t"],"id":56}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["i"],"id":57}],[{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["o"],"id":58}],[{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["n"],"id":59}],[{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":[" "],"id":60}],[{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["t"],"id":61}],[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["o"],"id":62}],[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["i"],"id":63}],[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":[" "],"id":64}],[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"remove","lines":[" "],"id":65}],[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"remove","lines":["i"],"id":66}],[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":[" "],"id":67}],[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["k"],"id":68}],[{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["e"],"id":69}],[{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["y"],"id":70}],[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["-"],"id":71}],[{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["o"],"id":72}],[{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"remove","lines":["o"],"id":73}],[{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["p"],"id":74}],[{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":["a"],"id":75}],[{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["i"],"id":76}],[{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":["r"],"id":77}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":4,"column":20},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1563063793749,"hash":"f7e40c946c43fed6c2fc57e60a728cb884a63ed4"}
{"filter":false,"title":"longest-substring-without-repeating-char-easy.py","tooltip":"/leet_facebook/array/longest-substring-without-repeating-char-easy.py","undoManager":{"mark":38,"position":38,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"",""],"id":1},{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["'''","1. Use brute force method to check if each substring is unique","2. for each substring check if all are unique","3. keep score of max unique substring in ans","'''","","","","def all_unique(str2):","    res=\"\"","    for i in str2:","        if i in res:","            return False","        else:","            res+=i","    return True","","","def longest_sub_str(str1):","    ans=0","    for i in range(len(str1)):","        for j in range(i+1, len(str1)):","            if all_unique(str1[i:j]):","                ans=max(ans,j-i)","    return ans","","","# s=\"darsh\"","# print(s[0:3])","print(longest_sub_str(\"abcabcbb\"))","",""]}],[{"start":{"row":4,"column":3},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":2}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":15},"action":"remove","lines":["# s=\"darsh\"","# print(s[0:3])"],"id":3},{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":31},"action":"remove","lines":["abcabcbb"],"id":4}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":29},"action":"insert","lines":["pwwkew"],"id":5}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":29},"action":"remove","lines":["pwwkew"],"id":6},{"start":{"row":26,"column":23},"end":{"row":26,"column":28},"action":"insert","lines":["bbbbb"]}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":28},"action":"remove","lines":["bbbbb"],"id":7}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":24},"action":"insert","lines":[" "],"id":8}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":24},"action":"remove","lines":[" "],"id":9}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":24},"action":"insert","lines":["c"],"id":10}],[{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"remove","lines":["1"],"id":11},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"remove","lines":["+"]}],[{"start":{"row":18,"column":9},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["n"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["="]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["l"]}],[{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["e"],"id":13},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":9},"end":{"row":19,"column":11},"action":"insert","lines":["()"],"id":14}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["s"],"id":15},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":12},"action":"remove","lines":["st"],"id":16},{"start":{"row":19,"column":10},"end":{"row":19,"column":14},"action":"insert","lines":["str1"]}],[{"start":{"row":20,"column":19},"end":{"row":20,"column":28},"action":"remove","lines":["len(str1)"],"id":17},{"start":{"row":20,"column":19},"end":{"row":20,"column":21},"action":"insert","lines":["n="]}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"remove","lines":["="],"id":18}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":35},"action":"remove","lines":["len(str1)"],"id":19},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["n"]}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["+"],"id":20},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["1"]}],[{"start":{"row":19,"column":15},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":["i"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":[" "],"id":22},{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"insert","lines":["n"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["="]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["="]},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["1"]},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":[":"]}],[{"start":{"row":20,"column":12},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["r"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["e"]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["t"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["u"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["r"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":[" "],"id":24}],[{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["1"],"id":25}],[{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"remove","lines":["c"],"id":26},{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["a"]},{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"insert","lines":["u"]}],[{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"insert","lines":["c"],"id":27}],[{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"remove","lines":["1"],"id":28},{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"remove","lines":["+"]}],[{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"remove","lines":["]"],"id":29},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["+"]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["1"]}],[{"start":{"row":23,"column":27},"end":{"row":23,"column":28},"action":"insert","lines":["+"],"id":30}],[{"start":{"row":23,"column":28},"end":{"row":23,"column":29},"action":"insert","lines":["1"],"id":31}],[{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"remove","lines":["1"],"id":32},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"remove","lines":["+"]}],[{"start":{"row":23,"column":23},"end":{"row":23,"column":26},"action":"remove","lines":["i, "],"id":33}],[{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["]"],"id":34}],[{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"remove","lines":["c"],"id":35}],[{"start":{"row":19,"column":15},"end":{"row":21,"column":16},"action":"remove","lines":["","    if n==1:","        return 1"],"id":36}],[{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"remove","lines":["u"],"id":37}],[{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["b"],"id":38}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["c"],"id":39},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["a"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":27,"column":27},"end":{"row":27,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1608415746000,"hash":"15b1370855189320da43186a33a3fd4fdf411f39"}
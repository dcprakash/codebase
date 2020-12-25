{"filter":false,"title":"permutations-of-a-given-string.py","tooltip":"/String/permutations-of-a-given-string.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":9,"column":17},"end":{"row":9,"column":19},"action":"insert","lines":["[]"],"id":41}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":[","],"id":42}],[{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["i"],"id":43}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["="],"id":44},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["a"]}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":25},"action":"insert","lines":["[]"],"id":45}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["i"],"id":46}],[{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["a"],"id":47}],[{"start":{"row":9,"column":27},"end":{"row":9,"column":29},"action":"insert","lines":["[]"],"id":48}],[{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["l"],"id":49}],[{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":[","],"id":50}],[{"start":{"row":9,"column":31},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":10,"column":0},"end":{"row":10,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["p"],"id":52},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["e"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["r"]}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":15},"action":"remove","lines":["per"],"id":53},{"start":{"row":10,"column":12},"end":{"row":10,"column":21},"action":"insert","lines":["permute()"]}],[{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["a"],"id":54},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":[","]}],[{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["l"],"id":55},{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["+"]},{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["!"]}],[{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"remove","lines":["!"],"id":56}],[{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["1"],"id":57},{"start":{"row":10,"column":25},"end":{"row":10,"column":26},"action":"insert","lines":[","]},{"start":{"row":10,"column":26},"end":{"row":10,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":10,"column":28},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":58},{"start":{"row":11,"column":0},"end":{"row":11,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":10,"column":28},"end":{"row":11,"column":31},"action":"insert","lines":["","            a[l],a[i]=a[i],a[l]"],"id":59}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":60},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["",""]},{"start":{"row":12,"column":12},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":12},"action":"remove","lines":["    "],"id":61},{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":19},"action":"remove","lines":["permute(a, 0, n-1) "],"id":64}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["p"],"id":65},{"start":{"row":16,"column":1},"end":{"row":16,"column":2},"action":"insert","lines":["r"]},{"start":{"row":16,"column":2},"end":{"row":16,"column":3},"action":"insert","lines":["i"]},{"start":{"row":16,"column":3},"end":{"row":16,"column":4},"action":"insert","lines":["n"]},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":5},"end":{"row":16,"column":7},"action":"insert","lines":["()"],"id":66}],[{"start":{"row":16,"column":6},"end":{"row":16,"column":25},"action":"insert","lines":["permute(a, 0, n-1) "],"id":67}],[{"start":{"row":16,"column":24},"end":{"row":16,"column":25},"action":"remove","lines":[" "],"id":68}],[{"start":{"row":0,"column":0},"end":{"row":16,"column":25},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"","","def permute(a,l,r):","    if l==r:","        return a","    else:","        for i in range(l,r+1):","            a[l],a[i]=a[i],a[l]","            permute(a,l+1,r)","            a[l],a[i]=a[i],a[l]","","string = \"ABC\"","n = len(string) ","a = list(string) ","print(permute(a, 0, n-1))"],"id":75},{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["# Python program to print all permutations with ","# duplicates allowed ","","def toString(List): ","\treturn ''.join(List) ","","# Function to print permutations of string ","# This function takes three parameters: ","# 1. String ","# 2. Starting index of the string ","# 3. Ending index of the string. ","def permute(a, l, r): ","\tif l==r: ","\t\tprint toString(a) ","\telse: ","\t\tfor i in xrange(l,r+1): ","\t\t\ta[l], a[i] = a[i], a[l] ","\t\t\tpermute(a, l+1, r) ","\t\t\ta[l], a[i] = a[i], a[l] # backtrack ","","# Driver program to test the above function ","string = \"ABC\"","n = len(string) ","a = list(string) ","permute(a, 0, n-1) ","","# This code is contributed by Bhavya Jain ",""]}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":42},"action":"remove","lines":["# This code is contributed by Bhavya Jain "],"id":76},{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":77}],[{"start":{"row":21,"column":44},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":78}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["r"],"id":79},{"start":{"row":22,"column":1},"end":{"row":22,"column":2},"action":"insert","lines":["e"]},{"start":{"row":22,"column":2},"end":{"row":22,"column":3},"action":"insert","lines":["s"]},{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"insert","lines":["="]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":6},"action":"insert","lines":["[]"],"id":80}],[{"start":{"row":11,"column":22},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":81},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["g"]}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["l"],"id":82},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["b"],"id":83},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["a"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["l"]}],[{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":[" "],"id":84},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["r"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["e"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":22},"end":{"row":12,"column":14},"action":"remove","lines":["","    global res"],"id":86}],[{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":[" "],"id":87}],[{"start":{"row":11,"column":21},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":88},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["g"],"id":89},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["l"]},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["b"],"id":90},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["a"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["l"]}],[{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":[" "],"id":91},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["r"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["e"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"remove","lines":[" "],"id":92}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["\t"],"id":93},{"start":{"row":12,"column":14},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":14},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":94},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":20},"end":{"row":15,"column":1},"action":"remove","lines":["","\t"],"id":95},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":[" "]}],[{"start":{"row":14,"column":19},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":96},{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"insert","lines":["\t\t"]}],[{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"remove","lines":["\t"],"id":97}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"remove","lines":[" "],"id":98}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["\t"],"id":99},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["\t"],"id":100},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "],"id":101},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "],"id":102},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":6},"end":{"row":16,"column":8},"action":"remove","lines":["","        "],"id":103}],[{"start":{"row":15,"column":6},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":104},{"start":{"row":16,"column":0},"end":{"row":16,"column":5},"action":"insert","lines":["\t    "]}],[{"start":{"row":16,"column":29},"end":{"row":17,"column":9},"action":"remove","lines":["","        \t"],"id":105}],[{"start":{"row":16,"column":29},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":106},{"start":{"row":17,"column":0},"end":{"row":17,"column":9},"action":"insert","lines":["\t        "]}],[{"start":{"row":17,"column":33},"end":{"row":18,"column":9},"action":"remove","lines":["","        \t"],"id":107},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"remove","lines":[" "]}],[{"start":{"row":17,"column":32},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":108},{"start":{"row":18,"column":0},"end":{"row":18,"column":9},"action":"insert","lines":["\t        "]}],[{"start":{"row":18,"column":28},"end":{"row":19,"column":9},"action":"remove","lines":["","        \t"],"id":109}],[{"start":{"row":18,"column":28},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":110},{"start":{"row":19,"column":0},"end":{"row":19,"column":9},"action":"insert","lines":["\t        "]}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"remove","lines":[" "],"id":111}],[{"start":{"row":18,"column":28},"end":{"row":19,"column":8},"action":"remove","lines":["","\t       "],"id":112},{"start":{"row":18,"column":27},"end":{"row":18,"column":28},"action":"remove","lines":[" "]}],[{"start":{"row":18,"column":27},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":113},{"start":{"row":19,"column":0},"end":{"row":19,"column":9},"action":"insert","lines":["\t        "]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":19},"action":"remove","lines":["toString(a)"],"id":114}],[{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":[" "],"id":115}],[{"start":{"row":14,"column":7},"end":{"row":14,"column":9},"action":"insert","lines":["()"],"id":116}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":19},"action":"insert","lines":["toString(a)"],"id":117}],[{"start":{"row":11,"column":21},"end":{"row":12,"column":14},"action":"remove","lines":["","    global res"],"id":118}],[{"start":{"row":0,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["# Python program to print all permutations with ","# duplicates allowed ","","def toString(List): ","\treturn ''.join(List) ","","# Function to print permutations of string ","# This function takes three parameters: ","# 1. String ","# 2. Starting index of the string ","# 3. Ending index of the string. ","def permute(a, l, r):","    if l==r:","\t\tprint(toString(a))","\telse:","\t    for i in xrange(l,r+1): ","\t        a[l], a[i] = a[i], a[l]","\t        permute(a, l+1, r)","\t        a[l], a[i] = a[i], a[l] # backtrack ","","","# Driver program to test the above function ","res=[]","string = \"ABC\"","n = len(string) ","a = list(string) ","permute(a, 0, n-1) ","",""],"id":119},{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["# Python program to print all permutations with ","# duplicates allowed ","","def toString(List): ","\treturn ''.join(List) ","","# Function to print permutations of string ","# This function takes three parameters: ","# 1. String ","# 2. Starting index of the string ","# 3. Ending index of the string. ","def permute(a, l, r): ","\tif l==r: ","\t\tprint toString(a) ","\telse: ","\t\tfor i in xrange(l,r+1): ","\t\t\ta[l], a[i] = a[i], a[l] ","\t\t\tpermute(a, l+1, r) ","\t\t\ta[l], a[i] = a[i], a[l] # backtrack ","","# Driver program to test the above function ","string = \"ABC\"","n = len(string) ","a = list(string) ","permute(a, 0, n-1) ","","# This code is contributed by Bhavya Jain ",""]}],[{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":[" "],"id":120}],[{"start":{"row":11,"column":21},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":121},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["s"],"id":122},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["="]}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":8},"action":"insert","lines":["\"\""],"id":123}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["h"],"id":124},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["e"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["l"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["l"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["o"]}],[{"start":{"row":0,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["# Python program to print all permutations with ","# duplicates allowed ","","def toString(List): ","\treturn ''.join(List) ","","# Function to print permutations of string ","# This function takes three parameters: ","# 1. String ","# 2. Starting index of the string ","# 3. Ending index of the string. ","def permute(a, l, r):","    s=\"hello\"","\tif l==r: ","\t\tprint toString(a) ","\telse: ","\t\tfor i in xrange(l,r+1): ","\t\t\ta[l], a[i] = a[i], a[l] ","\t\t\tpermute(a, l+1, r) ","\t\t\ta[l], a[i] = a[i], a[l] # backtrack ","","# Driver program to test the above function ","string = \"ABC\"","n = len(string) ","a = list(string) ","permute(a, 0, n-1) ","","# This code is contributed by Bhavya Jain ",""],"id":125},{"start":{"row":0,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["# Python program to print all permutations with ","# duplicates allowed ","","def toString(List): ","\treturn ''.join(List) ","","# Function to print permutations of string ","# This function takes three parameters: ","# 1. String ","# 2. Starting index of the string ","# 3. Ending index of the string. ","def permute(a, l, r): ","    global res","\tif l==r: ","\t\tres.append(toString(a))","\telse: ","\t\tfor i in xrange(l,r+1): ","\t\t\ta[l], a[i] = a[i], a[l] ","\t\t\tpermute(a, l+1, r) ","\t\t\ta[l], a[i] = a[i], a[l] # backtrack ","","# Driver program to test the above function ","res=[]","string = \"ABC\"","n = len(string) ","a = list(string) ","permute(a, 0, n-1) ","","# This code is contributed by Bhavya Jain ",""]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":126}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "],"id":127}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":128},{"start":{"row":11,"column":22},"end":{"row":12,"column":0},"action":"remove","lines":["",""]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":[" "]}],[{"start":{"row":11,"column":21},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":129},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":14},"end":{"row":13,"column":1},"action":"remove","lines":["","\t"],"id":130}],[{"start":{"row":12,"column":14},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":131},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":13},"end":{"row":14,"column":2},"action":"remove","lines":["","\t\t"],"id":132},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":[" "]}],[{"start":{"row":13,"column":12},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":133},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":31},"end":{"row":15,"column":1},"action":"remove","lines":["","\t"],"id":134}],[{"start":{"row":14,"column":31},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":135},{"start":{"row":15,"column":0},"end":{"row":15,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"remove","lines":["    "],"id":136}],[{"start":{"row":26,"column":19},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":137},{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"insert","lines":["p"]},{"start":{"row":27,"column":1},"end":{"row":27,"column":2},"action":"insert","lines":["r"]},{"start":{"row":27,"column":2},"end":{"row":27,"column":3},"action":"insert","lines":["i"]},{"start":{"row":27,"column":3},"end":{"row":27,"column":4},"action":"insert","lines":["n"]}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"remove","lines":["prin"],"id":138},{"start":{"row":27,"column":0},"end":{"row":27,"column":5},"action":"insert","lines":["print"]}],[{"start":{"row":27,"column":5},"end":{"row":27,"column":7},"action":"insert","lines":["()"],"id":139}],[{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["r"],"id":140},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["e"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":16,"column":25},"end":{"row":16,"column":26},"action":"remove","lines":[" "],"id":141}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"remove","lines":["x"],"id":142}],[{"start":{"row":15,"column":10},"end":{"row":16,"column":2},"action":"remove","lines":["","\t\t"],"id":143},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"remove","lines":[" "]}],[{"start":{"row":15,"column":9},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":144},{"start":{"row":16,"column":0},"end":{"row":16,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":16,"column":30},"end":{"row":17,"column":3},"action":"remove","lines":["","\t\t\t"],"id":145}],[{"start":{"row":16,"column":30},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":146},{"start":{"row":17,"column":0},"end":{"row":17,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":16,"column":30},"end":{"row":18,"column":3},"action":"remove","lines":["","            a[l], a[i] = a[i], a[l] ","\t\t\t"],"id":147}],[{"start":{"row":16,"column":30},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":148},{"start":{"row":17,"column":0},"end":{"row":17,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":17,"column":31},"end":{"row":18,"column":3},"action":"remove","lines":["","\t\t\t"],"id":149},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"remove","lines":[" "]}],[{"start":{"row":17,"column":30},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":150},{"start":{"row":18,"column":0},"end":{"row":18,"column":12},"action":"insert","lines":["            "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":16},"end":{"row":23,"column":16},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1608652398245,"hash":"8caed796ede94b1ed0bbae3309c8433ccd05e849"}
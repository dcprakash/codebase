{"filter":false,"title":"3-return-a-pair-with-maximum-product-in-array-of-integers.py","tooltip":"/Array/3-return-a-pair-with-maximum-product-in-array-of-integers.py","undoManager":{"mark":98,"position":98,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"",""],"id":1},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":[" "],"id":2}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":88},"action":"insert","lines":["https://www.geeksforgeeks.org/return-a-pair-with-maximum-product-in-array-of-integers/"],"id":3}],[{"start":{"row":0,"column":88},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["a"],"id":5},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["="]}],[{"start":{"row":3,"column":2},"end":{"row":3,"column":4},"action":"insert","lines":["[]"],"id":6}],[{"start":{"row":3,"column":3},"end":{"row":3,"column":19},"action":"insert","lines":["1, 4, 3, 6, 7, 0"],"id":7}],[{"start":{"row":3,"column":20},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["n"]},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["="]}],[{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["l"],"id":9},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":2},"end":{"row":4,"column":4},"action":"remove","lines":["le"],"id":10},{"start":{"row":4,"column":2},"end":{"row":4,"column":7},"action":"insert","lines":["len()"]}],[{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["a"],"id":11}],[{"start":{"row":4,"column":8},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":12}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["f"],"id":13},{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["i"]},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["n"]},{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["M"],"id":14},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["a"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["x"]}],[{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["P"],"id":15},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["r"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["o"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["d"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["K"]}],[{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["e"],"id":16},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["y"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["P"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["a"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["i"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":20},"action":"insert","lines":["()"],"id":17}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["a"],"id":18},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":[","]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["d"],"id":20},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["e"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":[" "],"id":21},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["f"]},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["i"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["n"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["d"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["m"],"id":22}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":8},"action":"remove","lines":["find"],"id":23},{"start":{"row":3,"column":4},"end":{"row":3,"column":22},"action":"insert","lines":["findMaxProdKeyPair"]}],[{"start":{"row":3,"column":22},"end":{"row":3,"column":24},"action":"insert","lines":["()"],"id":24}],[{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["a"],"id":25},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":[","]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":[":"],"id":26}],[{"start":{"row":3,"column":28},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":27},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["a"],"id":28},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["."]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["s"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["o"]}],[{"start":{"row":4,"column":6},"end":{"row":4,"column":8},"action":"remove","lines":["so"],"id":29},{"start":{"row":4,"column":6},"end":{"row":4,"column":12},"action":"insert","lines":["sort()"]}],[{"start":{"row":4,"column":12},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["s"],"id":31},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["u"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["m"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["1"]}],[{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"remove","lines":["1"],"id":32},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":["m"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"remove","lines":["u"]},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"remove","lines":["s"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["p"],"id":33},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["s"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["u"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["="],"id":34},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["a"]}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":12},"action":"insert","lines":["[]"],"id":35}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["n"],"id":36},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["-"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["2"]}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["2"],"id":37}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["1"],"id":38}],[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["*"],"id":39},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["a"]}],[{"start":{"row":5,"column":17},"end":{"row":5,"column":19},"action":"insert","lines":["[]"],"id":40}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["n"],"id":41}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["-"],"id":42},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["1"]}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["1"],"id":43}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["2"],"id":44}],[{"start":{"row":5,"column":22},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":45},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["n"],"id":46},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["="]}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"remove","lines":["="],"id":47}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["s"],"id":48},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["u"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["m"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["="]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["a"]}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":12},"action":"insert","lines":["[]"],"id":49}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["0"],"id":50}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["*"],"id":51},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["a"]}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":17},"action":"insert","lines":["[]"],"id":52}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["1"],"id":53}],[{"start":{"row":6,"column":18},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["i"],"id":55},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":[" "],"id":56},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["p"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":9},"action":"remove","lines":["ps"],"id":57},{"start":{"row":7,"column":7},"end":{"row":7,"column":11},"action":"insert","lines":["psum"]}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":[">"],"id":58},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["n"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":14},"action":"remove","lines":["ns"],"id":59},{"start":{"row":7,"column":12},"end":{"row":7,"column":16},"action":"insert","lines":["nsum"]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":[":"],"id":60}],[{"start":{"row":7,"column":17},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":61},{"start":{"row":8,"column":0},"end":{"row":8,"column":8},"action":"insert","lines":["        "]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["p"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["r"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["i"]}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":11},"action":"remove","lines":["pri"],"id":62},{"start":{"row":8,"column":8},"end":{"row":8,"column":15},"action":"insert","lines":["print()"]}],[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["a"],"id":63}],[{"start":{"row":8,"column":15},"end":{"row":8,"column":17},"action":"insert","lines":["[]"],"id":64}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["0"],"id":65}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":[","],"id":66},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["a"]}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":22},"action":"insert","lines":["[]"],"id":67}],[{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["1"],"id":68}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"remove","lines":[">"],"id":69}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["<"],"id":70}],[{"start":{"row":8,"column":24},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":71},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"remove","lines":["<"],"id":72}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":[">"],"id":73}],[{"start":{"row":8,"column":14},"end":{"row":8,"column":23},"action":"remove","lines":["a[0],a[1]"],"id":74},{"start":{"row":8,"column":14},"end":{"row":8,"column":27},"action":"insert","lines":["a[n-2]*a[n-1]"]}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["*"],"id":75}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":[","],"id":76}],[{"start":{"row":8,"column":28},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":77},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"remove","lines":["    "],"id":78}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["e"],"id":79},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["l"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":7},"action":"remove","lines":["els"],"id":80},{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"insert","lines":["else"]}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":[":"],"id":82}],[{"start":{"row":9,"column":9},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":83},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["p"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["r"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["i"]}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":11},"action":"remove","lines":["pri"],"id":84},{"start":{"row":10,"column":8},"end":{"row":10,"column":15},"action":"insert","lines":["print()"]}],[{"start":{"row":10,"column":14},"end":{"row":10,"column":23},"action":"insert","lines":["a[0]*a[1]"],"id":85}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"remove","lines":["*"],"id":86}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":[","],"id":87}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["/"],"id":88}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":["/"],"id":89}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["#"],"id":90}],[{"start":{"row":14,"column":21},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":91},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["a"]},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":["="]}],[{"start":{"row":15,"column":2},"end":{"row":15,"column":4},"action":"insert","lines":["[]"],"id":92}],[{"start":{"row":15,"column":3},"end":{"row":15,"column":23},"action":"insert","lines":["-1, -3, -4, 2, 0, -5"],"id":93}],[{"start":{"row":1,"column":0},"end":{"row":5,"column":15},"action":"insert","lines":["Input: arr[] = {1, 4, 3, 6, 7, 0}  ","Output: {6,7}  ","","Input: arr[] = {-1, -3, -4, 2, 0, -5} ","Output: {-4,-5}"],"id":94}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":2},"action":"insert","lines":["# "],"id":95},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":96}],[{"start":{"row":16,"column":8},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":97},{"start":{"row":16,"column":4},"end":{"row":16,"column":8},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":15,"column":24},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":15,"column":24},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":98},{"start":{"row":16,"column":0},"end":{"row":16,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":8},"action":"remove","lines":["    "],"id":99},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":21,"column":23},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":100}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":28},"end":{"row":13,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":17,"state":"start","mode":"ace/mode/python"}},"timestamp":1607197539684,"hash":"9f8490e6685746d8fa0fcb99bee853cbed4654a5"}
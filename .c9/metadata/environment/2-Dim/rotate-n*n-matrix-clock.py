{"changed":false,"filter":false,"title":"rotate-n*n-matrix-clock.py","tooltip":"/2-Dim/rotate-n*n-matrix-clock.py","undoManager":{"mark":16,"position":16,"stack":[[{"start":{"row":16,"column":27},"end":{"row":32,"column":24},"action":"remove","lines":["","\t\t\t","# \t\t\t# store current cell in temp variable ","# \t\t\tprint(N-x-1)","\t\t\ttemp = mat[x][y] ","","\t\t\t# move values from right to top ","\t\t\tmat[x][y] = mat[y][N-1-x] ","","\t\t\t# move values from bottom to right ","\t\t\tmat[y][N-1-x] = mat[N-1-x][N-1-y] ","","\t\t\t# move values from left to bottom ","\t\t\tmat[N-1-x][N-1-y] = mat[N-1-y][x] ","","\t\t\t# assign temp to left ","\t\t\tmat[N-1-y][x] = temp "],"id":2},{"start":{"row":16,"column":27},"end":{"row":21,"column":37},"action":"insert","lines":["","                temp=matrix[x][y]","                matrix[x][y]=matrix[N-1-y][x]","                matrix[N-1-y][x]=matrix[N-1-x][N-1-y]","                matrix[N-1-x][N-1-y]=matrix[y][N-1-x]","                matrix[y][N-1-x]=temp"]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":3},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":17,"column":17},"end":{"row":17,"column":23},"action":"remove","lines":["matrix"],"id":4},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["a"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["m"]}],[{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"remove","lines":["m"],"id":5},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"remove","lines":["a"]}],[{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["m"],"id":6},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["a"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":20},"action":"remove","lines":["mat"],"id":8},{"start":{"row":9,"column":17},"end":{"row":9,"column":23},"action":"insert","lines":["matrix"]}],[{"start":{"row":17,"column":17},"end":{"row":17,"column":20},"action":"remove","lines":["mat"],"id":9},{"start":{"row":17,"column":17},"end":{"row":17,"column":23},"action":"insert","lines":["matrix"]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":10},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":11},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":12},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["\t"],"id":13},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["\t"]},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["\t"]},{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"insert","lines":["\t"]},{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["\t"]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["\t"],"id":14},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["\t"]},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["\t"]},{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"insert","lines":["\t"]},{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["\t"]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["\t"],"id":15},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["\t"]},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["\t"]},{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"insert","lines":["\t"]},{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["\t"]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["#"],"id":16}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":[" "],"id":17}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":57},"action":"insert","lines":["https://leetcode.com/problems/rotate-image/submissions/"],"id":18}],[{"start":{"row":2,"column":57},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":19}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":0},"end":{"row":6,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1608951002195}
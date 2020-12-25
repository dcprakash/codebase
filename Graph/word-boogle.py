t = 1
for i in range(0,t):
    n = 4
    string = "GEEKS FOR QUIZ GO"
    ls = list(string.split(' '))
    print "ls: {}".format(ls)
    length = "3 3" #Not used in this code but, can check word if its smaller than length
    length = list(length.split(' '))
    print "length: {}".format(length)
    list_char = "G I Z U E K Q S E V R Y"
    list_char = list(list_char.split(' '))
    print "list_char: {} \n".format(list_char)
    words = []
    for j in ls:
        sample = []
        for k in list_char:
            sample.append(k)
        word = ""
        for y in j:
            if(y in sample):
                word+=y
                p = sample.index(y)
                sample[p] = ''
            else:
                break
        if(word==j and word not in words):
            words.append(word)
    words.sort()
    if(len(words)>0):
        word = ""
        for j in range(0,len(words)-1):
            word+=words[j]+" "
        word+=words[len(words)-1]
        print "Word is the: {}".format(word)
    else:
        print(-1)
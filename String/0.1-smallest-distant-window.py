# https://www.geeksforgeeks.org/smallest-window-contains-characters-string/
# same as *longest-substring-without-repeating-characters

def smallWindowEff(mystr):
    mystr=mystr.strip()
    a={}
    c=0
    n=len(mystr)
    for i in mystr:
        if(i not in a):
            a[i]=1
            c+=1
    # print(a)
    temp_c=c
    out=-1
    while(c<n):
        for i in range(0,n-c+1,1):
            substr1=mystr[i:i+c]
            # print(set(list(substr1)))
            # print(len(set(list(substr1))))
            if(len(set(list(substr1)))==temp_c):
                out=c
                break
            
        if(out!=-1):
            break
        c+=1
    
    if(out==-1):
        print(n)
    else:
        print(out)
        

# DOES NOT WORK, we should also consider subsrting. Not just unique characters
def smallWindow(mystr):
    wd={}
    for i in mystr:
        if i not in wd:
            wd[i]=1
    print(len(wd.keys()))


if __name__=='__main__':
    smallWindowEff("aabcbcdbca")
    smallWindow("aabcbcdbca")
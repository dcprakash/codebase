"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/solution/
"""


def removeDuplicates(s):
    n=len(s)
    t=[]
    for i in range(1,n):
        if s[i-1]!=s[i]:
            t.append(s[i-1])
    t.append(s[n-1])
    return "".join(t)
            

def removeDuplicatesKchar(s,k):
    stack=[]
    n=len(s)
    for i in range(n):
        if i==0 or s[i]!=s[i-1]:
            stack.append(1)
        else:
            top_count=stack[-1]+1
            if top_count==k:
                s=s[i-k::k+1]+s[k+2::]
                # s=s[0::4]+s[5::]
            else:
                stack[-1]=top_count
    return "".join(stack)
    #. 012345
    # s="abbbef"
    # print(s[0::4]+s[5::]) i=3


s="abbc"
# print(removeDuplicates(list(s)))

#.   01234
s = "deeeb"
k = 3
print(removeDuplicatesKchar(s,k))



'''
c++
string removeDuplicates(string s, int k) {
    stack<int> counts;
    for (int i = 0; i < s.size(); ++i) {
        if (i == 0 || s[i] != s[i - 1]) {
            counts.push(1);
        } else if (++counts.top() == k) {
            counts.pop();
            s.erase(i - k + 1, k);
            i = i - k;
        }
    }
    return s;
}
'''
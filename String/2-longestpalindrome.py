'''
https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
https://leetcode.com/problems/palindromic-substrings/solution/
'''

def longestpalindrome(s):
    n=len(s)
    max_len=1
    start=0
    for i in range(1,n):
        if n%2==0:
            l=i-1
            h=i
        else:
            l=i-1
            h=i+1
            
        while l>=0 and h<n and s[l]==s[h]:
            if h-l+1>max_len:
                max_len=h-l+1
                start=l
            l-=1
            h+=1

    res=""
    for i in range(start,start+max_len):
        res+=s[i]
    return res

s = "Geek"
print(longestpalindrome(s))


'''
public String longestPalindrome(String s) {
    if (s == null || s.length() < 1) return "";
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}

private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--;
        R++;
    }
    return R - L - 1;
}
'''
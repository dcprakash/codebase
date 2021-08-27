'''
https://leetcode.com/problems/monotone-increasing-digits/solution/
'''

class Solution:
    def monotoneIncreasingDigits(self, N):
        def monotone_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        # new = list(map(int, str(N))) 
        new=list(str(N))
        if monotone_increasing(new):
            return N
        
        count=1
        while True:
            num=N-count
            count+=1
            if monotone_increasing(list(str(num))):
                return num
    


# N = 603253281
# N=987654321
N = 332

s=Solution()
print(s.monotoneIncreasingDigits(N))

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solution/
# divisible by number i.e., 60 efficient approach on leetcode
# division

def numPairsDivisibleBy60(time):
    count=0
    n=len(time)
    for i in range(n):
        for j in range(i+1,n):
            if (time[i]+time[j])%60==0:
                count+=1
    return count


def numPairsDivisibleBy60Efficient(time):
    count=0
    n=len(time)
    sumarr=[]
    for i in range(n):
        for j in range(i+1,n):
            sumarr.append(time[i]+time[j])
    for s in sumarr:
        if s%60==0:
            count+=1
    return count
    

time = [30,20,150,100,40]
# print(numPairsDivisibleBy60(time))
print(numPairsDivisibleBy60Efficient(time))

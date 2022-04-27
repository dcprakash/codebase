'''
https://leetcode.com/problems/time-based-key-value-store/

'''

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyStore = {} # key : list of [val, timestamp]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        print(self.keyStore)

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        print("res {0}".format(res))
        print("values {0}".format(values))
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


'''
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        A = self.M.get(key, None)
        if A is None: return ""
        # to keep the list in sorted order after insertion of each element.
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
'''
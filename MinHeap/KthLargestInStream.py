"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
class KthLargest(object):
    def __init__(self, k, nums):
        self.nums = []
        heapify(self.nums)
        for i in  range(0, max(len(nums), k)): #Have atleast k elements
            # we fill void to accomodate below input and avoid list index out of range
            # ["KthLargest","add","add","add","add","add"]
            # [[1,[]],[-3],[-2],[-4],[0],[4]]
            heappush(self.nums, nums[i] if i<len(nums) else float('-inf')) #Fill the void with -inf
            if i >= k: #Maintain only k elements
                heappop(self.nums)
                
    def add(self, val):
        heappushpop(self.nums, val) #Will add k+1 element and remove (k+1)th element
        return self.nums[0] # Will always be the kth largest
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
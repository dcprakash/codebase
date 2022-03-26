'''
merge sort
mergesort
LinkedList/sort-linked-list.py

'''


class Solution:
    def sortList(self, arr):
        if len(arr)<=1: return arr
        mid=len(arr)//2
        left = self.sortList(arr[:mid])
        right = self.sortList(arr[mid:])
        return self.merge(left, right)
    
    def merge(self, list1, list2):
        left_index, right_index = 0, 0
        result = []
        while left_index < len(list1) and right_index < len(list2):
            if list1[left_index] < list2[right_index]:
                result.append(list1[left_index])
                left_index += 1
            else:
                result.append(list2[right_index])
                right_index += 1

        result += list1[left_index:]
        result += list2[right_index:]
        return result
        

                
            
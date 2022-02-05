# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        return False
        
            
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        values = {}
        for i in range(len(nums)):
            if nums[i] not in values:
                values[nums[i]] = 1
            else:
                values[nums[i]] += 1
        for key in values.keys():
            if values[key] == 1:
                return key
        
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n%2
            n //= 2
        return count

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # merge in reverse order
        # start from end
        last = m + n - 1
        # while there are things in the array
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m += -1
            else:
                nums1[last] = nums2[n-1]
                n += -1
            last += -1
        # edge case
        while n > 0:
            nums1[last] = nums2[n-1]
            n += -1
            last += -1
        


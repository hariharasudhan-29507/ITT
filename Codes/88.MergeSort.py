class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        size = len(nums1)
        nums1[:] = nums1[:m] + nums2
        for k in range(size):
            for i in range(size-1):
                if nums1[i] > nums1[i+1]:
                    nums1[i] ,nums1[i+1]= nums1[i+1],nums1[i] 
            
            

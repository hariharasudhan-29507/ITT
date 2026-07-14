class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = val + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res

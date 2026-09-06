class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = []
        for i in nums:
            if i not in x:
                x.append(i)
            else:
                return True   # Replaces print and exit
        return False  
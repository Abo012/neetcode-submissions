class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        # check if it is a start of a sequence
        for n in nums:
            if(n-1) not in numSet:
                sequence = 0
                while(n+sequence) in numSet:
                    sequence += 1
                longest = max(sequence, longest)
        return longest

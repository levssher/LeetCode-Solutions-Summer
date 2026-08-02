class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            dif=target-nums[i]
            if dif in hashmap:
                return [i,hashmap[dif]]
            hashmap[nums[i]]=i
        return [] #no solution
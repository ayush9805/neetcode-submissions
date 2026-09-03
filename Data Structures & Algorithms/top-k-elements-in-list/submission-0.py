class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i] = 1
        sortitem = sorted(frequency.items(),key= lambda pair:pair[1],reverse=True)
        return [pair[0] for pair in sortitem[:k]]
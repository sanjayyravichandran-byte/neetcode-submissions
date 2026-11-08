class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        
        for num in nums:
            track[num] = track.get(num,0) + 1
        output = sorted(track.keys(), key=track.get, reverse=True)[:k]
        return output
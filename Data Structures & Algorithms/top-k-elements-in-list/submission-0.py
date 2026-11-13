class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}

        for num in nums:

            if num not in track:
                track[num] = 1
            else:
                track[num] += 1

        result = []
        for _ in range(k):
            best_num = None
            best_count = 0

            for num in track:
                if track[num] > best_count:
                    best_count = track[num]
                    best_num = num

            result.append(best_num)

            del track[best_num]

        return result
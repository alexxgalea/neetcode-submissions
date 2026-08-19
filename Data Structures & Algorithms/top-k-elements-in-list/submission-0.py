class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        app = {}
        for n in nums:
            if n not in app:
                app[n] = 1
            else:
                app[n] += 1
        sorted_app = sorted(app.keys(), key=lambda n: app[n], reverse=True)

        return sorted_app[:k]
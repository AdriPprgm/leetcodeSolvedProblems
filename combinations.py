#type: ignore

class Solution:
    def power_set(self, s: list[int]) -> list[list[int]]:
        if not s:
            return [[]]
        recursive: list[list[int]] = self.power_set(s[:-1])
        return recursive + [x + [s[-1]] for x in recursive]

    def combine(self, n: int, k: int) -> List[List[int]]:
        l: list[int] = []
        for i in range(1, n + 1):
            l.append(i)

        return [x for x in self.power_set(l) if len(x) == k]
        
#type: ignore
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        instructions = []
        for i in range(1, n + 1):
            if stack == target:
                break
            stack.append(i)
            instructions.append("Push")
            if i not in target:
                instructions.append("Pop")
                stack.pop(-1)
        print(stack)
        return instructions
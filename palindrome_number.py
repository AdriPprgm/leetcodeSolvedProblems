class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        return num_string[::-1] == num_string
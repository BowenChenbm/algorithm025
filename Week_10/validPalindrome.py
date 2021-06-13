#680. 验证回文字符串 Ⅱ
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome_check(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return palindrome_check(low + 1, high) or palindrome_check(low, high - 1)
        return True

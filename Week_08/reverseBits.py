#190. 颠倒二进制位
#颠倒给定的 32 位无符号整数的二进制位。

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(1, 33):
            result |= (n & 1) << (32 - i)
            n >>= 1
        return result

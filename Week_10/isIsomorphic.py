#205. 同构字符串
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #1, return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        #2, index
        # for i in range(len(s)):
        #     if s.index(s[i]) != t.index(t[i]):
        #         return False
        # return True
        # two hashmap:
        s_to_t = {}
        t_to_s = {}
        for i in range(len(s)):
            if s[i] not in s_to_t: s_to_t[s[i]] = t[i]
            elif s[i] in s_to_t and s_to_t[s[i]] != t[i]: return False
            if t[i] not in t_to_s: t_to_s[t[i]] = s[i]
            elif t[i] in t_to_s and t_to_s[t[i]] != s[i]: return False
        return True

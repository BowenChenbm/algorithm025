#242. 有效的字母异位词

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        # return collections.Counter(s) == collections.Counter(t)
        dic1, dic2 = {}, {}
        for item1 in s:
            dic1[item1] = dic1.get(item1, 0) + 1
        for item2 in t:
            dic2[item2] = dic2.get(item2, 0) + 1
        return dic1 == dic2

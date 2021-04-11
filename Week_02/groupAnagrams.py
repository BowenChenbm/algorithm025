# 49. 字母异位词分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 输入:["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: 
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]

# 思路: 遍历一遍，使用哈希表存储每种字符串的情况

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = dict() #存放字符串种类，key为sorted后的字符串，value为原字符串
        result = []
        for i, sr in enumerate(strs):
            sort_str = str(sorted(sr))
            if sort_str not in temp:
                temp[sort_str] = []
            temp[sort_str].append(strs[i])
        return [temp[key] for key in temp]


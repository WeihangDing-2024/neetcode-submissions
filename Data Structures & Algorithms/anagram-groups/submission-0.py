class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            sort_str = "".join(sorted(word))
            if sort_str in dic:
                dic[sort_str].append(word)
            else:
                dic[sort_str] = [word]
        res = []
        for key, value in dic.items():
            res.append(value)
        return res
        
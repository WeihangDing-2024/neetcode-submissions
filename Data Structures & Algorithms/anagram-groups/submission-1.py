class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getOrd(char):
            return ord(char) - ord('a')
        freq_dict = defaultdict(list) # key: freq tuple, value: list of word
        for word in strs:
            freq = [0] * 26
            for char in word:
                idx = getOrd(char)
                freq[idx] += 1
            freq_dict[tuple(freq)].append(word)
        res = []
        for key, value in freq_dict.items():
            res.append(value)



        
        
        
        return res
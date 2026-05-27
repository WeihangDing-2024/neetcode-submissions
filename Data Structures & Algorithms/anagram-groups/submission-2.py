class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # helper
        def getOrd(char):
            return ord(char) - ord('a')

        res = []
        freq_dict = {}
        for single_str in strs:
            freq = [0 for _ in range(26)]
            for char in single_str:
                freq[getOrd(char)] += 1
            
            for i, val in enumerate(freq):
                freq[i] = str(val)

            freq_tup = tuple(freq)
            if freq_tup in freq_dict:
                freq_dict[freq_tup].append(single_str)
            else:
                freq_dict[freq_tup] = [single_str]

        
        # for key, value in freq_dict.items():
        #     res.append(value)
        return list(freq_dict.values())
            
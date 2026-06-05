class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        max_freq = 0
        freq_dict = defaultdict(int)
        i = 0
        for j in range(len(s)):
            freq_dict[s[j]] += 1
            max_freq = max(max_freq, freq_dict[s[j]])
            while j - i + 1 > max_freq + k:
                freq_dict[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
            
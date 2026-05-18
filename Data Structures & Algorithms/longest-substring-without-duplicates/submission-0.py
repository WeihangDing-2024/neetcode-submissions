class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: 
            return len(s)

        low, high = 0, 1
        freq_dict = defaultdict(int)
        freq_dict[s[low]] += 1

        max_len = 1

        while high < len(s):
            curr_char = s[high]
            if freq_dict[curr_char] >= 1:
                max_len = max(max_len, high - low)
                while s[low] != curr_char:
                    freq_dict[s[low]] = max(0, freq_dict[s[low]] - 1)
                    low += 1
                low += 1
                freq_dict[curr_char] = 1
                high += 1
            else:
                freq_dict[curr_char] += 1
                high += 1

        max_len = max(max_len, high - low)
        return max_len

        
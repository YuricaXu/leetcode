class Solution:
    def longestNiceSubstring(self, s: str) -> str:#build a set of all letters
        if len(s) < 2: return ""
        chars = set(list(s))
        for i in range(len(s)):#go through the string, check if it has an invalid letter 
            if not (s[i].lower() in chars and s[i].upper() in chars):
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s2 if len(s2) > len(s1) else s1  
        return s    
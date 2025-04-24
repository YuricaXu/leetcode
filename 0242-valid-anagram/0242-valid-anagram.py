class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0]*26# Initialize a list of size 26 to count character frequencies (a-z)
        for i in s:
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            # If any count is not zero, the strings are not anagrams
            if record[i] != 0:
                return False

        return True
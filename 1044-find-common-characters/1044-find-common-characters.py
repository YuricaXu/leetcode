class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        tmp = collections.Counter(words[0])
        l = []
        for i in range(1,len(words)):
            # apply
            tmp = tmp & collections.Counter(words[i])

        for j in tmp:
            v = tmp[j]
            while(v):
                l.append(j)
                v -= 1
        return l
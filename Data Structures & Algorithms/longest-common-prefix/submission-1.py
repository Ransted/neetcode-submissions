class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ""
        lcp = []
        n = len(strs)
        for i in range(len(strs[0])):
            for s in strs:
                if s[i] != strs[0][i]:
                    return res
            lcp.append(strs[0][i])
            res = str("".join(lcp))
        return res

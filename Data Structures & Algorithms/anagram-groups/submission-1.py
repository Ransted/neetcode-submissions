class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for n in strs:
            key = "".join(sorted(n))
            if key not in di:
                di[key] = []
            di[key].append(n)
        return list(di.values())

        

        
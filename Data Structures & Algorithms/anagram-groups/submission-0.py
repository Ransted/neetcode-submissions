class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        li = []
        for i,n in enumerate(strs):
            sorted_str = "".join(sorted(n))
            if sorted_str not in di:
                di[sorted_str] = [i]
            else:
                di[sorted_str].append(i)
        for j in di.values():
            tmp = []
            for k in j:
                tmp.append(strs[k])
            li.append(tmp)
        return li

        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        # for s in strs:
        #     freq = [0] * 26

        #     for ch in s:
        #         freq[ord(ch) - ord('a')] += 1

        #     groups[tuple(freq)].append(s)

        for i in range(len(strs)):
            sig = tuple(sorted(strs[i]))

            groups[sig].append(strs[i])

        return list(groups.values())
import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = collections.defaultdict(list)
        for s in strs:
            anagram_map[tuple(sorted(s))].append(s)
        return list(anagram_map.values())
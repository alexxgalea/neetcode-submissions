class Solution:
    def char_apps(self, str1: str):
        char_app = [0] * 26
        for s in str1:
            char_app[ord(s) - ord('a')] += 1
        
        return char_app

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str in strs:
            key = tuple(self.char_apps(str)) #lista imutabila de vector fix de 32
            if key not in groups:
                groups[key] = []
            groups[key].append(str)
        
        return list(groups.values())

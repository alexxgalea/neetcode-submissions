class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        ap = [0] * 26
        
        for i in range(len(s)):
            ap[ord(s[i]) - 97] += 1
            ap[ord(t[i]) - 97] -= 1
            
        return all(x == 0 for x in ap)
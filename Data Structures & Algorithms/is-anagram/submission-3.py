class Solution:
    def apIndex(self, c: str) -> int:
        return ord(c) - ord('a')

    def isAnagram(self, s: str, t: str) -> bool:
        ap = [0] * 26 # letters in alphabet

        if len(s) != len(t):
            return False
        for letter in s:
            ap[self.apIndex(letter)] += 1
        
        for letter in t:
            ap[self.apIndex(letter)] -= 1
        
        if all(i == 0 for i in ap):
            return True
        
        return False
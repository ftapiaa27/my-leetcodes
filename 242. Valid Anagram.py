from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            elif i in hash:
                hash[i] += 1
        for i in t:
            if i in hash:
                hash[i] -= 1
                if hash[i] < 0:
                    return False
        return max(hash.values()) == 0

    def isAnagram2(self, s: str, t: str):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram3(self, s: str, t: str):
        if len(s) != len(t):
            return False
        hash_s, hash_t = {}, {}
        for i in range (len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        return hash_s == hash_t

    def isAnagram4(self, s: str, t: str):
        return Counter(s) == Counter(t)

solution = Solution()
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s, t))

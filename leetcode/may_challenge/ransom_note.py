
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        did = set()
        for ch in ransomNote:
            if ch in did:
                continue
            if ransomNote.count(ch) > magazine.count(ch):
                return False
            did.add(ch)
        return True


    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(ch) <= magazine.count(ch) for ch in set(ransomNote))

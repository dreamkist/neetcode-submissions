class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_text = "".join(ch.lower() for ch in s if ch.isalnum())
        start = 0
        
        end = len(clean_text) - 1

        while start < end:         
            if clean_text[start] != clean_text[end]:
                return False
            start += 1
            end -= 1

        return True
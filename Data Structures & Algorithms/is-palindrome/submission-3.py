class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        1. Loop through string
        2. See if value is a letter using isalpha()
        4. If it is, lowercase it and add to empty array
        5. Create a reversed array
        6. If both are same: palindrome
        
        temp = []

        for e in s:
            if e.isalnum():
                temp.append(e.lower())
        
        reversed_temp = temp[::-1]

        if temp == reversed_temp:
            return True
        
        return False
        '''

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True

        
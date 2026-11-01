class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        1. Loop through string
        2. See if value is a letter using isalpha()
        4. If it is, lowercase it and add to empty array
        5. Create a reversed array
        6. If both are same: palindrome
        '''
        temp = []

        for e in s:
            if e.isalnum():
                temp.append(e.lower())
        
        reversed_temp = temp[::-1]

        if temp == reversed_temp:
            return True
        
        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Algorithm:
                - Store characters in s into hashmap with the number of ocurrences
                    - Loop through s
                    - If letter is inside hashmap --> Increase count by 1
                    - If not --> Add to hashmap with count = 1
                - Do same for t
                - Compare both hash maps
        '''

        if len(s) != len(t):
            return False

        s_map = {
            #Value: Count
        }

        t_map = {}

        for e in s:
            if e in s_map:
                s_map[e] += 1
            else:
                s_map[e] = 1
        
        for e in t:
            if e in t_map:
                t_map[e] += 1
            else:
                t_map[e] = 1

        if s_map == t_map:
            return True

        return False
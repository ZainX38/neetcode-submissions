class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Create a dict
        Key: number of letters used
        If number of letter used match in two words, add it as the values
        If not, 

        '''
        groups = {}

        for word in strs:
            count = [0] * 26    # Creates an array of 26 0s

            for c in word:
                # Increases the count of the position inside count corresponding to the letter
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)  # Lists cannot be keys, so convert to tuple

            # Creates empty list with the key and then appends the value
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)

        return list(groups.values())
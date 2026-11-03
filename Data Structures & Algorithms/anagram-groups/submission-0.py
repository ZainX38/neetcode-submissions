class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Loop through each word
        Sort it and see if the sorted version is inside dict
        If inside, add it as the value
        If not, create new key using the sorted word
        Convert dict to array and return
        '''

        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())
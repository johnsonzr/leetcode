class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        longer = ''
        word = False
        for x in s:
            if x != ' ':
                longer += x
                word = True
            if x == ' ' and word == True:
                break

        return len(longer)
    
# Runtime: 12ms 
# Beats: 62.29%

# Memory: 11.87MB
# Beats: 50.72% 
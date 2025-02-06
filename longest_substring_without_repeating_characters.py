def lengthOfLongestSubstring(s):
    if s == '':
        return 0
    ans = []
    sub = ''
    for i in range(len(s)):
        if s[i] not in sub: 
            sub += s[i]
            ans.append(len(sub))
        else:
            a = s[0:i].rfind(s[i])
            sub = s[a+1:i+1]
            ans.append(len(sub))
    return max(ans)

example = 'abcabcbb'
lengthOfLongestSubstring(example)



# Runtime: 23ms Beats: 33%
# Memory: 17.8MB  Beats 45%

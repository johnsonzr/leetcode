strs0 = ["flower","flow","flight"]
strs1 = ["dog","racecar","car"]
strs2 = [""]
strs3 = ["a"]
strs4 = ["ab", "a"]
strs5 = ["abab","aba",""]



def longestCommonPrefix(strs):
    y = 0
    var = ''
    try:
        while len(set(var)) < 2:
            var = ''
            for x in strs:
                var += x[y]
            y += 1
    except IndexError:
        if '' in strs:
            y = 0
        else:
            y += 1
    if y < 2:
        ans = ''
    else:
        ans = strs[0][0:y-1]
    print(ans)

print(longestCommonPrefix(strs5))
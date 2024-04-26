needle = 'sad'
haystack = 'sadbutsad'

if needle not in haystack:
    return -1
if needle in haystack:
    nl = len(needle)
    hl = len(haystack)
    for y in range(hl - nl + 1):
        if needle in haystack[y:nl + y]:
            return y

# Runtime: 24ms
# Beats 98%

# Memory: 16.5 MB
# Beats 90.4%

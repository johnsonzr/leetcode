def find_needle_in_haystack(needle, haystack):
    if needle not in haystack:
        return -1

    if needle in haystack:
        nl = len(needle)
        hl = len(haystack)
        for y in range(hl - nl + 1):
            if needle in haystack[y:nl + y]:
                return y

needle = 'sad'
haystack = 'sadbutsad'
print(find_needle_in_haystack(needle, haystack))

# Runtime: 24ms
# Beats 98%

# Memory: 16.5 MB
# Beats 90.4%

code = [5, 7, 1, 4]
k = 3



code_wrap = code + code

if k > -1:
    for x in range(len(code)):
        code[x] = sum(code_wrap[x+1:k+x+1])
else:
    for x in range(len(code)):
        y = (len(code_wrap) // 2)
        code[x] = sum(code_wrap[k+x+y:x+y])
return code




# Runtime: 0ms
# Beats: 100.00%

# Memory: 16.63MB
# Beats: 62.2%
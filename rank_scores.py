scores = pd.DataFrame({'score': [3.5, 3.65, 4, 3.85, 4, 3.65],
          'id': [1, 2, 3, 4, 5, 6]})


import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values('score', ascending = False)
    scores = scores.drop(columns = 'id')

    scores['rank'] = 1
    y = 0

    for x in range(int(scores.size / 2)):

        prev = scores.iloc[x-1, 0]
        cur = scores.iloc[x, 0]

        if str(prev) == str(cur):
            scores.iloc[x, 1] = scores.iloc[x-1, 1]
            y += 1
        else:
            scores.iloc[x, 1] = x + 1 - y
    return scores


# Runtime: 438ms
# Beats: 58.48%

# Memory: 67.25MB
# Beats: 55.24%

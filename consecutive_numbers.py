import pandas as pd

logs = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6],
          'num': [1, 1, 1, 2, 1, 2]})
logs2 = pd.DataFrame({'id': [1, 2, 4, 5, 6, 7],
          'num': [1, 1, 1, 1, 2, 1]})



logs = logs.set_index('id')
logs = logs.sort_values(by = 'id')
answer = pd.DataFrame({'ConsecutiveNums': []})
c = None
x = None
y = 0

for key, val in logs.iterrows():
    val = val[0]
    if val == c and key - x == 1:
        y += 1
        x = key
    else:
        y = 1
        c = val
        x = key
    if y == 3:
        answer.loc[len(answer)] = {'ConsecutiveNums': val}
            
print(answer.drop_duplicates())


  # Runtime: 557ms
  # Beats: 56%

  # Memory: 65.9MB
  # Beats: 86%


import pandas as pd

employee = pd.DataFrame({'id': [1, 2, 3],
          'salary': [100, 200, 300]})



def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.sort_values(by = 'salary')
    employee = employee.drop_duplicates(subset = 'salary')
    if len(employee) == 1:
        sal = None
    else:
        sal = employee.iloc[-2, 1]

    SecondHighestSalary = pd.DataFrame({'SecondHighestSalary': [sal]})
    return SecondHighestSalary

print(second_highest_salary(employee))

  # Runtime: 382ms
  # Beats: 73%

  # Memory: 65.5MB
  # Beats: 89%

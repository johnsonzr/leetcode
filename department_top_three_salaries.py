import pandas as pd

# employee = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6, 7],
#           'name': ['Joe', 'Henry', 'Sam', 'Max', 'Janet', 'Randy', 'Will'],
#           'salary': [85000, 80000, 60000, 90000, 69000, 85000, 70000],
#           'departmentId': [1, 2, 2, 1, 1, 1, 1]})

# department = pd.DataFrame({'id': [1, 2],
#           'name': ['IT', 'Sales']})

# employee = pd.DataFrame({'id': [],
#           'name': [],
#           'salary': [],
#           'departmentId': []})

# department = pd.DataFrame({'id': [],
#           'name': []})


employee = pd.DataFrame({'id': [1, 2, 3, 4],
          'name': ['Joe', 'Ralph', 'Joel', 'Tracy'],
          'salary': [60000, 30000, 50000, 55000],
          'departmentId': [1, 1, 1, 1]})

department = pd.DataFrame({'id': [1],
          'name': ['IT']})


try:
    answer = pd.DataFrame()
    department = department.sort_values(by = 'id')
    departments = list(department['name'])

    for x in range(len(department)):
        dep = employee[employee.departmentId == x + 1]
        salaries = set(dep.salary)
        salaries = list(salaries)
        salaries.sort(reverse=True)
        for sal in salaries[:3]:
            s = dep[dep.salary == sal]
            answer = pd.concat([answer, s], axis = 0)

        answer.loc[answer.departmentId == x+1, 'Department'] = departments[x]

    answer = answer.rename(columns = {'name':'Employee', 'salary':'Salary'})
    answer = answer.drop(columns = ['id', 'departmentId'])
except Exception:
    answer = pd.DataFrame({'Employee': [], 'Salary': [], 'Department': []})
print(answer)


# Runtime: 655ms
# Beats: 33.13%

# Memory: 70.6MB
# Beats: 5.07%

# Difficulty: Hard



#### The names of the employees are recorded under the shift 

import pandas as pd
import numpy as np
file = "Holiday Schedule Ranking 2019.csv"
data = pd.read_csv(file, header=0, index_col=0)
cols = []
for col in data.columns:
    cols.append(col)

num_dates = len(cols)
schedule = pd.DataFrame(np.full((3, num_dates), "replace"), columns=cols)
positions = ["one", "two", "three"]
schedule.index = positions
emp_days_dict = {}

for emp, row in data.iterrows():

    day_count = 0
    sorted_list_of_dates = row.sort_values(axis=0).index.tolist()

    for x in range(13):

        if day_count == 2:
            break
        elif schedule.loc["one", sorted_list_of_dates[x]] == "replace":
            schedule.loc["one", sorted_list_of_dates[x]] = emp
            day_count += 1
    for x in range(13):

        if day_count == 2:
            break
        elif schedule.loc["two", sorted_list_of_dates[x]] == "replace":
            schedule.loc["two", sorted_list_of_dates[x]] = emp
            day_count += 1
    for x in range(13):

        if day_count == 2:
            break
        elif schedule.loc["three", sorted_list_of_dates[x]] == "replace":
            schedule.loc["three", sorted_list_of_dates[x]] = emp
            day_count += 1
position = ["1st shift", "2nd Shift", "3rd Shift"]
schedule.index = position
print(schedule)
schedule.to_csv(r'C:\Users\Akintoye Asaolu\OneDrive - Baylor University\Spring Semester\Advanced Python\Test\schedule.csv', index=True, header=True)

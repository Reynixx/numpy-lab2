import numpy as np
import pandas as pd

df = pd.DataFrame({
    "name": ["Анна", "Борис", "Виктор", "Галина", "Дмитрий", "Елена"],
    "department": ["IT", "IT", "HR", "Sales", "IT", "Sales"],
    "salary": [95000, 65000, 62000, 78000, 120000, 72000],
    "bonus": [15000, np.nan, 5000, 12000, np.nan, 8000],
    "hire_date": ["2021-03-15", "2022-07-01", "2020-11-20", "2023-01-10", "2019-05-12", "2022-09-30"]
})

it_employees = df.loc[df["department"] == "IT", ["name", "salary"]]
print("2.1 Name и salary для IT:")
print(it_employees)

print("\n2.2 Первые 3 строки и 2 столбца (iloc):")
print(df.iloc[:3, :2])

high_earners = df[df["salary"] > 70000]
print("\n2.3 Зарплата > 70000:")
print(high_earners)

df["total_comp"] = df["salary"] + df["bonus"].fillna(0)
print("\n2.4 Столбец total_comp:")
print(df[["name", "salary", "bonus", "total_comp"]])

df = df.drop(columns=["hire_date"])
print("\n2.5 После удаления hire_date:")
print(df.columns.tolist())
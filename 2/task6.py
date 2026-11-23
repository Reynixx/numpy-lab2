import pandas as pd

df = pd.DataFrame({
    "name": ["Анна", "Борис", "Виктор", "Галина", "Дмитрий", "Елена", "Жан", "Зоя"],
    "department": ["IT", "IT", "HR", "Sales", "IT", "Sales", "HR", "IT"],
    "salary": [95000, 72000, 62000, 85000, 120000, 74000, 79000, 82000],
    "bonus": [15000, 10000, 5000, 12000, 25000, 8000, 6000, 18000]
})
df["total_comp"] = df["salary"] + df["bonus"]

top_3 = df.nlargest(3, "total_comp")[["name", "department", "total_comp"]]
print("6.1 Топ-3 по total_comp:")
print(top_3)

dept_means = df.groupby("department", as_index=False).agg(
    mean_salary=("salary", "mean"),
    mean_bonus=("bonus", "mean")
)
print("\n6.2 Средняя зарплата и средний бонус по отделам:")
print(dept_means)

share_above_75k = (df["salary"] > 75000).groupby(df["department"]).mean()
print("\n6.3 Доля сотрудников с salary > 75000 по отделам:")
print(share_above_75k)
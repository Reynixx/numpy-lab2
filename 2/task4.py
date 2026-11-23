import pandas as pd

df = pd.DataFrame({
    "name": ["Анна", "Борис", "Виктор", "Галина", "Дмитрий", "Елена", "Жан"],
    "department": ["IT", "IT", "HR", "Sales", "IT", "Sales", "HR"],
    "salary": [95000, 105000, 62000, 78000, 120000, 68000, 70000],
    "bonus": [15000, 10000, 5000, 12000, 20000, 8000, 7000]
})

avg_salary = df.groupby("department")["salary"].mean()
print("4.1 Средняя зарплата по отделам:")
print(avg_salary)

stats_by_dept = df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    max_bonus=("bonus", "max"),
    employees_count=("name", "count")
)
print("\n4.2 Агрегация по отделам:")
print(stats_by_dept)

pivot = df.pivot_table(index="department", values="salary", aggfunc="mean")
print("\n4.3 Сводная таблица:")
print(pivot)

sorted_dept = avg_salary.sort_values(ascending=False)
print("\n4.4 По убыванию средней зарплаты:")
print(sorted_dept)
import pandas as pd

df = pd.DataFrame({
    "name": ["Анна", "Борис", "Виктор", "Галина"],
    "department": ["IT", "IT", "HR", "Sales"],
    "salary": [95000, 105000, 62000, 78000]
})

managers = pd.DataFrame({
    "department": ["IT", "HR", "Sales"],
    "manager": ["Алексей", "Мария", "Сергей"]
})

merged = df.merge(managers, on="department", how="left")

new_row = pd.DataFrame([{
    "name": "Дмитрий",
    "department": "IT",
    "salary": 120000,
    "manager": "Алексей"
}])

result = pd.concat([merged, new_row], ignore_index=True)
result = result.reset_index(drop=True)

print("5.1-5.4 Итоговый DataFrame после merge и concat:")
print(result)
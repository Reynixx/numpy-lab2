import numpy as np
import pandas as pd

df = pd.DataFrame({
    "name": ["Анна", "Борис", "Виктор", "Галина", "Дмитрий", "Елена", "Жан"],
    "department": ["IT", "IT", "HR", "Sales", "IT", "Sales", "Design"],
    "salary": [95000.0, np.nan, 62000.0, 78000.0, 115000.0, 68000.0, np.nan],
    "bonus": [15000.0, 10000.0, np.nan, 12000.0, np.nan, 8000.0, 5000.0]
})

print("3.1 Пропуски до обработки:")
print(df.isna().sum())

df["salary"] = df["salary"].fillna(df.groupby("department")["salary"].transform("mean"))
df["bonus"] = df["bonus"].fillna(0)
df = df.dropna(subset=["salary"])

print("\n3.2-3.4 Пропуски после обработки:")
print(df.isna().sum())
print("\nИтоговый DataFrame:")
print(df)
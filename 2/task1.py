import pandas as pd

s = pd.Series([15, 28, 42, 67, 89], index=["a", "b", "c", "d", "e"], name="scores")
print("Series:")
print(s)

df = pd.DataFrame({
    "name": ["Анна", "Борис", "Виктор", "Галина", "Дмитрий", "Елена"],
    "department": ["IT", "IT", "HR", "Sales", "IT", "Sales"],
    "salary": [95000, 88000, 62000, 78000, 120000, 68000],
    "bonus": [15000, 10000, 5000, 12000, 20000, 8000]
})

print("\nПервые строки:")
print(df.head(3))

print("\nПоследние строки:")
print(df.tail(2))

print("\nИнформация о типах данных:")
df.info()

print("\nСтатистика:")
print(df.describe())
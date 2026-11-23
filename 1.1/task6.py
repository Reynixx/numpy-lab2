import numpy as np

arr = np.arange(20)
print("6.1a Каждый 3-й элемент с индекса 1:", arr[1::3])
print("6.1b Элементы с 5-го по 15-й (не включая 15) в обратном порядке:", arr[14:4:-1])
print("6.1c Последние 5 элементов в обратном порядке:", arr[-1:-6:-1])

rng = np.random.default_rng(42)
mat6 = rng.integers(0, 10, size=(6, 6))
print("\nМатрица 6x6:\n", mat6)
print("6.2a Подматрица строки 2-4, столбцы 1-3 (включительно):\n", mat6[2:5, 1:4])
print("6.2b Главная диагональ через np.diagonal:", np.diagonal(mat6))

idx = np.arange(6)
chess_mask = (idx[:, None] + idx[None, :]) % 2 == 0
print("6.2c Шахматный узор (чётная сумма индексов):\n", mat6[chess_mask])

a = np.array([10, 20, 30, 40, 50, 60])
m = np.arange(12).reshape(3, 4)

print("\n6.3a Элементы a по индексам [0, 2, 4]:", a[[0, 2, 4]])
print("6.3b Попарно элементы (0,1), (1,3), (2,0):", m[[0, 1, 2], [1, 3, 0]])
print("6.3c Блок 2x2 из строк [0, 2] и столбцов [1, 3]:\n", m[np.ix_([0, 2], [1, 3])])

x = rng.standard_normal(1000)
count_gt_1 = np.sum(x > 1)
print("\n6.4a Количество элементов > 1:", count_gt_1)

x_no_neg = x.copy()
x_no_neg[x_no_neg < 0] = 0
print("6.4b Отрицательные заменены на 0 (минимум теперь):", x_no_neg.min())

x_sign_flip = x.copy()
diff_signs = (x[:-2] * x[2:]) < 0
x_sign_flip[1:-1][diff_signs] = 0
print("6.4c Обнулено элементов при смене знака соседей:", np.sum(diff_signs))
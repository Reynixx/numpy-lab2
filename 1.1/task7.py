import os
import time
import numpy as np

mm = np.memmap("big.dat", dtype="float32", mode="w+", shape=(50000, 200))
mm[:] = np.random.rand(50000, 200).astype("float32")
mm.flush()
del mm

print("Размер файла:", os.path.getsize("big.dat"))
print("Ожидаемый размер:", 50000 * 200 * 4)

mm_r = np.memmap("big.dat", dtype="float32", mode="r", shape=(50000, 200))
mins = []
maxs = []
sums = []

for i in range(0, 50000, 5000):
    chunk = mm_r[i:i+5000]
    mins.append(chunk.min())
    maxs.append(chunk.max())
    sums.append(chunk.sum())

print("Min:", min(mins))
print("Max:", max(maxs))
print("Mean:", sum(sums) / (50000 * 200))
del mm_r

a_c = np.ones((3000, 3000), order="C")
a_f = np.ones((3000, 3000), order="F")

t0 = time.time()
s = 0
for i in range(3000):
    for j in range(3000):
        s += a_c[i, j]
print("C-order по строкам:", time.time() - t0)

t0 = time.time()
s = 0
for j in range(3000):
    for i in range(3000):
        s += a_c[i, j]
print("C-order по столбцам:", time.time() - t0)

t0 = time.time()
s = 0
for i in range(3000):
    for j in range(3000):
        s += a_f[i, j]
print("F-order по строкам:", time.time() - t0)

t0 = time.time()
s = 0
for j in range(3000):
    for i in range(3000):
        s += a_f[i, j]
print("F-order по столбцам:", time.time() - t0)

n = 10_000_000
a = np.ones(n, dtype="float64") * 2.0
b = np.ones(n, dtype="float64") * 1.0
la = a.tolist()
lb = b.tolist()

t0 = time.time()
r1 = [(x + y) / (x - y + 1) for x, y in zip(la, lb)]
print("Python list:", time.time() - t0)

t0 = time.time()
r2 = (a + b) / (a - b + 1)
print("NumPy:", time.time() - t0)

t0 = time.time()
buf1 = np.empty(n, dtype="float64")
buf2 = np.empty(n, dtype="float64")
r3 = np.empty(n, dtype="float64")
np.add(a, b, out=buf1)
np.subtract(a, b, out=buf2)
np.add(buf2, 1, out=buf2)
np.divide(buf1, buf2, out=r3)
print("NumPy out=:", time.time() - t0)
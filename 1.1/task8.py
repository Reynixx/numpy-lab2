import time
import numpy as np
from scipy.sparse import coo_matrix, random

rng = np.random.default_rng(42)

row = rng.integers(0, 5000, size=10_000)
col = rng.integers(0, 5000, size=10_000)
data = rng.random(10_000)

mat_coo = coo_matrix((data, (row, col)), shape=(5000, 5000))
mat_csr = mat_coo.tocsr()

print(f"8.1 Исходных записей: {len(data)} | COO nnz: {mat_coo.nnz} | CSR nnz: {mat_csr.nnz}")
print("    Разница из-за дубликатов координат (суммирование при CSR):", mat_coo.nnz - mat_csr.nnz)

sp_4k = random(4000, 4000, density=0.005, format="csr", dtype=np.float64, random_state=rng)
dn_4k = sp_4k.toarray()
vec_4k = rng.random(4000)

dense_bytes = dn_4k.nbytes
csr_bytes = sp_4k.data.nbytes + sp_4k.indices.nbytes + sp_4k.indptr.nbytes

repeats = 200
t0 = time.perf_counter()
for _ in range(repeats):
    _ = dn_4k @ vec_4k
t_dense = (time.perf_counter() - t0) / repeats

t0 = time.perf_counter()
for _ in range(repeats):
    _ = sp_4k @ vec_4k
t_csr = (time.perf_counter() - t0) / repeats

print(f"\n8.2 Матрица 4000x4000 (density=0.005):")
print(f"    Память Dense : {dense_bytes / (1024**2):.2f} МБ")
print(f"    Память CSR   : {csr_bytes / (1024**2):.2f} МБ")
print(f"    Время Dense  : {t_dense * 1000:.4f} мс")
print(f"    Время CSR    : {t_csr * 1000:.4f} мс")

n_bench = 2000
x_bench = rng.random(n_bench)
densities = [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]

print("\n8.3 Сравнение времени A @ x при n=2000:")
print(f"{'Density':<10} | {'CSR (мс)':<12} | {'Dense (мс)':<12} | {'CSR быстрее?'}")
print("-" * 55)

crossover_density = None
for d in densities:
    sp_m = random(n_bench, n_bench, density=d, format="csr", dtype=np.float64, random_state=rng)
    dn_m = sp_m.toarray()

    iters = 100
    t0 = time.perf_counter()
    for _ in range(iters):
        _ = sp_m @ x_bench
    t_s = ((time.perf_counter() - t0) / iters) * 1000

    t0 = time.perf_counter()
    for _ in range(iters):
        _ = dn_m @ x_bench
    t_d = ((time.perf_counter() - t0) / iters) * 1000

    csr_wins = t_s < t_d
    if not csr_wins and crossover_density is None:
        crossover_density = d

    print(f"{d:<10} | {t_s:<12.4f} | {t_d:<12.4f} | {'Да' if csr_wins else 'Нет'}")

print("Точка, где sparse начинает проигрывать dense:", crossover_density)
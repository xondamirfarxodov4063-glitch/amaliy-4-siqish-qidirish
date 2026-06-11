# ============================================================
# AMALIY ISH - 7: Mashinali o'qitish. Gradiyent pastlash.
# Farxodov Xondamir | D2OT1-25 KBI | FDTU
# ============================================================

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print("=" * 65)
print("AMALIY ISH - 7: Mashinali o'qitish. Gradiyent pastlash.")
print("=" * 65)

# ============================================================
# 1. DARSLIKDAGI ASOSIY MISOL
# ============================================================
print("\n1. DARSLIK NAMUNASI — darslikdagi kod")
print("-" * 55)

data = {
    'X1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'X2': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'y':  [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
}
df = pd.DataFrame(data)
X  = df[['X1', 'X2']]
y  = df['y']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_sc, y_train)
y_pred = model.predict(X_test_sc)

print(f"  MSE : {mean_squared_error(y_test, y_pred):.6f}")
print(f"  MAE : {mean_absolute_error(y_test, y_pred):.6f}")
print(f"  R²  : {r2_score(y_test, y_pred):.6f}")

# ============================================================
# 2. IXTIYORIY MASALA — UY NARXINI BASHORAT QILISH
# ============================================================
print("\n2. IXTIYORIY MASALA — Uy narxini bashorat qilish")
print("-" * 55)

np.random.seed(42)
n = 100
maydoni = np.random.randint(40, 200, n).astype(float)
xonalar = np.random.randint(1, 6, n).astype(float)
qavat   = np.random.randint(1, 16, n).astype(float)
yoshi   = np.random.randint(1, 40, n).astype(float)
narx    = maydoni*2.5 + xonalar*10 + qavat*3 - yoshi*1.5 + np.random.normal(0, 8, n)

df2 = pd.DataFrame({
    'Maydon':  maydoni,
    'Xonalar': xonalar,
    'Qavat':   qavat,
    'Yoshi':   yoshi,
    'Narx':    narx
})

print(f"  Dataset: {n} ta uy  |  Ustunlar: Maydon, Xonalar, Qavat, Yoshi => Narx")
print(f"  Narx diapazoni: {narx.min():.1f} – {narx.max():.1f} mln so'm")

X2 = df2[['Maydon','Xonalar','Qavat','Yoshi']]
y2 = df2['Narx']

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y2, test_size=0.2, random_state=42)

# ============================================================
# 3. NORMALLASH
# ============================================================
print("\n3. MA'LUMOTLARNI NORMALLASH (StandardScaler)")
print("-" * 55)

sc2 = StandardScaler()
X2_train_sc = sc2.fit_transform(X2_train)
X2_test_sc  = sc2.transform(X2_test)

# Y ni ham normallash (SGD uchun)
y_mean, y_std = y2_train.mean(), y2_train.std()
y2_train_sc = (y2_train - y_mean) / y_std
y2_test_sc  = (y2_test  - y_mean) / y_std

print(f"  Normallashdan OLDIN — Maydon: ort={X2_train['Maydon'].mean():.1f}, std={X2_train['Maydon'].std():.1f}")
print(f"  Normallashdan SO'NG  — Maydon: ort={X2_train_sc[:,0].mean():.4f}, std={X2_train_sc[:,0].std():.4f}")

# ============================================================
# 4. CHIZIQLI REGRESSIYA
# ============================================================
print("\n4. CHIZIQLI REGRESSIYA MODELI (LinearRegression)")
print("-" * 55)

lr = LinearRegression()
lr.fit(X2_train_sc, y2_train)
y_pred_lr = lr.predict(X2_test_sc)

mse_lr = mean_squared_error(y2_test, y_pred_lr)
mae_lr = mean_absolute_error(y2_test, y_pred_lr)
r2_lr  = r2_score(y2_test, y_pred_lr)

print(f"  Koeffitsiyentlar:")
for name, coef in zip(X2.columns, lr.coef_):
    print(f"    {name:<10}: {coef:+.4f}")
print(f"  Intercept : {lr.intercept_:.4f}")
print(f"\n  MSE  : {mse_lr:.4f}")
print(f"  MAE  : {mae_lr:.4f}")
print(f"  RMSE : {np.sqrt(mse_lr):.4f}")
print(f"  R²   : {r2_lr:.4f}  ({r2_lr*100:.1f}%)")

# ============================================================
# 5. SGD REGRESSIYA (target ham normalized)
# ============================================================
print("\n5. GRADIYENT PASTLASH — SGDRegressor")
print("-" * 55)

sgd = SGDRegressor(max_iter=2000, tol=1e-4, learning_rate='invscaling',
                   eta0=0.01, random_state=42)
sgd.fit(X2_train_sc, y2_train_sc)
y_pred_sgd_sc = sgd.predict(X2_test_sc)
y_pred_sgd    = y_pred_sgd_sc * y_std + y_mean   # teskari normallash

mse_sgd = mean_squared_error(y2_test, y_pred_sgd)
mae_sgd = mean_absolute_error(y2_test, y_pred_sgd)
r2_sgd  = r2_score(y2_test, y_pred_sgd)

print(f"  max_iter=2000, learning_rate=invscaling, eta0=0.01")
print(f"  MSE  : {mse_sgd:.4f}")
print(f"  MAE  : {mae_sgd:.4f}")
print(f"  RMSE : {np.sqrt(mse_sgd):.4f}")
print(f"  R²   : {r2_sgd:.4f}  ({r2_sgd*100:.1f}%)")

# ============================================================
# 6. QOLYOZMA GRADIYENT PASTLASH
# ============================================================
print("\n6. QOLYOZMA GRADIYENT PASTLASH (NumPy)")
print("-" * 55)

Xg = X2_train_sc
yg = y2_train_sc.values
m  = len(Xg)

W = np.zeros(Xg.shape[1])
b = 0.0
lr_rate = 0.05
epochs  = 1000

history = []
for epoch in range(epochs):
    y_hat = Xg @ W + b
    err   = y_hat - yg
    loss  = np.mean(err**2)
    history.append(loss)
    dW = (2/m) * Xg.T @ err
    db = (2/m) * err.sum()
    W -= lr_rate * dW
    b -= lr_rate * db

print(f"  Boshlang'ich yo'qotish (epoch 1)   : {history[0]:.4f}")
print(f"  100-epochdagi yo'qotish            : {history[99]:.4f}")
print(f"  500-epochdagi yo'qotish            : {history[499]:.4f}")
print(f"  Yakuniy yo'qotish (epoch {epochs})  : {history[-1]:.4f}")
print(f"  Kamayish: {history[0]:.4f} → {history[-1]:.4f}  ({(1-history[-1]/history[0])*100:.1f}% yaxshilandi)")

# ============================================================
# 7. SOLISHTIRISH JADVALI
# ============================================================
print("\n7. MODELLARNI SOLISHTIRISH")
print("-" * 55)
print(f"  {'Model':<20} {'MSE':>10} {'MAE':>8} {'RMSE':>8} {'R²':>8}")
print(f"  {'-'*20} {'-'*10} {'-'*8} {'-'*8} {'-'*8}")
print(f"  {'LinearRegression':<20} {mse_lr:>10.3f} {mae_lr:>8.3f} {np.sqrt(mse_lr):>8.3f} {r2_lr:>8.4f}")
print(f"  {'SGDRegressor':<20} {mse_sgd:>10.3f} {mae_sgd:>8.3f} {np.sqrt(mse_sgd):>8.3f} {r2_sgd:>8.4f}")

# ============================================================
# 8. YANGI UY UCHUN BASHORAT
# ============================================================
print("\n8. YANGI UYLAR UCHUN BASHORAT")
print("-" * 55)

new_data = pd.DataFrame({
    'Maydon':  [85.0, 120.0, 55.0],
    'Xonalar': [3.0,   4.0,   2.0],
    'Qavat':   [5.0,   8.0,   2.0],
    'Yoshi':   [10.0,  3.0,  25.0]
})
new_sc   = sc2.transform(new_data)
pred_new = lr.predict(new_sc)

labels = ['Kichik (55m²)', "O'rta (85m²)", 'Katta (120m²)']
for i, row in new_data.iterrows():
    print(f"  Uy {i+1}: {int(row.Maydon)}m², {int(row.Xonalar)} xona, "
          f"{int(row.Qavat)}-qavat, {int(row.Yoshi)} yil")
    print(f"     => Bashorat: {pred_new[i]:.2f} mln so'm")

print("\n" + "=" * 65)
print("XULOSA")
print("=" * 65)
print(f"  1. Darslik namunasi   : R²=1.000 (mukammal chiziqli bog'liqlik)")
print(f"  2. LinearRegression   : R²={r2_lr:.4f} ({r2_lr*100:.1f}% aniqlik)")
print(f"  3. SGDRegressor       : R²={r2_sgd:.4f} ({r2_sgd*100:.1f}% aniqlik)")
print(f"  4. Qolyozma GD        : yo'qotish {(1-history[-1]/history[0])*100:.1f}% kamaydi")
print(f"  5. Normallash         : Ort=0.0000, Std=1.0000 ga keltirildi")
print("=" * 65)

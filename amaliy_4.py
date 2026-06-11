import gzip
import shutil
import os
import time

print("=" * 60)
print("AMALIY ISH - 4: Ma'lumotlarni Siqish va Qidirish")
print("=" * 60)

# ============================================================
# 1-TOPSHIRIQ: Ma'lumotlarni siqishga misol
# ============================================================
print("\n📦 1-TOPSHIRIQ: Ma'lumotlarni Gzip bilan siqish")
print("-" * 50)

# Asl ma'lumot
data = b"Bu ma'lumotlarni siqish orqali saqlash usuli. " * 100

# Ma'lumotni faylga yozish
with open('data.txt', 'wb') as f:
    f.write(data)

asl_hajm = os.path.getsize('data.txt')
print(f"Asl fayl hajmi     : {asl_hajm} bytes")

# Gzip yordamida siqish
with open('data.txt', 'rb') as f_in:
    with gzip.open('data.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

siqilgan_hajm = os.path.getsize('data.txt.gz')
print(f"Siqilgan fayl hajmi: {siqilgan_hajm} bytes")
print(f"Tejash koeffitsiyenti: {(1 - siqilgan_hajm/asl_hajm)*100:.1f}%")
print("✅ Gzip yordamida siqilgan ma'lumotlar 'data.txt.gz' faylida saqlandi.")

# ============================================================
# 2-TOPSHIRIQ: Siqilgan faylni ochish va tekshirish
# ============================================================
print("\n🔓 2-TOPSHIRIQ: Siqilgan faylni ochish va tekshirish")
print("-" * 50)

with gzip.open('data.txt.gz', 'rb') as f:
    file_content = f.read()

print(f"O'qilgan ma'lumot hajmi: {len(file_content)} bytes")
print(f"Birinchi 80 belgi: {file_content[:80]}")

# Tekshirish: asl ma'lumot va qayta tiklangan ma'lumot bir xilmi?
if file_content == data:
    print("✅ Tekshiruv muvaffaqiyatli: Asl va tiklangan ma'lumotlar bir xil!")
else:
    print("❌ Xato: Ma'lumotlar farq qiladi!")

# ============================================================
# QIDIRISH ALGORITMLARI
# ============================================================
print("\n🔍 QIDIRISH ALGORITMLARI")
print("-" * 50)

# Linear Search
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test
massiv = list(range(1, 10001))  # 1 dan 10000 gacha
target = 7777

# Linear Search
start = time.perf_counter()
linear_result = linear_search(massiv, target)
linear_time = time.perf_counter() - start

# Binary Search
start = time.perf_counter()
binary_result = binary_search(massiv, target)
binary_time = time.perf_counter() - start

print(f"Massiv: 1 dan 10000 gacha, qidirilayotgan: {target}")
print(f"\n📌 Linear Search:")
print(f"   Topilgan indeks: {linear_result}")
print(f"   Vaqt: {linear_time*1000:.4f} ms")

print(f"\n📌 Binary Search:")
print(f"   Topilgan indeks: {binary_result}")
print(f"   Vaqt: {binary_time*1000:.4f} ms")

speedup = linear_time / binary_time if binary_time > 0 else 0
print(f"\n⚡ Binary Search {speedup:.1f}x marta tezroq!")

# ============================================================
# XULOSA
# ============================================================
print("\n" + "=" * 60)
print("📊 XULOSA")
print("=" * 60)
print(f"1. Gzip siqish {(1 - siqilgan_hajm/asl_hajm)*100:.1f}% joy tejadi")
print(f"2. Yo'qotishsiz siqish: ma'lumotlar to'liq tiklandi ✅")
print(f"3. Linear Search: O(n) - har bir element tekshiriladi")
print(f"4. Binary Search: O(log n) - tezroq, lekin tartiblangan massiv kerak")
print("=" * 60)


x = 5
y = 5

# Besar (>)
hasil_besar = x > y
print(f"Apakah nilai dari {x} lebih besar (>) dari {y} ? {hasil_besar}")
# Kecil (<)
hasil_kecil = x < y
print(f"Apakah nilai dari {x} lebih kecil (<) dari {y} ? {hasil_kecil}")
# Besar sama dengan (>=)
hasil_besar_sama_dengan = x >= y
print(f"Apakah nilai dari {x} lebih besar sama dengan (>=) dari {y} ? {hasil_besar_sama_dengan}")
# Kecil sama dengan (<=)
hasil_kecil_sama_dengan = x <= y
print(f"Apakah nilai dari {x} lebih kecil sama dengan (<=) dari {y} ? {hasil_kecil_sama_dengan}")
# Sama dengan (==)
hasil_sama_dengan = x == y
print(f"Apakah nilai dari {x} sama dengan (==) dari {y} ? {hasil_sama_dengan}")
# Tidak sama dengan (!=)
hasil_tidak_sama_dengan = x != y
print(f"Apakah nilai dari {x} tidak sama dengan (!=) dari {y} ? {hasil_tidak_sama_dengan}")

# Logical and (&&)
hasil_logical_and = (x > 0) and (y > 0)
print(f"Apakah nilai dari kondisi 1 dan kondisi 2 terpenuhi? {hasil_logical_and}")
# Logical or (||)
hasil_logical_or = (x > 0) or (y < 0)
print(f"Apakah nilai dari kondisi 1 atau kondisi 2 terpenuhi? {hasil_logical_or}")
# Logical not (!)
hasil_logical_not = not (x > 0)
print(f"Apakah nilai dari kondisi 1 tidak sama dengan nilai asli ? {hasil_logical_not}")  

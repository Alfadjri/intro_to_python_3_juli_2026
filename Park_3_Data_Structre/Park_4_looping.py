# for 
print("======For Looping======")
# range(start , stop , langkahnya)
for kata in range(2):
    print(f"angka ke {kata} : A")
print("======For Looping using List======")
buahs = ["apel","jeruk","mangga","pisang","anggur","semangka","melon"]
nomer = 0 
for buah in buahs:
    print(f"buah {nomer}: {buah}") 
    nomer += 1 

print("======While Looping======")
i = 2
while i < 5:
    print(f"angka ke {i} : B")
    i += 1

print("======Continue and Break======")
angka = 1
while angka <= 100:
    if angka % 2 == 0:
        angka += 1
        continue # melewati iterasi saat ini jika angka genap
    print(f"angka ke {angka}")
    angka += 1
    if angka <= 30:
        break # menghentikan perulangan jika angka lebih besar dari 30
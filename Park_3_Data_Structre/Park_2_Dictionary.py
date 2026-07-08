# Sekolah
# Create Inisialisasi Dictionary
sekolah = {
    "kelas" : 10,
    "jurusan" : ["IPA","IPS","Bahasa"],
}
# Read
print("===== menampilkan Dictionary =====")
print(f"Dictionary : {sekolah}")
print(f"Kelas Berapa ini ? : {sekolah["kelas"]}")
print(f"Bagimana ambil jurusan IPS : {sekolah["jurusan"][1]}")

# Add
sekolah["nama"] = "SMK Negeri 1"
print(f"Dictionary : {sekolah}")
# Update
sekolah["kelas"] = 11
print(f"Dictionary : {sekolah}")
# Delete
del sekolah["nama"]
print(f"Dictionary : {sekolah}")

data_kariawan = [
    {
        "nama": "Budi",
        "umur": 25,
        "alamat": "Jakarta",
    },
    {
        "nama": "Siti",
        "umur": 30,
        "alamat": "Bandung",
    },
    {
        "nama": "Andi",
        "umur": 28,
        "alamat": "Surabaya",
    },
    {
        "nama": "Rina",
        "umur": 22,
        "alamat": "Medan",
    }
]

# Type Function
# Void
# function yang tidak menghasilkan nilai balik atau return
def print_format(nama,umur,alamat):
    print(f"Nama   : {nama}")
    print(f"Umur   : {umur}")
    print(f"Alamat : {alamat}")
    print("===================================")


print("===== menampilkan data kariawan =====")
print_format(data_kariawan[0]["nama"],data_kariawan[0]["umur"],data_kariawan[0]["alamat"])
print_format(data_kariawan[1]["nama"],data_kariawan[1]["umur"],data_kariawan[1]["alamat"])
print_format(data_kariawan[2]["nama"],data_kariawan[2]["umur"],data_kariawan[2]["alamat"])
print_format(data_kariawan[3]["nama"],data_kariawan[3]["umur"],data_kariawan[3]["alamat"])

# non Void
# function yang menghasilkan nilai balik atau return
def menghitung_tahun_lahir(umur):
    tahun_lahir = 2026 - umur
    return tahun_lahir

print("===== menampilkan umur kariawan =====")
print(f"tahun lahir dari {data_kariawan[0]['nama']} adalah {menghitung_tahun_lahir(data_kariawan[0]['umur'])}")
print(f"tahun lahir dari {data_kariawan[1]['nama']} adalah {menghitung_tahun_lahir(data_kariawan[1]['umur'])}")
print(f"tahun lahir dari {data_kariawan[2]['nama']} adalah {menghitung_tahun_lahir(data_kariawan[2]['umur'])}")
print(f"tahun lahir dari {data_kariawan[3]['nama']} adalah {menghitung_tahun_lahir(data_kariawan[3]['umur'])}")
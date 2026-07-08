import datetime
tempat_lahir = "Bandung"
tanggal_hari_ini = datetime.datetime.now()


# Kopsurat
print("======== Formating String ========")
print("Tanggal : {0}.\nTempat : {1}".format(tempat_lahir,tanggal_hari_ini))
print("======= Keyword Argument ========")
print("Tanggal : {tanggal}.\nTempat : {tempat}".format(tempat=tempat_lahir,tanggal=tanggal_hari_ini))
print("======= Singkat Argument ========")
print(f"Tanggal : {tanggal_hari_ini}.\nTempat : {tempat_lahir}")
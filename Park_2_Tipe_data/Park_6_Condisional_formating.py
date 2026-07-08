# if
# if statement di gunakan saat kamu punya satu syarat 
nilai = 70
# if kondisi :
#   perintah yang kamu mau lakukan kalau benar kondisinya
print("===== if statement =====")
if nilai > 80 :
    print("Selamat Kamu lulus dalam ujian ini!")

print("===== if else statement =====")
if nilai > 80 :
    print("Selamat Kamu lulus dalam ujian ini!")
else :
    print("Maaf Kamu tidak lulus dalam ujian ini!")

print("===== if elif else statement =====")
if nilai > 80 :
    print("Selamat Kamu lulus dalam ujian ini!")
elif nilai > 60 :
    print("Selamat Kamu lulus dalam ujian ini, tapi harus belajar lebih giat lagi!")
else :
    print("Maaf Kamu tidak lulus dalam ujian ini!")

# if bersarang
print("===== if bersarang =====")
nilai = 95
if nilai > 80 :
    print("Selamat Kamu lulus dalam ujian ini!")
    if nilai > 90 :   
        print("Kamu mendapatkan nilai A!")
    else :
        print("Kamu mendapatkan nilai B!")


# Match and case
print("===== match and case =====")
print("======Menu======")
print("1. Start")
print("2. exit")
selection = input("Masukkan pilihan menu : ")
match selection :
    case "1":
        print("Kamu memilih menu Start")
    case "2":
        print("Kamu memilih menu Exit")
    case _:
        print("Pilihan menu tidak tersedia")
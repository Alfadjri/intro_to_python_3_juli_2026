file = open("../Create/pesan.txt","r")
read = file.read()

print("All value in file : ")
print(read)

file.seek(0)
print("Get 1 line")
for line in file.readlines():
    print(line.strip())
    break


class Animal : 
    nama = "default"
    jenis = "default"
    _umur = 10 #private

    def __init__(self, nama , jenis):
        self.nama = nama
        self.jenis = jenis


    def suara():
        print("Suara belum di Temukan !!!")


    # setter and getter 
    # set itu di gunakan untuk merubah nilai

    def setUmur(self,usia):
        self._umur = usia
    # get itu di gunakan untuk mengambil nilai
    def getProfile(self):
        print("=====================")
        print(f"Nama : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Usia : {self._umur} tahun")
        print("=====================")


kucing = Animal("Tom","Anggora")
kucing.setUmur(2)
kucing.getProfile()


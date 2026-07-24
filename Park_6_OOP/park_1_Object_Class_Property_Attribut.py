class Animal : # ini adalah nama class
    nama = "default" #nama propertynya public : bisa di ubah di manapun
    jenis = "default"
    _umur = 10  #property private : tidak semua oarng bisa lihat

    # Constructor
    def __init__(self, nama , jenis):
        self.nama = nama
        self.jenis = jenis


    #ini di sebut method
    def suara():
        print("Suara belum di Temukan !!!")

    
    def getProfile(self):
        print("=====================")
        print(f"Nama : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Usia : {self._umur} tahun")
        print("=====================")


kucing = Animal("Tom","Anggora") #pemanggilan class dengan Constructor
#memanggil method
kucing.getProfile()

kucing.jenis = "Kucing Kampung"
kucing.umur = 2
kucing.getProfile()






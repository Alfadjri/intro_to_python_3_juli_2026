class Animal : 
    nama =jenis = "default"
    _suara = "default"
    _umur = 10 #private

    def __init__(self, nama = "default" , jenis = "default",suara = "Suara belum di temukan"):
        self.nama = nama
        self.jenis = jenis
        self._suara = suara

    def suara(self):
        print(f"{self._suara}")

    def getSuara(self):
        return self._suara

    def setUmur(self,usia):
        self._umur = usia
    def getProfile(self):
        print("=====================")
        print(f"Nama : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Usia : {self._umur} tahun")
        print("=====================")

class Kucing(Animal):
    def __init__(self,nama,jenis,suara):
        super().__init__(nama,jenis,suara)
    
    #Overite method # menulis code ulang dengan fungsi atau method yang sama 
    def suara(self):
        super().suara() # meneruskan atau menambahkan code 
        print(f"Suara : {self.getSuara()}")

class Tikus(Animal):
    def __init__(self,nama,jenis,suara):
        super().__init__(nama,jenis,suara)
    
    #Overite method # menulis code ulang dengan fungsi atau method yang sama 
    def suara(self):
        super().suara() # meneruskan atau menambahkan code 
        print(f"Suara : {self.getSuara()}")

class Dog(Animal):
    def __init__(self,nama,jenis,suara):
        super().__init__(nama,jenis,suara)
    
    #Overite method # menulis code ulang dengan fungsi atau method yang sama 
    def suara(self):
        super().suara() # meneruskan atau menambahkan code 
        print(f"Suara : {self.getSuara()}")




def getSuara(Animal):
    Animal.suara()


kucing = Kucing("Tom","Anggora", "Meow!!!!!!")
tikus = Tikus("Jeryy","Tikus Rumah","Cit!!!!!")
dog = Dog("Spike","Buldog","Wooffff!!!!!!")


getSuara(kucing)
getSuara(tikus)
getSuara(dog)

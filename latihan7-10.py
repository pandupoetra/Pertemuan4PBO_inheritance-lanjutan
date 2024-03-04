class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id, *args, **kwargs):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

class Pelajar:
    def __init__(self, *args, **kwargs):
        self.matkul = []
    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Pengajar:
    def __init__(self, *args, **kwargs):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)   

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul = []
        self.matkul_diajar = []


# Membuat objek uswatun menggunakan kelas Asdos
uswatun=Asdos("Uswatun","Hasanah","456456")
# Memanggil method enrol untuk menambahkan mata kuliah "Big Data"
uswatun.enrol("Big Data")
# Memanggil method mengajar untuk menambahkan mata kuliah yang diajar "Kecerdasan Artifisial"
uswatun.mengajar("Kecerdasan Artifisial")
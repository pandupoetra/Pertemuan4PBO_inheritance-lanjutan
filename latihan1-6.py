class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id, *args, **kwargs):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

class Mahasiswa(Orang):
    def __init__(self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []

    SARJANA, MASTER, DOKTOR = range(3)

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Karyawan(Orang):
    def __init__(self, status_karyawan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status_karyawan = status_karyawan

    TETAP, TDK_TETAP = range(2)

class Dosen(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul_diajar = []
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

#membuat objek bowo menggunakan kelas mahasiswa
bowo=Mahasiswa("Bowo", "Nugroho", 987654, Mahasiswa.SARJANA)
# Memanggil method enrol untuk menambahkan mata kuliah "Basis Data"
bowo.enrol("Basis Data")

#membuat objek rizki menggunakan kelas mahasiswa
rizki=Dosen("Rizki","Setiabudi","456789",Dosen.TETAP)
# Memanggil method mengajar untuk menambahkan mata kuliah "Statistik"
rizki.mengajar("Statistik")
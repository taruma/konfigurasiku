# Strovers

Strovers merupakan sistem penamaan dokumen/direktori yang saya gunakan. 

-----

## Direktori UTAMA

Berikut struktur folder pada direktori D: (Strovers / **UTAMA**).

### _Special Folder_ / direktori khusus

| Status | Nama | Keterangan |
| :-: | :-- | :-- |
🔴 | `__dropbox` | direktori sementara untuk menampung seluruh dokumen/direktori terlebih dahulu
🔴 | `_app` | kumpulan aplikasi pada sistem yang bersifat _temporary/removable/portable_
☁🔂 | `_github` | kumpulan direktori untuk proyek yang ada di github. Seluruhnya merupakan repo yang sudah terhubung dengan github
 🟢🔂 | `_jupyterdir` | sebagai _working directory_ untuk pekerjaan yang menggunakan jupyter notebook
❌ | `_learn` | kumpulan direktori hasil salinan dari folder lain untuk memudahkan mengakses materi
☁ | `Online` | direktori khusus untuk layanan cloud storage (dropbox/drive/onedrive) dan digunakan sebagai direktori khusus _temporary/cache_ untuk spotify dan IDM. 
🔴 | `Download` | direktori khusus penyimpanan hasil unduh dari berbagai aplikasi (chrome/vivaldi/idm)
🔴 |  `Games` | direktori khusus untuk seluruh game (steam/epic/garena)

### _Main Folder_ / direktori utama

Direktori utama menggunakan format penamaan `XX Y` dengan `XX` bilangan bulat dan `Y` kategori.

| Status | Kode | Nama | Keterangan |
| :-: | :-: | :-- | :-- |
🟢 | UMA | `00 UMA Personal Repository` | Direktori khusus untuk kepentingan pribadi
💾 | SNK | `01 Science and Knowledge` | Tempat untuk menaruh sumber pengetahuan
💾 | VOK | `03 Video of Knowledge` | Koleksi kumpulan video kursus/kuliah online
💾 | CER | `04 Civil Engineering Reference` | Koleksi kumpulan materi mengenai teknik sipil
💾🟢 | RAT | `05 Reference and Textbook` | Perpustakaan digital pribadi
💾🟢 | SCM | `06 School College Material` | Kumpulan akademis
💾🔴 | SAI | `09 Software Application Installation` |	Kumpulan aplikasi
🔴 | ... | `99 Temporary Files` | Direktori sementara

Keterangan:
- 🔴 : Tidak disinkronisasi dengan OneDrive
- 🟢 : Disinkronisasi dengan OneDrive
- ☁ : Online/Cloud
- ❌ : Bisa dihapus
- 🔂 : Sebagai _junction directory_ pada direktori `%USER`
- 💾 : Disimpan pada HDD external.
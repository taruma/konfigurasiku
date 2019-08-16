# Strovers

Strovers merupakan sistem penamaan dokumen/direktori yang saya gunakan. 

-----

## Direktori UTAMA

Berikut struktur folder pada direktori D: (Strovers / **UTAMA**).

### Special Folder

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

Keterangan:
- 🔴 : Tidak disinkronisasi dengan OneDrive
- 🟢 : Disinkronisasi dengan OneDrive
- ☁ : Online/Cloud
- ❌ : Bisa dihapus
- 🔂 : Sebagai _junction directory_ pada direktori `%USER`.













## Jenis Folder

Terdapat dua jenis tanda khusus sebelum `[Folder Name]` yaitu `_` (*underscore*) dan `[00-99]` (dua digit angka `0-9`) yang digunakan oleh saya. 

- `_[Folder Name]`: Tanda `_` sebelum `[Folder Name]`  memisahkan jenis folder lain tanpa `_`. Pemberian tanda `_` pada umumnya digunakan agar menandakan pentingnya folder tersebut baik dalam penggunaan ataupun pencarian, contohnya: 
  - `_app`: aplikasi pada sistem yang bersifat removable/portable, 
  - `_[type]`: digunakan sebagai _working directory_ seperti `_github _jupyterdir _matlab` 
  - memisahkan file yang tidak berkategori sementara (`.\_dropbox`).
  - **pengecualian**: (`.\Download`,`.\Games`,`.\Online`) dibuat tanpa `_` karena bersifat umum dan sudah jelas isinya dengan namanya. 
- `.\[00 - 99] [Folder Name]`: Dua digit angka `XX` didepan `[Folder Name]` menandakan folder tersebut merupakan bagian penting dari `(Root Folder)` atau `.\`, memudahkan pengurutan folder, bagian dari kategori umum. 
- `.\[Folder Name]`: Folder yang tidak diawali tanda/angka apapun merupakan folder yang bersifat umum/general sehingga tidak perlu diberi tanda khusus.

## Struktur Folder

```Information
Update: 20180610

DIREKTORI UTAMA

> _app          :	Application Portable Folder
> _dropbox      :	Temporary/Uncategorized Folder
> _github       :	Github Folder (Online) (Junction to %USER%)
> _jupyterdir   :   Jupyter Notebook Folder (Junction to %USER%)
> _matlab       :	Matlab Folder

> 00 (UMA) UMA Personal Repository:		My Personal Repository (<-> OneDrive)
> 01 (SNK) Science and Knowledge:		GENERAL Knowledge
> 02 (...)
> 03 (VOK) Video of Knowledge:			Collection of GENERAL Course/Learning Video  
> 04 (CER) Civil Engineering Reference:	Civil Engineering Library (Book/Video)
> 05 (RAT) Reference and Textbook:		GENERAL Library (Read Material Only)
> 06 (SCM) School College Material:		Academic Library (Courses/Assignment)
> 07 (...)
> 08 (...)
> 09 (SAI) Software App. Install.:		Software Library
> 99 (...) Temporary Files:				Temporary Folder

> Download:		Download Folder (IDM, Chrome, Firefox, etc.)
> Games:		Gaming Folder
> Online:		Cloud Service Folder (OneDrive, Google, Dropbox)
```


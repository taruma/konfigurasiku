# Script Jupyter Notebook/Lab

## Akses Lokal untuk Google Colab

Berikut isi file `run_tf-colab.bat`, dengan `tf-colab` sebagai nama _environment_ conda:

```bat
@echo off

echo "RUNNING TF-COLAB SERVER"

C:\Miniconda3\python.exe C:\Miniconda3\cwp.py C:\Miniconda3\envs\tf-colab C:\Miniconda3\envs\tf-colab\python.exe C:\Miniconda3\envs\tf-colab\Scripts\jupyter-notebook-script.py --NotebookApp.allow_origin="https://colab.research.google.com" --port=8888 --NotebookApp.port_retries=0 --no-browser --notebook-dir "D:\Online\GoogleDrive\Colab Notebooks"
```

Digunakan `--notebook-dir [Lokasi GoogleDrive]` untuk memudahkan sinkronisasi antara penggunaan saat lokal ataupun _cloud_. 
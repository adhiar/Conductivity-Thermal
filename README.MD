# Sistem Instrumentasi untuk Mengukur Konduktivitas Termal Material dan Suhu Transien

## Gambaran Umum

**Sistem Instrumentasi** ini dikembangkan untuk mengukur konduktivitas termal material dan suhu transien. Sistem ini dibangun menggunakan **mikrokontroler Arduino Uno R3** dan **ruang pemanas** yang dibuat khusus. Data yang dikumpulkan oleh sistem ditransmisikan ke **Python** melalui pustaka serial. Pengaturan ini memungkinkan kontrol yang tepat terhadap instrumentasi, memungkinkan fungsi mulai/berhenti, serta pencatatan data untuk analisis lebih lanjut.

## Fitur

- **Pengukuran Konduktivitas Termal**: Sistem dapat mengukur konduktivitas termal material dengan akurasi tinggi.
- **Pengukuran Suhu Transien**: Memungkinkan pengamatan suhu dalam kondisi transien.
- **Kontrol Presisi**: Fungsi mulai/berhenti untuk kontrol yang mudah.
- **Pencatatan Data**: Data yang dikumpulkan dapat dicatat dan dianalisis lebih lanjut.
- **Antarmuka Grafis Ramah Pengguna**: Dibangun menggunakan pustaka Tkinter di Python, antarmuka ini memungkinkan aksesibilitas bagi siapa saja, bahkan bagi mereka yang tidak familiar dengan Python.

## Teknologi yang Digunakan

- **Arduino Uno R3**: Sebagai komponen perangkat keras utama untuk pengukuran.
- **Python**: Digunakan untuk pemrosesan data dan visualisasi.
- **Tkinter**: Menyediakan antarmuka pengguna grafis.
- **Serial Library**: Untuk komunikasi antara Arduino dan Python.

## Persyaratan

Untuk menjalankan aplikasi Python, Anda perlu menginstal library berikut. Anda dapat menginstalnya menggunakan pip:

```bash
pip install -r requirements_py.txt
```

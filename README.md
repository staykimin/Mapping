
# Aplikasi Mapping dan Tracers Lokasi

    Aplikasi Ini Menggunakan Flask dan Ngrok Sebagai Servernya Serta Program Apk Kimin Tracers Untuk Mengirim Lokasi Terkini Ke Dalam Server Tsb.






## Installation

Cara Install Server

```bash
  pip install -r modul.min
```
    
## Usage/Examples

```python
-> python server.py
-> Masukkan Token Ngrok Kalian
-> Pilih Mode Auto Reload, Jika ya kirim "y" dan jika tidak kirim "t"
```

## Next Update

- Polygon Drawing
- Marker Area
- Warna Marker & Logo Marker
- Costume Tooltip


## Features

- Ambil Lokasi Terkini
- Ambil Semua Data Lokasi Dalam Bentuk API


## Documentation

[Documentation]

- `/maps`  -> Digunakan Untuk Melihat Lokasi Terkini Dalam Bentuk Peta
- `/data`     -> Digunakan Untuk Melihat Semua Data Lokasi Yang Telah Dikirim Dari Apk Kimin Tracers
- `File : db/lokasi.min`    -> Digunakan Untuk Menyimpan Semua Data Lokasi Yang Dikirim Oleh APK Kimin Tracers


## API Reference

#### Kirim Pesan

```http
  POST /
```

| Parameter | Required | Type     | Description                       |
| :-------- | :------- | :------- | :-------------------------------- |
| `label`| `True` | `string` | Label Dari Apk Kimin Tracers |
| `warna` | `True` |`string` | Warna Dari Marker
| `author` | `True` | `string` | Nama Pengirim Data
| `long`| `True` | `string` | Longitude
| `lat` | `False` | `string` | Latitude



# skripsi

## Format 3 - Data Formatting Module

Format 3 adalah modul Python untuk memformat data dalam format terstruktur dengan delimiter dan padding yang dapat disesuaikan.

### Fitur

- Format data dalam bentuk tabel dengan delimiter kustom
- Opsi padding otomatis untuk perataan kolom
- Dukungan untuk multiple data items
- Fungsi quick format untuk penggunaan cepat

### Penggunaan

#### Contoh Dasar

```python
from format3 import Format3

# Data contoh
data = [
    {"Name": "Alice", "Age": 20, "Grade": "A"},
    {"Name": "Bob", "Age": 21, "Grade": "B"},
]

# Buat formatter
formatter = Format3()
result = formatter.format_data(data)
print(result)
```

#### Output:
```
Name   |Age|Grade
-------|---|-----
Alice  |20 |A    
Bob    |21 |B    
```

#### Menggunakan Delimiter Kustom

```python
formatter = Format3(delimiter="::")
result = formatter.format_data(data)
```

#### Tanpa Padding

```python
formatter = Format3(padding=False)
result = formatter.format_data(data)
```

#### Quick Format

```python
from format3 import format3_quick

result = format3_quick(data)
```

### Menjalankan Contoh

```bash
python3 example_format3.py
```

### Struktur File

- `format3.py` - Modul utama Format 3
- `example_format3.py` - Contoh penggunaan
- `test_format3.py` - Unit tests

### Lisensi

MIT License
import sqlite3

# Cria/conecta ao banco
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

# Cria a tabela products
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL,
    brand TEXT NOT NULL,
    rating REAL,
    sales INTEGER DEFAULT 0
)
""")

# Produtos variados
products = [
    ("Notebook IdeaPad 3", "Notebook", 3299.90, 15, "Lenovo", 4.6, 320),
    ("Notebook Aspire 5", "Notebook", 3799.90, 8, "Acer", 4.7, 280),
    ("MacBook Air M3", "Notebook", 8499.90, 5, "Apple", 4.9, 190),

    ("iPhone 15", "Celular", 4299.90, 20, "Apple", 4.8, 850),
    ("Galaxy S24", "Celular", 3999.90, 12, "Samsung", 4.7, 720),
    ("Redmi Note 13", "Celular", 1399.90, 35, "Xiaomi", 4.5, 1100),
    ("Moto G84", "Celular", 1599.90, 25, "Motorola", 4.4, 640),

    ("Monitor UltraGear 24", "Monitor", 1199.90, 18, "LG", 4.7, 410),
    ("Monitor Odyssey G5", "Monitor", 2299.90, 10, "Samsung", 4.8, 350),
    ("Monitor TUF Gaming", "Monitor", 1799.90, 7, "ASUS", 4.6, 290),

    ("Teclado Mecânico K552", "Teclado", 249.90, 40, "Redragon", 4.6, 1250),
    ("Teclado MX Keys", "Teclado", 599.90, 15, "Logitech", 4.8, 730),
    ("Teclado Huntsman Mini", "Teclado", 699.90, 9, "Razer", 4.7, 510),

    ("Mouse G203", "Mouse", 149.90, 50, "Logitech", 4.7, 1800),
    ("Mouse DeathAdder V2", "Mouse", 299.90, 22, "Razer", 4.8, 1200),
    ("Mouse Basilisk V3", "Mouse", 349.90, 14, "Razer", 4.8, 890),

    ("Headset Cloud II", "Headset", 449.90, 17, "HyperX", 4.8, 970),
    ("Headset Blackshark V2", "Headset", 599.90, 11, "Razer", 4.7, 620),
    ("AirPods Pro 2", "Headset", 1899.90, 6, "Apple", 4.9, 450),

    ("SSD NVMe 1TB", "Armazenamento", 499.90, 30, "Kingston", 4.8, 1350),
    ("SSD NVMe 2TB", "Armazenamento", 899.90, 16, "WD", 4.8, 780),
    ("HD 2TB", "Armazenamento", 399.90, 25, "Seagate", 4.5, 560),

    ("Memória RAM 16GB", "Memória", 329.90, 45, "Kingston", 4.7, 1450),
    ("Memória RAM 32GB", "Memória", 649.90, 20, "Corsair", 4.8, 820),
    ("Memória RAM 64GB", "Memória", 1299.90, 8, "Corsair", 4.9, 310),

    ("RTX 4060", "Placa de Vídeo", 1899.90, 10, "Gigabyte", 4.7, 530),
    ("RTX 4070", "Placa de Vídeo", 3899.90, 6, "ASUS", 4.9, 280),
    ("RX 7600", "Placa de Vídeo", 1699.90, 13, "AMD", 4.6, 420),

    ("Ryzen 5 5600", "Processador", 799.90, 18, "AMD", 4.8, 1600),
    ("Ryzen 7 7700", "Processador", 1899.90, 9, "AMD", 4.9, 520),
    ("Core i5-14400F", "Processador", 1399.90, 12, "Intel", 4.7, 680),

    ("Fonte 650W", "Fonte", 399.90, 24, "Corsair", 4.7, 740),
    ("Fonte 750W", "Fonte", 549.90, 15, "Cooler Master", 4.6, 490),
    ("Fonte 850W", "Fonte", 799.90, 8, "XPG", 4.8, 320),

    ("Cadeira ThunderX3", "Cadeira", 1399.90, 7, "ThunderX3", 4.6, 380),
    ("Cadeira DT3 Sports", "Cadeira", 1199.90, 10, "DT3", 4.5, 450),
    ("Cadeira Ergonômica", "Cadeira", 899.90, 14, "Flexform", 4.7, 520),

    ("Webcam C920", "Webcam", 499.90, 18, "Logitech", 4.8, 900),
    ("Webcam StreamCam", "Webcam", 899.90, 7, "Logitech", 4.7, 340),

    ("Roteador AX3000", "Rede", 599.90, 12, "TP-Link", 4.7, 610),
    ("Adaptador Wi-Fi USB", "Rede", 99.90, 35, "TP-Link", 4.4, 1300),
]

# Insere os produtos
cursor.executemany("""
INSERT INTO products
(name, category, price, stock, brand, rating, sales)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", products)

# Salva
conn.commit()

# Mostra quantidade de produtos
cursor.execute("SELECT COUNT(*) FROM products")
total = cursor.fetchone()[0]

print(f"Banco criado com sucesso!")
print(f"Produtos cadastrados: {total}")

conn.close()
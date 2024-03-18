CREATE TABLE IF NOT EXISTS product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    unit_price REAL NOT NULL,
    quantity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS purchase (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    purchase_date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    total_cost REAL NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE IF NOT EXISTS sale (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    sale_date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    total_sale_amount REAL NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

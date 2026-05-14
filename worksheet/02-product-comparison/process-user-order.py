"""
Test target cho Lab 2 — Google Antigravity vs GitHub Copilot.

Cả Hải Văn (Antigravity) và Dũng (Copilot) paste TOÀN BỘ file này vào prompt,
yêu cầu AI refactor thành 3 function:
  1) validate_order_input(user_data, items)
  2) calculate_total_with_tax(items, country, is_premium)
  3) save_order_to_db(db_conn, user_email, totals, items)

Yêu cầu: type hints + docstring + 1 pytest test/function. Giữ nguyên logic.
"""
import sqlite3
from datetime import datetime


def process_user_order(user_data, items, db_conn):
    # Validate user_data
    if not user_data:
        raise ValueError("user_data is required")
    if 'email' not in user_data or '@' not in user_data['email']:
        raise ValueError("invalid email")
    if 'age' not in user_data or user_data['age'] < 18:
        raise ValueError("user must be 18+")
    if user_data.get('country') not in ['VN', 'US', 'JP', 'KR']:
        raise ValueError("country not supported")

    # Validate items
    if not items or len(items) == 0:
        raise ValueError("items cannot be empty")
    for item in items:
        if 'price' not in item or item['price'] <= 0:
            raise ValueError(f"invalid price for {item.get('name', 'item')}")
        if 'quantity' not in item or item['quantity'] <= 0:
            raise ValueError(f"invalid quantity for {item.get('name', 'item')}")

    # Calculate subtotal
    subtotal = 0
    for item in items:
        subtotal += item['price'] * item['quantity']

    # Apply tax based on country
    if user_data['country'] == 'VN':
        tax_rate = 0.10
    elif user_data['country'] == 'US':
        tax_rate = 0.08
    elif user_data['country'] == 'JP':
        tax_rate = 0.10
    elif user_data['country'] == 'KR':
        tax_rate = 0.10
    else:
        tax_rate = 0.0
    tax_amount = subtotal * tax_rate

    # Apply premium discount
    if user_data.get('is_premium'):
        discount = subtotal * 0.05
    else:
        discount = 0
    total = subtotal + tax_amount - discount

    # Save to database
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO orders (user_email, subtotal, tax, discount, total, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (user_data['email'], subtotal, tax_amount, discount, total,
         datetime.now().isoformat()),
    )
    order_id = cursor.lastrowid
    for item in items:
        cursor.execute(
            "INSERT INTO order_items (order_id, name, price, quantity) "
            "VALUES (?, ?, ?, ?)",
            (order_id, item['name'], item['price'], item['quantity']),
        )
    db_conn.commit()
    return {'order_id': order_id, 'total': total}


if __name__ == "__main__":
    # Sanity check — tạo DB in-memory, chạy 1 order mẫu
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        """
        CREATE TABLE orders (id INTEGER PRIMARY KEY AUTOINCREMENT, user_email TEXT,
                             subtotal REAL, tax REAL, discount REAL, total REAL, created_at TEXT);
        CREATE TABLE order_items (id INTEGER PRIMARY KEY AUTOINCREMENT, order_id INTEGER,
                                  name TEXT, price REAL, quantity INTEGER);
        """
    )
    user = {"email": "van@example.com", "age": 25, "country": "VN", "is_premium": True}
    items = [{"name": "Book", "price": 100, "quantity": 2},
             {"name": "Pen", "price": 10, "quantity": 5}]
    print(process_user_order(user, items, conn))

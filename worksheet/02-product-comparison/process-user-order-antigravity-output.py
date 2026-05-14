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
import pytest
from datetime import datetime
from typing import Dict, List, Any, Union

def validate_order_input(user_data: Dict[str, Any], items: List[Dict[str, Any]]) -> None:
    """
    Validates user data and items for processing an order.

    Args:
        user_data (Dict[str, Any]): A dictionary containing user information.
        items (List[Dict[str, Any]]): A list of items in the order.

    Raises:
        ValueError: If user_data or items are missing or invalid.
    """
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

def calculate_total_with_tax(items: List[Dict[str, Any]], country: str, is_premium: bool) -> Dict[str, float]:
    """
    Calculates subtotal, tax, discount, and total for an order.

    Args:
        items (List[Dict[str, Any]]): A list of items with price and quantity.
        country (str): The country code to determine tax rate.
        is_premium (bool): Whether the user is a premium member.

    Returns:
        Dict[str, float]: A dictionary containing subtotal, tax, discount, and total.
    """
    # Calculate subtotal
    subtotal = 0.0
    for item in items:
        subtotal += item['price'] * item['quantity']

    # Apply tax based on country
    if country == 'VN':
        tax_rate = 0.10
    elif country == 'US':
        tax_rate = 0.08
    elif country == 'JP':
        tax_rate = 0.10
    elif country == 'KR':
        tax_rate = 0.10
    else:
        tax_rate = 0.0
    tax_amount = subtotal * tax_rate

    # Apply premium discount
    if is_premium:
        discount = subtotal * 0.05
    else:
        discount = 0.0
    total = subtotal + tax_amount - discount

    return {
        'subtotal': subtotal,
        'tax': tax_amount,
        'discount': discount,
        'total': total
    }

def save_order_to_db(db_conn: sqlite3.Connection, user_email: str, totals: Dict[str, float], items: List[Dict[str, Any]]) -> int:
    """
    Saves the order and its items to the database.

    Args:
        db_conn (sqlite3.Connection): The database connection.
        user_email (str): The email of the user placing the order.
        totals (Dict[str, float]): A dictionary containing subtotal, tax, discount, and total.
        items (List[Dict[str, Any]]): A list of items in the order.

    Returns:
        int: The order ID of the inserted order.
    """
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO orders (user_email, subtotal, tax, discount, total, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (user_email, totals['subtotal'], totals['tax'], totals['discount'], totals['total'],
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
    return order_id

def process_user_order(user_data: Dict[str, Any], items: List[Dict[str, Any]], db_conn: sqlite3.Connection) -> Dict[str, Union[int, float]]:
    """
    Processes a user order by validating inputs, calculating totals, and saving to database.

    Args:
        user_data (Dict[str, Any]): A dictionary containing user information.
        items (List[Dict[str, Any]]): A list of items in the order.
        db_conn (sqlite3.Connection): The database connection.

    Returns:
        Dict[str, Union[int, float]]: A dictionary with the order_id and total.
    """
    # 1. Validate
    validate_order_input(user_data, items)
    
    # 2. Calculate totals
    totals = calculate_total_with_tax(
        items=items, 
        country=user_data.get('country', ''), 
        is_premium=user_data.get('is_premium', False)
    )
    
    # 3. Save to DB
    order_id = save_order_to_db(db_conn, user_data['email'], totals, items)
    
    return {'order_id': order_id, 'total': totals['total']}

# --- Pytest Tests ---

def test_validate_order_input():
    valid_user = {"email": "test@example.com", "age": 20, "country": "VN"}
    valid_items = [{"name": "Item A", "price": 10, "quantity": 1}]
    
    # Should not raise any exception
    validate_order_input(valid_user, valid_items)
    
    # Should raise error for invalid age
    invalid_user = {"email": "test@example.com", "age": 17, "country": "VN"}
    with pytest.raises(ValueError, match="user must be 18\\+"):
        validate_order_input(invalid_user, valid_items)

def test_calculate_total_with_tax():
    items = [{"name": "A", "price": 100, "quantity": 2}] # subtotal = 200
    # VN tax = 10% -> 20. Premium discount = 5% -> 10. Total = 200 + 20 - 10 = 210
    totals = calculate_total_with_tax(items, country="VN", is_premium=True)
    assert totals['subtotal'] == 200.0
    assert totals['tax'] == 20.0
    assert totals['discount'] == 10.0
    assert totals['total'] == 210.0

def test_save_order_to_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        """
        CREATE TABLE orders (id INTEGER PRIMARY KEY AUTOINCREMENT, user_email TEXT,
                             subtotal REAL, tax REAL, discount REAL, total REAL, created_at TEXT);
        CREATE TABLE order_items (id INTEGER PRIMARY KEY AUTOINCREMENT, order_id INTEGER,
                                  name TEXT, price REAL, quantity INTEGER);
        """
    )
    totals = {'subtotal': 100.0, 'tax': 10.0, 'discount': 0.0, 'total': 110.0}
    items = [{"name": "A", "price": 100, "quantity": 1}]
    order_id = save_order_to_db(conn, "test@example.com", totals, items)
    
    assert order_id == 1
    cursor = conn.cursor()
    cursor.execute("SELECT user_email, total FROM orders WHERE id=?", (order_id,))
    order = cursor.fetchone()
    assert order[0] == "test@example.com"
    assert order[1] == 110.0

def test_process_user_order():
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
    
    result = process_user_order(user, items, conn)
    assert result['order_id'] == 1
    # Subtotal: 250. Tax VN: 25. Discount: 12.5. Total: 262.5
    assert result['total'] == 262.5


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

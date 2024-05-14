import requests

def fetch_product_price(product_id):
    response = requests.get(f"<https://api.example.com/products/{product_id}>")
    return response.json()['price']

def calculate_tax(product_id):
    price = fetch_product_price(product_id)
    tax_rate = 0.20  # 20% Tax
    return price * tax_rate


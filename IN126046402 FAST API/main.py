from fastapi import FastAPI

app = FastAPI()

# Product Data
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 799, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "Desk Lamp", "price": 599, "category": "Electronics", "in_stock": False},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]


# Scenario 1 – Get all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total_products": len(products)
    }


# Scenario 2 – Get products by category
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    filtered_products = []

    for p in products:
        if p["category"].lower() == category_name.lower():
            filtered_products.append(p)

    return {
        "category": category_name,
        "matched_products": filtered_products,
        "count": len(filtered_products)
    }


# Scenario 3 – Get only in-stock products
@app.get("/products/instock")
def get_instock_products():

    instock_products = []

    for p in products:
        if p["in_stock"] == True:
            instock_products.append(p)

    return {
        "instock_products": instock_products,
        "count": len(instock_products)
    }


# Scenario 4 – Store summary
@app.get("/store/summary")
def store_summary():

    total_products = len(products)
    in_stock = 0
    categories = []

    for p in products:

        if p["in_stock"] == True:
            in_stock += 1

        if p["category"] not in categories:
            categories.append(p["category"])

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock,
        "out_of_stock": total_products - in_stock,
        "categories": categories
    }


# Scenario 5 – Search products
@app.get("/products/search")
def search_products(query: str):

    matched_products = []

    for p in products:
        if query.lower() in p["name"].lower():
            matched_products.append(p)

    return {
        "search_query": query,
        "matched_products": matched_products,
        "count": len(matched_products)
    }


# Scenario 6 – Best deal and premium pick
@app.get("/products/highlights")
def product_highlights():

    best_deal = min(products, key=lambda p: p["price"])
    premium_pick = max(products, key=lambda p: p["price"])

    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }

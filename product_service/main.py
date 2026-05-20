from fastapi import FastAPI

STUDENT_N = 1

app = FastAPI(title="Product Service")

PRODUCTS = {
    101: {
        "id": 101,
        "name": "Laptop",
        "price": 1000,
        "stock": 5
    },
    102: {
        "id": 102,
        "name": "Mouse",
        "price": 25,
        "stock": 50
    }
}


@app.get("/products")
def get_products():
    return {
        "student_id": STUDENT_N,
        "products": list(PRODUCTS.values())
    }


@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id in PRODUCTS:
        return {
            "student_id": STUDENT_N,
            "product": PRODUCTS[product_id]
        }

    return {
        "error": "Product not found"
    }
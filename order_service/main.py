from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

STUDENT_N = 1

app = FastAPI(title="Order Service")

PRODUCT_SERVICE_URL = "http://product-service:8000"

ORDERS = []


class OrderRequest(BaseModel):
    product_id: int
    quantity: int


@app.post("/orders")
def create_order(order: OrderRequest):

    response = requests.get(
        f"{PRODUCT_SERVICE_URL}/products/{order.product_id}"
    )

    if response.status_code != 200:
        raise HTTPException(
            status_code=400,
            detail="Product not found"
        )

    product_data = response.json()["product"]

    new_order = {
        "student_id": STUDENT_N,
        "order_id": len(ORDERS) + 1,
        "product_name": product_data["name"],
        "quantity": order.quantity,
        "total_price": product_data["price"] * order.quantity
    }

    ORDERS.append(new_order)

    return new_order
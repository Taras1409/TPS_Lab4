from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

STUDENT_N = 1

app = FastAPI(title="Payment Service")

BILL_SERVICE_URL = "http://bill-service:8000"

PAYMENTS = []


class PaymentRequest(BaseModel):
    bill_id: int
    card_number: str


@app.post("/payments")
def create_payment(payment: PaymentRequest):
    response = requests.get(
        f"{BILL_SERVICE_URL}/bills/{payment.bill_id}"
    )

    if response.status_code != 200:
        raise HTTPException(
            status_code=400,
            detail="Bill not found"
        )

    bill_data = response.json()["bill"]

    new_payment = {
        "student_id": STUDENT_N,
        "payment_id": len(PAYMENTS) + 1,
        "bill_id": payment.bill_id,
        "service_name": bill_data["service_name"],
        "provider": bill_data["provider"],
        "amount": bill_data["amount"],
        "status": "paid"
    }

    PAYMENTS.append(new_payment)

    return new_payment


@app.get("/payments")
def get_payments():
    return {
        "student_id": STUDENT_N,
        "payments": PAYMENTS
    }
from fastapi import FastAPI, HTTPException

STUDENT_N = 1

app = FastAPI(title="Bill Service")

BILLS = {
    101: {
        "id": 101,
        "service_name": "Electricity",
        "provider": "Ivano-Frankivsk Energy",
        "amount": 450.0,
        "status": "unpaid"
    },
    102: {
        "id": 102,
        "service_name": "Water Supply",
        "provider": "Vodokanal",
        "amount": 220.0,
        "status": "unpaid"
    }
}


@app.get("/bills")
def get_bills():
    return {
        "student_id": STUDENT_N,
        "bills": list(BILLS.values())
    }


@app.get("/bills/{bill_id}")
def get_bill(bill_id: int):
    if bill_id not in BILLS:
        raise HTTPException(status_code=404, detail="Bill not found")

    return {
        "student_id": STUDENT_N,
        "bill": BILLS[bill_id]
    }
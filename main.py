from fastapi import FastAPI, HTTPException, status
from model import PaymentRequest

app = FastAPI()


@app.post("/process_payment/", status_code=status.HTTP_200_OK)
async def process_payment(payment: PaymentRequest):
    if validate_payment(payment):
        return {"message": "Payment processed successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payment processing failed")

def validate_payment(payment: PaymentRequest):
    if payment.amount > 0 and payment.card_number.startswith("4"):
        return True
    return False

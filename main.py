from fastapi import FastAPI, HTTPException, status
from model import PaymentRequest

app = FastAPI()

def validate_payment(payment: PaymentRequest):
    # Validate payment amount
    if payment.amount <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payment amount must be positive")

    # Validate card number length
    if len(payment.card_number) != 16:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid card number length")

    # Validate CVV length
    if len(payment.cvv) != 3 and len(payment.cvv) != 4:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid CVV length")

def authenticate_payment(payment: PaymentRequest):
    # Simulate authentication by checking card number prefix
    if not payment.card_number.startswith("1234"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized payment")

@app.post("/process_payment/", status_code=status.HTTP_200_OK)
async def process_payment(payment: PaymentRequest):
    # Validate payment
    validate_payment(payment)

    # Authenticate payment
    authenticate_payment(payment)
    return {"message": "Payment processed successfully"}

from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints, validator
from datetime import datetime


class PaymentRequest(BaseModel):
    amount: Annotated[int, Field(gt=0)]
    card_number: Annotated[str, StringConstraints(min_length=16, max_length=16, pattern=r"^[0-9]{16}$")]
    expiration_date: Annotated[
        str, StringConstraints(pattern=r"^(0[1-9]|1[0-2])\/\d{2}$")
    ]
    cvv: Annotated[str, StringConstraints(min_length=3, max_length=4, pattern="^[0-9]{3}$")]


    @validator("expiration_date")
    def validate_expiration_date(cls, value):
        expiration_month, expiration_year = map(int, value.split("/"))
        current_month = datetime.now().month
        current_year = datetime.now().year % 100
        if expiration_year < current_year or (
            expiration_year == current_year and expiration_month < current_month
        ):
            raise ValueError("Expiration date is expired")
        return value

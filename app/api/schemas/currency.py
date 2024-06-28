from pydantic import BaseModel, constr


class CurrencyConvert(BaseModel):
    amount: int
    from_currency: constr(min_length=3, max_length=3)
    to_currency: constr(min_length=3, max_length=3)

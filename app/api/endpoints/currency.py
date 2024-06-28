from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from app.utils.external_api import CurrencyAPI
from ..schemas.currency import CurrencyConvert
from app.core.security import get_user_from_token, get_user


currency_route = APIRouter(
    prefix='/currency'
)


@currency_route.get('/exchange/')
async def convert_currency(
        to_currency: str,
        from_currency: str,
        amount: int,
        cur_user: str = Depends(get_user_from_token)):
    user = get_user(cur_user)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    else:
        user_currency = CurrencyAPI()
        result = user_currency.get_convert(
            query_params=CurrencyConvert(
                to_currency=to_currency,
                from_currency=from_currency,
                amount=amount
            )
        )

        return {'rate': result}


@currency_route.get('/list')
async def get_currency_list(cur_user: str = Depends(get_user_from_token)):
    user = get_user(cur_user)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    else:
        users_currency_list = CurrencyAPI()
        return users_currency_list.get_list()


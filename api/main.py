"""ATM API Main Entry Point"""
from typing import Optional

from atm.controller import AtmController
from atm.exceptions import InsufficientFunds, NoAccountFound
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .models import AccountInput

app = FastAPI()
atm = AtmController()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"message": "Invalid Data passed", "data": {}}),
    )


@app.get("/accounts")
async def get_accounts():
    """Retrieves all Accounts"""
    accounts = atm.get_accounts()
    return {"data": accounts}


@app.get("/account/{account_id}")
async def get_account(account_id: int):
    """Retrieve single account"""
    try:
        account = atm.get_account(account_id)
    except (NoAccountFound, ValueError):
        return {"data": {}, "message": f"No account with id: {account_id} was found."}
    return {"data": account}


@app.post("/account/{account_id}/deposit")
async def account_deposit(account_id: int, item: AccountInput):
    """Deposits money into an account"""
    try:
        results = atm.deposit(account_id, item.amount)
        return {"data": results}
    except NoAccountFound:
        return {"data": {}, "message": f"No account with id: {account_id} was found."}


@app.post("/account/{account_id}/withdraw")
async def account_withdraw(account_id: int, item: AccountInput):
    """Withdraws money from an account"""
    try:
        results = atm.withdraw(account_id, item.amount)
        return {"data": results}
    except InsufficientFunds:
        return {"data": {}, "message": f"Account {account_id} has insufficient funds to process draw for {item.amount}"}

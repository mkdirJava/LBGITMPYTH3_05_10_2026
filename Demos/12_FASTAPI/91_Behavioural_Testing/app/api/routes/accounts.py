from fastapi import APIRouter, Depends, HTTPException

from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)
from app.schemas.account import AccountResponse
from app.services.account_service import AccountService
from app.core.security import (
    create_token,
    get_current_user,
)

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(request: LoginRequest):

    user = AccountService.authenticate(
        request.username,
        request.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    return {
        "access_token": create_token(
            request.username
        )
    }


@router.get(
    "/accounts/me",
    response_model=AccountResponse,
)
def get_account(
    user=Depends(get_current_user),
):
    return {
        "account_id": user["account_id"],
        "balance": user["balance"],
        "currency": "GBP",
    }
from fastapi import APIRouter, Query, Depends

from app.utils.response import build_json_response
from app.utils.cleaners import clean_account_number, clean_transaction_type
from app.api.deps import get_transaction_service

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/health")
def health():
    return build_json_response(200, {"status": "ok"})


@router.get("/")
def get_transactions(
    account_number: str = Query(..., description="8-digit bank account number"),
    query_service=Depends(get_transaction_service),
):
    cleaned_account_number = clean_account_number(account_number)
    if cleaned_account_number is None:
        return build_json_response(
            400, {"error": "account_number must be an 8-digit numeric string"}
        )

    transactions = query_service(account_number=cleaned_account_number)

    if not transactions:
        return build_json_response(
            404,
            {
                "error": "No transactions found",
                "account_number": cleaned_account_number,
            },
        )

    return build_json_response(
        200,
        {
            "account_number": cleaned_account_number,
            "count": len(transactions),
            "transactions": transactions,
        },
    )


@router.get("/filter")
def get_transactions_by_type(
    account_number: str = Query(...),
    transaction_type: str = Query(...),
    query_service=Depends(get_transaction_service),
):
    cleaned_account_number = clean_account_number(account_number)
    if cleaned_account_number is None:
        return build_json_response(
            400, {"error": "account_number must be an 8-digit numeric string"}
        )

    cleaned_transaction_type = clean_transaction_type(transaction_type)
    if cleaned_transaction_type is None:
        return build_json_response(
            400, {"error": "transaction_type must be 'deposit' or 'withdrawal'"}
        )

    transactions = query_service(
        account_number=cleaned_account_number,
        transaction_type=cleaned_transaction_type,
    )

    if not transactions:
        return build_json_response(
            404,
            {
                "error": "No transactions found",
                "account_number": cleaned_account_number,
                "transaction_type": cleaned_transaction_type,
            },
        )

    return build_json_response(
        200,
        {
            "account_number": cleaned_account_number,
            "transaction_type": cleaned_transaction_type,
            "count": len(transactions),
            "transactions": transactions,
        },
    )

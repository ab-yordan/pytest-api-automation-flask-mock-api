def get_transaction_history_api():
    from .transaction_history import transactionHistoryRequest

    return transactionHistoryRequest


def bank_account_api():
    from .bank_account import bankAccountRequest

    return bankAccountRequest

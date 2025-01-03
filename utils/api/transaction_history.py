from .endpoint import baseUrl, path
import requests
import logging

logger = logging.getLogger(__name__)


class transactionHistoryRequest:
    def get_transaction_history():
        endpoint = baseUrl.base_url + path.transaction_history
        headers = {"Accept": "application/json"}
        res = requests.get(endpoint, headers=headers)
        return transactionHistoryResponse(res)

    def add_new_transaction_history(xid, amount, date, description):
        endpoint = baseUrl.base_url + path.transaction_history
        headers = {"Accept": "application/json"}
        json = {"xid": xid, "amount": amount, "date": date, "description": description}
        res = requests.post(endpoint, headers=headers, json=json)
        return transactionHistoryResponse(res)


class transactionHistoryResponse:
    def __init__(self, res):
        self.status_code = res.status_code
        self.response = res.json()
        logger.info(self.response)

    def get_response_status_code(self):
        return self.status_code

    def get_transactions(self):
        return self.response["transactions"]

    def get_transaction_xid(self):
        self.transaction_xid = [
            transaction_xid["xid"] for transaction_xid in self.response["transactions"]
        ]
        return self.transaction_xid

    def get_response_message(self):
        return self.response["message"]

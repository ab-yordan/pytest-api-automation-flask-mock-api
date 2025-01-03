from .endpoint import baseUrl, path
import requests
import logging

logger = logging.getLogger(__name__)


class bankAccountRequest:
    def get_bank_account(customer_id):
        endpoint = baseUrl.base_url + path.bank_account
        headers = {"Accept": "application/json"}
        json = {"customer_id": customer_id}
        res = requests.get(endpoint, headers=headers, json=json)
        return bankAccountResponse(res)

    def get_bank_account_without_body():
        endpoint = baseUrl.base_url + path.bank_account
        headers = {"Accept": "application/json"}
        res = requests.get(endpoint, headers=headers)
        return bankAccountResponse(res)


class bankAccountResponse:
    def __init__(self, res):
        self.status_code = res.status_code
        self.response = res.json()
        logger.info(self.response)

    def get_response_status_code(self):
        return self.status_code

    def get_customer_email(self):
        return self.response["email"]

    def get_full_name(self):
        return self.response["full_name"]

    def get_account_id(self):
        self.account_number = [
            account_number["account_number"]
            for account_number in self.response["account"]
        ]
        return self.account_number

    def get_error_message(self):
        return self.response["error"]

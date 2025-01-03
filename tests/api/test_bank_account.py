from utils.api import bank_account_api
from utils.data import get_customer
import logging

logger = logging.getLogger(__name__)


def test_get_bank_account_details():
    bank_account = bank_account_api()
    customer_data = get_customer()

    response = bank_account.get_bank_account(customer_id=customer_data.customer_id)
    response_status_code = response.get_response_status_code()
    print(response.get_account_id())

    logger.info("assertion api status code: 200")
    assert response_status_code == 200


def test_check_customer_email():
    bank_account = bank_account_api()
    customer_data = get_customer()

    response = bank_account.get_bank_account(customer_id=customer_data.customer_id)
    email = response.get_customer_email()

    logger.info("assertion response email should be: {}".format(customer_data.email))
    assert email == customer_data.email


def test_check_customer_full_name():
    bank_account = bank_account_api()
    customer_data = get_customer()

    response = bank_account.get_bank_account(customer_id=customer_data.customer_id)
    full_name = response.get_full_name()

    logger.info(
        "assertion response full name should be: {}".format(customer_data.full_name)
    )
    assert full_name == customer_data.full_name


def test_invalid_customer_id():
    bank_account = bank_account_api()

    response = bank_account.get_bank_account(customer_id=12345)
    response_status_code = response.get_response_status_code()
    response_error_message = response.get_error_message()

    logger.info("assertion api status code: 404")
    assert response_status_code == 404

    logger.info("assertion api error message: 'data not found'")
    assert response_error_message == "data not found"


def test_request_without_body():
    bank_account = bank_account_api()
    response = bank_account.get_bank_account_without_body()
    response_status_code = response.get_response_status_code()
    response_error_message = response.get_error_message()

    logger.info("assertion api status code: 400")
    assert response_status_code == 400

    logger.info("assertion api error message: 'invalid request'")
    assert response_error_message == "invalid request"


def test_check_bank_account_exist():
    bank_account = bank_account_api()
    customer_data = get_customer()

    response = bank_account.get_bank_account(customer_id=customer_data.customer_id)
    customer_account_numbers = response.get_account_id()

    logger.info(
        "assertion account number {} exist in response".format(
            customer_data.account_number
        )
    )
    assert customer_data.account_number in customer_account_numbers

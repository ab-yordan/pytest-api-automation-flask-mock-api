from utils.api import get_transaction_history_api
from utils.data import get_transaction
import logging

logger = logging.getLogger(__name__)


class TestTransactionHistory:
    def test_get_transaction_history(self):
        transaction_history = get_transaction_history_api()

        response = transaction_history.get_transaction_history()
        response_status_code = response.get_response_status_code()

        logger.info("assertion api status code: 200")
        assert response_status_code == 200

    def test_add_new_transaction_history(self):
        transaction_history = get_transaction_history_api()
        transaction_data = get_transaction()

        response = transaction_history.add_new_transaction_history(
            xid=transaction_data.xid,
            amount=transaction_data.amount,
            date=transaction_data.date,
            description=transaction_data.description,
        )
        response_status_code = response.get_response_status_code()
        response_message = response.get_response_message()

        logger.info("assertion api status code: 201")
        assert response_status_code == 201

        logger.info("assertion api message: 'success add new transaction history'")
        assert response_message == "success add new transaction history"

        response_get = transaction_history.get_transaction_history()
        list_transaction_xid = response_get.get_transaction_xid()

        logger.info(
            "assertion transaction xid {} exist in response".format(
                transaction_data.xid
            )
        )
        assert transaction_data.xid in list_transaction_xid

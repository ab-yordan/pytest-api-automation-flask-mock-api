from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/api/bank-account", methods=["GET"])
def bank_account():
    try:
        request_data = json.loads(request.data)
        with open("sample_test_api/data/bank_account.txt", "r") as f:
            data = f.read()
            records = json.loads(data)
            if records["customer_id"] == request_data["customer_id"]:
                return jsonify(records)
            else:
                return jsonify({"error": "data not found"}), 404
    except ValueError:
        return jsonify({"error": "invalid request"}), 400
    except KeyError:
        return jsonify({"error": "customer_id is required"}), 400


@app.route("/api/bank-account-transactions-history", methods=["GET"])
def bank_account_transactions_history():
    try:
        request_data = json.loads(request.data)
        with open(
            "sample_test_api/data/bank_account_transactions_history.txt", "r"
        ) as f:
            data = f.read()
            records = json.loads(data)
            if (
                records["account_id"] == request_data["account_id"]
                and records["account_number"] == request_data["account_number"]
            ):
                return jsonify(records)
            else:
                return jsonify({"error": "data not found"}), 404
    except ValueError:
        return jsonify({"error": "invalid request"}), 400
    except KeyError:
        return jsonify({"error": "account_id and account_number is required"}), 400


@app.route("/api/transaction-history", methods=["GET"])
def get_incomes():
    with open("sample_test_api/data/transaction_history.json", "r") as f:
        data = f.read()
        records = json.loads(data)
        return jsonify(records)


@app.route("/api/transaction-history", methods=["POST"])
def test_add():
    with open("sample_test_api/data/transaction_history.json", "r") as f:
        data = f.read()
        records = json.loads(data)
    transactions = records["transactions"]
    transactions.append(request.get_json())
    f = open("sample_test_api/data/transaction_history.json", "w")
    f.write(json.dumps(records))
    return (
        jsonify({"success": True, "message": "success add new transaction history"}),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)

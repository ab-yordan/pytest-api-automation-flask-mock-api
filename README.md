# Pytest API Automation with Flask Mock API
 Pytest API Automation with Flask Mock API Sample Project

# Prerequisites
 * Python 3.9.13 
 * Pip 22.0.4
 * Setup python venv
 * Setup flask
 * Setup pytest requests

# Python venv
1. Download or clone the repository 
2. Open a terminal and go to the project root directory
3. Create a virtual environment or venv: `py -m venv venv`
4. Activate virtual environment: `.\venv\Scripts\activate`

Reference: [venv — Creation of virtual environments](<https://docs.python.org/3/library/venv.html>)

# Flask
1. When the virtual environment is active, run the following command: `pip install Flask`
2. To run the application, use the flask command or python
```
flask --app .\sample_test_api\main.py run
or
python .\sample_test_api\main.py
```
3. After running try to hit the following endpoint
```
curl --location --request GET '<localhost>/api/bank-account' \
--header 'Content-Type: application/json' \
--data '{
    "customer_id": 10011
}'
```
4. The endpoint response will come from `.\sample_test_api\data\bank_account.txt`

Reference: 
 * [Flask-Quickstart](<https://flask.palletsprojects.com/en/stable/quickstart/>)
 * [Flask REST API Tutorial](<https://pythonbasics.org/flask-rest-api/>)

# Pytest
1. While flask running, open new terminal
2. Install pytest `pip install -U pytest`
3. Install pytest-html `pip install pytest-html`
4. Install request `pip install requests`
5. Run all test case `pytest .\tests\api`
6. Run specific file `pytest .\tests\api\test_bank_account.py`
7. Run specific test `pytest .\tests\api\test_bank_account.py::test_get_bank_account_details`



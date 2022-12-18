# Software testing assignment 3 - Online Pizza Delivery

## Requirements
- Requires python 3.x + pip (I used 3.10.6 but it might (or might not) work with other versions)
- Also requires xampp (for windows)
- The browsers you intend to use to test the application with

## Setting up

- Do as instructed in the [original repo](https://github.com/darshankparmar/OnlinePizzaDelivery) (at the time of writing this the demo website is gone so a local setup is required, if anyone wants to find a way to host/deploy the website + database then be my guest)
- Install dependencies
```
pip install -U -r requirements.txt
```

## Usage

### Windows
```
python -m pytest
```
or just
```
pytest
```

## Technicals

Tests are defined in test_\*.py, inside a Test* class (optional), and in a test_* function

- test_opd.py includes test cases for the sign up and order feature of the OPD application
    - all tests are run using 1 pre-configured browser with 2 different window sizes (to emulate desktop and mobile versions) (check the @pytest.mark.parametrize decorator)

- opd_helper.py contains helpful utilities for both client and server

- _test_config.py defines generic variables needed to run tests like database credentials, etc (not to be confused with test data)
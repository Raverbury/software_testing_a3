import requests
import uuid

def get_url_from_registration(username, email, phone, password, cpassword):
  url = 'http://onlinepizzadelivery.infinityfreeapp.com/OnlinePizzaDelivery/partials/_handleSignup.php'
  data = {
    'username': username,
    'firstName': 'FN',
    'lastName': 'Herstal',
    'email': email,
    'phone': phone,
    'password': password,
    'cpassword': cpassword
  }
  response = requests.post(url, data)
  return response.url if response.status_code == 200 else response.reason

def test_signup_normal():
  assert get_url_from_registration(str(uuid.uuid4()), '', '', '', '') == 'http://onlinepizzadelivery.infinityfreeapp.com/OnlinePizzaDelivery/index.php?signupsuccess=true'

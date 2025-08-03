from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import accounts as controller
from ..models import accounts as model
from ..models.accounts import Accounts as Models

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_overall(db_session):
    test_data1 = {
        "name": "John Doe",
        "pay_name": "John D",
        "pay_num": "1346321343",
        "pay_sec": "235",
        "email": "JD@gmail.com",
        "phone_num": "123 424 1234",
        "address": "123 address drive",
        "username": "JohnUserName",
        "password": "JohnPassword"
    }
    test_object1 = Models(**test_data1)
    created_test_object1 = controller.create(db_session, test_object1)
    print(created_test_object1)
    assert test_object1 == 1
    #this should fail
    test_data1_1f = {
        "name": "John Doe",
        "pay_name": "John D",
        "pay_num": "1346321343",
        "pay_sec": "235",
        "email": "JD@gmail.com",
        "phone_num": "123 424 1234",
        "address": "123 address drive",
        "username": "JohnUserName",
        "password": "JohnPassword"
    }
    test_object1_1f = Models(**test_data1_1f)
    created_test_object1_1f = controller.create(db_session, test_object1_1f)
    assert created_test_object1_1f.id == None
    test_data2 = {
        "name": "John2 Doe",
        "pay_name": "John2 D",
        "pay_num": "46532",
        "pay_sec": "123",
        "email": "JD2@gmail.com",
        "phone_num": "3223 424 1234",
        "address": "222 address drive",
        "username": "2JohnUserName",
        "password": "2JohnPassword"
    }
    test_object2 = Models(**test_data2)
    created_test_object2 = controller.create(db_session, test_object2)
    assert created_test_object2 == 2
    test_data3 = {
        "name": "John Doe",
        "pay_name": "John D",
        "pay_num": "1346321343",
        "pay_sec": "235",
        "email": "JD@gmail.com",
        "phone_num": "123 424 1234",
        "address": "123 address drive",
        "username": "JohnUserName",
        "password": "JohnPassword"
    }
    test_object3 = Models(**test_data3)
    created_test_object3 = controller.create(db_session, test_object3)
    test_data4 = {
        "name": "John Doe",
        "pay_name": "John D",
        "pay_num": "1346321343",
        "pay_sec": "235",
        "email": "JD@gmail.com",
        "phone_num": "123 424 1234",
        "address": "123 address drive",
        "username": "JohnUserName",
        "password": "JohnPassword"
    }
    test_object4 = Models(**test_data4)
    created_test_object4 = controller.create(db_session, test_object4)
def test_create_account(db_session):
    # Create a sample account
    test_data = {
        "name": "John Doe",
        "pay_name": "John D",
        "pay_num": "1346321343",
        "pay_sec": "235",
        "email": "JD@gmail.com",
        "phone_num": "123 424 1234",
        "address": "123 address drive",
        "username": "JohnUserName",
        "password": "JohnPassword"
    }

    test_object = Models(**test_data)

    # Call the create function
    created_test_object = controller.create(db_session, test_object)

    # Assertions
    assert created_test_object is not None
    #TODO: find out if using test_data.varname is bad practice(since i am persuming it dosnt change)
    assert created_test_object.name == test_data["name"]
    assert created_test_object.pay_num == test_data["pay_num"]
    assert created_test_object.pay_num == test_data["pay_num"]
    assert created_test_object.pay_sec == test_data["pay_sec"]
    assert created_test_object.email == test_data["email"]
    assert created_test_object.phone_num == test_data["phone_num"]
    assert created_test_object.address == test_data["address"]
    assert created_test_object.username == test_data["username"]
    assert created_test_object.password == test_data["password"]


#TODO: updates-> test overall, test trying to change id, change email to one that another accounts have(should fail),
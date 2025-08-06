from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import logs_in as controller
from ..models import accounts as model
from ..models.logs_in import Login as Models
from datetime import datetime

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_overall(db_session):
    test_data1 = {
        "username": "JohnUserName",
        "password": "JohnPassword"
    }
    test_object1 = Models(**test_data1)
    created_test_object1 = controller.create(db_session, test_object1)
    print(created_test_object1)
    assert test_object1 == 1
    #this should fail
    test_data1_1f = {
        "username": "JohnUseName",
        "password": "JohnPasswod"
    }
    test_object1_1f = Models(**test_data1_1f)
    created_test_object1_1f = controller.create(db_session, test_object1_1f)
    assert created_test_object1_1f.id == None
    test_data2 = {
        "username": "2JohnUserName",
        "password": "2JohnPassword"
    }
    test_object2 = Models(**test_data2)
    created_test_object2 = controller.create(db_session, test_object2)
    assert created_test_object2 == 2
    test_data3 = {
        "username": "JohnUserName",
        "password": "JohnPassword"
    }
    test_object3 = Models(**test_data3)
    created_test_object3 = controller.create(db_session, test_object3)
    test_data4 = {
        "username": "JohnUserName",
        "password": "JohnPassword"
    }
    test_object4 = Models(**test_data4)
    created_test_object4 = controller.create(db_session, test_object4)
def test_create_account(db_session):
    # Create a sample account
    test_data = {
        "username": "JohnUserName",
        "password": "JohnPassword"
    }

    test_object = Models(**test_data)

    # Call the create function
    created_test_object = controller.create(db_session, test_object)

    # Assertions
    assert created_test_object is not None

    assert created_test_object.username == test_data["username"]
    assert created_test_object.password == test_data["password"]



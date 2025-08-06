from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import logs_out as controller
from ..models import accounts as model
from ..models.logs_out import Logout as Models
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
    assert created_test_object1.id == 1
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
    assert created_test_object2.id == 2
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

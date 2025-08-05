from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import orders as controller
from ..models import orders as model
from ..models.orders import Orders as Models

# Create a test client for the app
client = TestClient(app)
test_data = {
    "name":"ordersName1",
    "total": 1.42
}

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_orders(db_session):
    test_object = Models(**test_data)

    # Call the create function
    created_test_object = controller.create(db_session, test_object)

    # Assertions
    assert created_test_object is not None
    assert created_test_object.name == test_data["name"]
    assert created_test_object.total == test_data["total"]
    #TODO: find out if using test_data.varname is bad practice(since i am persumeing it dosnt change)
    #TODO: do all vars

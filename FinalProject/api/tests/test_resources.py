
from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import resources as controller
from ..models import resources as model
from ..models.resources import Resource as Models

# Create a test client for the app
client = TestClient(app)
test_data = {
    "name":"ResourceName1",
    "amount_in_storage": 23
}

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_sample(db_session):

    test_object = Models(**test_data)

    # Call the create function
    created_test_object = controller.create(db_session, test_object)

    # Assertions
    assert created_test_object is not None
    assert created_test_object.name == test_data["name"]
    assert created_test_object.amount_in_storage == test_data["amount_in_storage"]
    #TODO: find out if using test_data.varname is bad practice(since i am persumeing it dosnt change)
    #TODO: do all vars
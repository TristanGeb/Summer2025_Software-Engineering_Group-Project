
from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import reviews as controller
from ..models import reviews as model
from ..models.reviews import Reviews as Models

# Create a test client for the app
client = TestClient(app)
test_data = {
    "name": "review1",
    "body": "body for test1",
    "rating": 4
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
    assert created_test_object.body == test_data["body"]
    assert created_test_object.rating == test_data["rating"]
    #TODO: find out if using test_data.varname is bad practice(since i am persumeing it dosnt change)
    #TODO: do all vars
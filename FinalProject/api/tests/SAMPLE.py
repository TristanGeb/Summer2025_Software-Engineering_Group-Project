#Sample -> Object
#samples -> objects
#sample -> object
"""
from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import sample as controller
from ..models import sample as model
from ..models.sample import Samples as Models

# Create a test client for the app
client = TestClient(app)
test_data = {
    "":""
    #TODO: add Create data
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
    #TODO: find out if using test_data.varname is bad practice(since i am persumeing it dosnt change)
    #TODO: do all vars
"""

from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..controllers import menu_items as controller
from ..models import menuitems as model
from ..models.menuitems import MenuItems as Models

# Create a test client for the app
client = TestClient(app)
test_data = {
    "name":"menuItemName1",
    "price": 1.24,
    "food_category":"MenuItem_1_category",
    "calories": 123
}

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_menuItem(db_session):

    test_object = Models(**test_data)

    # Call the create function
    created_test_object = controller.create(db_session, test_object)

    # Assertions
    assert created_test_object is not None
    assert created_test_object.name == test_data["name"]
    assert created_test_object.price == test_data["price"]
    assert created_test_object.food_category == test_data["food_category"]
    assert created_test_object.calories == test_data["calories"]
    #TODO: find out if using test_data.varname is bad practice(since i am persumeing it dosnt change)
    #TODO: do all vars

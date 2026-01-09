from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

def test_patch_order_by_id():
    order_data = {"pet_id": 2}
    create_response = api_helpers.post_api_data("/store/order", order_data)
    
    assert create_response.status_code == 201
    
    order_id = create_response.json()["id"]
    
    update_data = {"status": "sold"}
    patch_response = api_helpers.patch_api_data(f"/store/order/{order_id}", update_data)
    
    assert patch_response.status_code == 200
    
    # Verify response message
    assert patch_response.json()["message"] == "Order and pet status updated successfully"
import sender_stand_request
import data
from data import kit_body
from sender_stand_request import authtoken


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    response_status_code = kit_response.status_code
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name
    print(response_status_code)


def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response_kit = sender_stand_request.post_new_client_kit(kit_body)
    response_kit_status_code = response_kit.status_code
    assert response_kit.status_code == 400
    assert response_kit.json()["code"] == 400


def test_create_kit_body_1_letter_in_name():
    positive_assert('a')

def test_create_kit_body_511_letter_in_name():
    positive_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

def test_create_kit_body_0_letter_in_name_error():
    negative_assert_code_400("")

def test_create_kit_body_512_letter_in_name_error():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_body_special_symbols_letter_in_name():
    positive_assert("№%@")

def test_create_kit_body_has_space_letter_in_name():
    positive_assert("A Aaa")

def test_create_kit_body_has_number_letter_in_name():
    positive_assert("123")

def test_create_kit_body_no_name_error():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

def test_create_kit_body_number_type_in_name_error():
    negative_assert_code_400(123)
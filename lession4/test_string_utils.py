import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive_test(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative_test(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_data, expected_result", [
    ("     skypro", "skypro"),
    ("hello", "hello"),
    ("   with spaces   ", "with spaces   "),
    ("  ", "")
])
def test_trim_positive_test(input_data, expected_result):
    assert string_utils.trim(input_data) == expected_result


@pytest.mark.negative_test
@pytest.mark.parametrize("invalid_input", [
    (123),
    (True),
    (["string"])
])
def test_trim_negative_types(invalid_input):
    with pytest.raises(AttributeError):
        string_utils.trim(invalid_input)


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, input_sym, res_bool", [
    ("Skypro", "S", True),
    ("Skypro", "Z", False),
    ("TU134", "4", True),
])
def test_contains_positive_test(input_str, input_sym, res_bool):
    assert string_utils.contains(input_str, input_sym) == res_bool


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, input_sym, res_bool", [
    ("123", "З", False),
    ("&^%$#", "&", True),
    ("", " ", False),
])
def test_contains_negative_test(input_str, input_sym, res_bool):
    assert string_utils.contains(input_str, input_sym) == res_bool


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, input_sym, res_str", [
    ("Skypro", "k", "Sypro"),
    ("Skypro", "pro", "Sky"),
    ("Tororo", "o", "Trr"),
])
def test_delete_symbol_positive_test(input_str, input_sym, res_str):
    assert string_utils.delete_symbol(input_str, input_sym) == res_str


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, input_sym, res_str", [
    ("", "qwert", ""),
    ("^%$#@", "$", "^%#@"),
    ("ASD", "123", "ASD"),
])
def test_delete_symbol_negative_test(input_str, input_sym, res_str):
    assert string_utils.delete_symbol(input_str, input_sym) == res_str

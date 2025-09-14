"""
Author: Thailis Gonzalez
Purpose: Test the functions from the file logic.py to verify their work
"""
import pytest
import os
from logic import ( read_findings_existing, save_find, search_by_field, delete_find, \
    CODE_INDEX, NAME_INDEX, MATERIAL_INDEX, DATED_INDEX, DESCRIPTION_INDEX
)

#file to test
test_object = "test_warehouse_objects.csv" 


@pytest.fixture(scope="module", autouse=True)

def file_for_test():
    """Create a CSV test file before tests and delete it after all tests finish"""

    with open(test_object, "w", newline="", encoding="utf-8") as csvfile:

        csvfile.write("code,name,material,dated,description\n")
        csvfile.write("001,Vase,Clay,500 BC,Ancient clay vase\n")
        csvfile.write("002,Statue,Stone,300 BC,Marble statue\n")

    yield test_object 

    if os.path.exists(test_object):
        os.remove(test_object)


def test_read_findings_existing(file_for_test):
    """Test the function read_findings_existing"""

    stored_objects, error = read_findings_existing(file_for_test, CODE_INDEX)
    assert error is None
    assert "001" in stored_objects
    assert stored_objects["002"][NAME_INDEX] == "Statue"


def test_save_find(file_for_test):
    """Test the function save_find"""

    error = save_find(file_for_test, "003", "Coin", "Gold", "100 BC", "Ancient gold coin")
    assert error is None

    stored_objects, error = read_findings_existing(file_for_test, CODE_INDEX)
    assert "003" in stored_objects
    assert stored_objects["003"][NAME_INDEX] == "Coin"


def test_search_by_field(file_for_test):
    """Test the function search_by_field"""

    results = search_by_field(file_for_test, [NAME_INDEX], "Statue")
    assert len(results) == 1
    assert results[0][CODE_INDEX] == "002"


def test_delete_find(file_for_test):
    """Test the function delete_find"""

    stored_objects, error = read_findings_existing(file_for_test, CODE_INDEX)
    assert "002" in stored_objects

    error = delete_find(file_for_test, "002")
    assert error is None

    stored_objects, error = read_findings_existing(file_for_test, CODE_INDEX)
    assert "002" not in stored_objects

    error = delete_find(file_for_test, "999")
    assert error is not None

pytest.main(["-v", "--tb=line", "-rN", __file__])
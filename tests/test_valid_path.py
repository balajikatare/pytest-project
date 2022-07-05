
import os
import pytest


@pytest.mark.parametrize("source_path", ["C:\\Users\\Balaji Katare\\practice-projects\\pytest-project\\tests\\__init__.py",
                                         "C:\\Users\\Balaji Katare\\practice-projects\\pytest-project\\tests\pytest.ini"])
def test_source_path(souce_path):
    import os
    assert os.path.exists(souce_path) == True, "Source path is invalid"

#
# def test_destination_path(destination_path):
#     assert os.path.exists(destination_path) == True, "In-valid destination path"

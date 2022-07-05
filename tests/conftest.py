import pytest

@pytest.fixture()
def get_spark_session_from_conf_file():
    spark = "This is spark session object"
    return spark
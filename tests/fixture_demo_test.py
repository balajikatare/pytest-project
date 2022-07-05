import pytest


@pytest.fixture
def get_spark_session():
    spark = "this is spark session object"
    return spark


def test_source_df(get_spark_session):
    assert "session" in get_spark_session


def test_target_df(get_spark_session):
    assert "spark" in get_spark_session
